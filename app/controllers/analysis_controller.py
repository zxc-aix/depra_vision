import pandas as pd
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QImage

from app.analysis.factory import create_analyzer
from app.ui.dialogs import SaveImgaeDialog
from app.visualization.analysis_visual import AnalysisVisual

from .output_results_controller import OutputResultsController


class AnalysisController(QObject):
    def __init__(self, widget_ui, state):
        super().__init__()
        self.widget_ui = widget_ui
        self.state = state

        self.video_configure = state.video
        self.field_configure = state.field
        self.animal_configure = state.animal
        self.analisis_configure = state.analysis
        self.data_to_export = pd.DataFrame([])
        self.stats = None

        self._on_field_changed(self.field_configure)
        self.apply_state_to_ui(self.analisis_configure)
        self._setup_signals()

    def _setup_signals(self):
        self.state.video_changed.connect(self._on_video_changed)
        self.state.field_changed.connect(self._on_field_changed)
        self.state.animal_changed.connect(self._on_animal_changed)

        self.widget_ui.start_analysis_clicked.connect(self.start_analysis)
        self.widget_ui.save_graph_clicked.connect(self.on_save_graph)
        self.widget_ui.data_export_clicked.connect(self.on_data_export)
        self.widget_ui.load_data_clicked.connect(self.on_load_data)

    def _on_video_changed(self, video):
        self.video_configure = video

    def _on_field_changed(self, field):
        self.field_configure = field
        is_activate = True if field.mode == "morris" else False
        self.widget_ui.enabled_elements(is_activate)

    def _on_animal_changed(self, animal):
        self.animal_configure = animal

    def apply_state_to_ui(self, cfg):
        self.widget_ui.ui.chbShStEn.setChecked(cfg.ShStEn)
        self.widget_ui.ui.checkbDiveTraj.setChecked(cfg.DiveTraj)
        self.widget_ui.ui.chbAddZones.setChecked(cfg.AddZones)

        self.widget_ui.ui.dsbScale.setValue(cfg.Scale)
        self.widget_ui.ui.dsbThError.setValue(cfg.ThError)
        self.widget_ui.ui.dsbSpdThFS.setValue(cfg.speed_threshold)
        self.widget_ui.ui.dsbStopSpdTh.setValue(cfg.freeze_threshold)
        self.widget_ui.ui.dsbStopTimeTh.setValue(cfg.min_freeze_duration)

        self.widget_ui.ui.chbWrap.setChecked(cfg.Wrap)
        self.widget_ui.ui.chbBuildBr.setChecked(cfg.BuildBr)

        self.widget_ui.ui.dsbScale.setValue(cfg.Thick)
        self.widget_ui.ui.sbAngleDist.setValue(cfg.AngleDist)
        self.widget_ui.ui.sbAngleTime.setValue(cfg.AngleTime)
        self.widget_ui.ui.sbAnglePer.setValue(cfg.AnglePer)
        self.widget_ui.ui.sbTimeStart.setValue(cfg.TimeStart)
        self.widget_ui.ui.sbTimeEnd.setValue(cfg.TimeEnd)
        self.widget_ui.ui.sbT0.setValue(cfg.T0)
        self.widget_ui.ui.sbT1.setValue(cfg.T1)
        self.widget_ui.ui.sbT2.setValue(cfg.T2)
        self.widget_ui.ui.sbT3.setValue(cfg.T3)
        self.widget_ui.ui.dsblWidthTraj.setValue(cfg.WidthTraj)
        self.widget_ui.ui.dsbWidthMarkup.setValue(cfg.WidthMarkup)

    def start_analysis(self,):
        print("Анализ")
        add_params = self.get_params()
        field_configure = self.field_configure.copy()

        raw_points, ok = self.load_points(ann_dir=self.video_configure.annotate_dir, name=self.video_configure.video_name)
        if not ok:
            return

        analyzer = create_analyzer(raw_points.copy(), field_configure, add_params)
        results = analyzer.run()

        warnings = results.get("warnings", [])
        if warnings:
            for war in warnings:
                self.widget_ui.show_error(war)

        self.stats = results["stats"]
        self.data_to_export = results["points"]
        print(results["stats"])

        visual_settings = self.widget_ui.collect_settings()
        visual_settings["fps"] = self.video_configure.fps
        visual_settings["field_size"] = self.field_configure.field_size

        visual_data = self.prepare_data_to_visualization(raw_points.copy(), visual_settings["Scale"])

        visualizer = AnalysisVisual(self.field_configure.mode, visual_data, visual_settings, field_configure)
        image = visualizer.create_visualization()
        self.widget_ui.set_image(image)

    def load_points(self, ann_dir, name):
        if ann_dir:
            try:
                path = ann_dir + name + "_data.csv"
                df = pd.read_csv(path, sep=',')

                df['is_invalid'] = (df['xc'] <= 10) & (df['yc'] <= 10)
                if len(df) < 2 or len(df[~df['is_invalid']]) == 0:
                    self.widget_ui.show_error("Not enough points or detection problems. Please, check the video processing results.")
                    return [], False

                return df[['xc', 'yc', 'is_invalid']], True
            
            except FileNotFoundError:
                self.widget_ui.show_error(f"File .csv not found at path {path}.")
                return [], False
            except Exception as e:
                self.widget_ui.show_error(f"Error loading CSV: {e}")
                return [], False
        else:
            self.widget_ui.show_error("Directory not found")
            return [], False

    def get_params(self):
        params = self.widget_ui.collect_params()
        params["fps"] = self.video_configure.fps

        return params
    
    def prepare_data_to_visualization(self, raw_points, scale):
        pixel_size = self.field_configure.pixel_size
        w_label, h_label = self.widget_ui.get_size_label()
        target_size = min(w_label, h_label)

        factor = target_size * scale / 100

        x_raw_center, y_raw_center = self.field_configure.p_center

        raw_points['is_invalid'] = (raw_points['xc'] <= 10) & (raw_points['yc'] <= 10)
        visual_points = pd.DataFrame()
        visual_points['xc'] = (raw_points['xc'] - x_raw_center) * pixel_size * factor + target_size / 2
        visual_points['yc'] = (raw_points['yc'] - y_raw_center) * pixel_size * factor + target_size / 2
        visual_points['is_invalid'] = raw_points['is_invalid']

        visual_center = (int(target_size / 2), int(target_size / 2))
        visual_dots = []
        dots = self.field_configure.p
        if dots:
            for i in range(len(dots)):
                x_raw, y_raw = dots[i]
                x = (x_raw - x_raw_center) * pixel_size * factor + target_size / 2
                y = (y_raw - y_raw_center) * pixel_size * factor + target_size / 2

                visual_dots.append([x, y])

        return {
            "visual_points": visual_points,
            "visual_center": visual_center,
            "visual_dots": visual_dots,
            "target_size": target_size,
            "factor": factor,
        }
    
    @Slot(QImage)
    def on_save_graph(self, image):
        dialog = SaveImgaeDialog(image, self.state.app.trajectory_dir, "trajectory")
        dialog.exec()

    def on_data_export(self):
        if self.data_to_export.empty:
            self.widget_ui.show_error("First, build the trajectory graph!")
            return
        folder_dir = self.state.video.annotate_dir
        if not folder_dir:
            self.widget_ui.show_error("First, process the video!")
            return
        
        self.data_to_export.to_csv(folder_dir + "data.csv", index=False)
        self.widget_ui.show_info("File with data exported!")

    def on_load_data(self):
        if not self.stats:
            self.widget_ui.show_error("First, build the trajectory graph!")
            return
        
        controller = OutputResultsController(
            self.field_configure.mode, 
            self.video_configure.dict(), 
            self.animal_configure.dict(), 
            self.field_configure.dict(), 
            self.stats, 
            self.state.video.annotate_dir,
            language="en"
        )
        controller.run()

    def get_configuration(self):
        new_settings = self.widget_ui.collect_settings()
        new_params = self.widget_ui.collect_params()
        self.analisis_configure = self.analisis_configure.model_copy(update=new_settings)
        self.analisis_configure = self.analisis_configure.model_copy(update=new_params)

        return self.analisis_configure