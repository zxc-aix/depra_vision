import json
import os
import tempfile
from datetime import datetime
from pathlib import Path

import cv2
from PySide6.QtCore import QObject, QUrl, Slot
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QDialog, QFileDialog, QGraphicsScene

from app.controllers import (
    AnalysisController,
    DetectionController,
    FieldSettingsController,
    HeatmapController,
    VideoTrimmerController,
)
from app.ui.dialogs import (
    AnimalCardDialog,
    AppPathSettingsDialog,
    FieldSettingsDialog,
    LoadedDialog,
    ThemeLanguageDialog,
    VideoTrimmerDialog,
)
from app.ui.widget import AnalysisWidget, HeatmapWidget


class AppController(QObject):
    
    def __init__(self, main_window, state_manager, PREDICTIONS_DIR, VIDEOS_DIR):
        super().__init__()
        self.main_window = main_window
        self.state_manager = state_manager

        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.main_window.get_video_item())

        self.main_window.open_clicked.connect(self.on_open)
        self.main_window.play_clicked.connect(self.on_play)
        self.main_window.pause_clicked.connect(self.on_pause)
        self.main_window.stop_clicked.connect(self.on_stop)
        self.main_window.slider_moved.connect(self.on_slider_moved)
        self.main_window.field_settings_clicked.connect(self.on_field_settings)
        self.main_window.animal_card_clicked.connect(self.on_animal_card)
        self.main_window.detection_clicked.connect(self.on_detection)
        self.main_window.analysis_clicked.connect(self.on_analysis)
        self.main_window.heatmap_clicked.connect(self.on_heatmap)
        self.main_window.video_trim_clicked.connect(self.on_video_trim)
        self.main_window.app_path_settings_clicked.connect(self.on_app_path_settings)
        self.main_window.theme_language_clicked.connect(self.on_theme_language)

        self.media_player.positionChanged.connect(self.on_position)
        self.media_player.durationChanged.connect(self.on_duration)

        self.media_player.positionChanged.connect(self.on_position_changed)
        self.media_player.durationChanged.connect(self.on_duration_changed)

    @Slot()
    def on_open(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Select a video file",
            self.state_manager.app.videos_dir,
            "Video (*.mp4 *.avi *.mov *.mkv); All files (*) (*.*)"
        )
        if file_path:
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.on_pause()
            
            meta = self._get_video_metadata(file_path, self.state_manager.app.predictions_dir)
            self.state_manager.update_video(**meta)

            print(self.state_manager.video)      

    @Slot()
    def on_play(self):
        self.media_player.play()

    @Slot()
    def on_pause(self):
        self.media_player.pause()

    @Slot()
    def on_stop(self):
        self.media_player.stop()

    @Slot(int)
    def on_slider_moved(self, pos: int):
        self.media_player.setPosition(pos)

    @Slot(int)
    def on_position_changed(self, pos: int):
        self.main_window.ui.progressSlider.setValue(pos)

    @Slot(int)
    def on_duration_changed(self, duration: int):
        self.main_window.ui.progressSlider.setRange(0, duration)

    def on_position(self, pos: int):
        self.main_window.set_position(pos)

    def on_duration(self, dur: int):
        self.main_window.set_duration(dur)

    @Slot(QGraphicsScene)
    def update_scene(self, scene: QGraphicsScene):
        # Передача сцены в UI
        self.main_window.set_scene_signal.emit(scene)

    # Открытие диалога настроек поля
    @Slot()
    def on_field_settings(self):
        self.on_pause()

        def cleanup():
            try:
                os.remove(temp_path)
            except Exception as e:
                print("Ошибка удаления временного файла:", e)

        if self.state_manager.video.video_name is None:
            self.main_window.show_error("Open video file first!")
            return

        temp_path = self.create_timestamp()
        dialog = FieldSettingsDialog(temp_path)
        controller = FieldSettingsController(dialog, self.state_manager.field.model_copy())
        dialog.controller = controller
        dialog.finished.connect(cleanup)
        if dialog.exec() == QDialog.Accepted:
            # print(f"Пользователь применил новую конфигурацию")
            new_settings = controller.get_configuration()
            self.state_manager.update_field(**new_settings.dict())
            # print("Новые настройки:", self.state_manager.field)

            state_manager = self.state_manager
            dump_dict = self.fill_dump(state_manager.video, state_manager.field)
            # print(f"DEBUG: dump_data = {dump_dict}")
            path = state_manager.video.annotate_dir + state_manager.video.video_name + "_cfg.json"
            # print(f"DEBUG: dump.json = {path}")
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(dump_dict, f, indent=4, ensure_ascii=False)
        else:
            print("Отмена изменений конфигурации теста")

    def fill_dump(self, video, field):
        return {
            "p_center": field.p_center,
            "p": field.p,
            "pixel_size": field.pixel_size,
            "mode": field.mode,
            "fps": video.fps,
            "areaInt": field.dict().get(field.mode).get("areaInt", None)
        }

    def create_timestamp(self):
        # Чтение кадра и создание временного файла
        is_playing = self.media_player.playbackState() == QMediaPlayer.PlayingState
        if is_playing:
            self.media_player.pause()

        current_pos = self.media_player.position()
        fps = self.state_manager.video.fps
        frame_number = int(current_pos / 1000 * fps)

        cap = cv2.VideoCapture(self.state_manager.video.current_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        # Чтение кадра из видео
        success, frame = cap.read()
        cap.release()
        if not success:
            print("Не удалось прочитать кадр из видео")
            return
        # Сохранение кадра во временный файл
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        temp_path = temp_file.name
        temp_file.close()
        cv2.imwrite(temp_path, frame)

        return temp_path
    
    @Slot()
    def on_animal_card(self):
        self.on_pause()
        dialog = AnimalCardDialog(self.state_manager.animal.model_copy())
        if dialog.exec() == QDialog.Accepted:
            # print(f"Пользователь применил новые параметры объекта")
            new_settings = dialog.get_configuration()
            self.state_manager.update_animal(**new_settings.dict())
            # print("Параметры объекта:", self.state_manager.animal)
        else:
            print("Отмена изменений конфигурации объекта")

    @Slot()
    def on_video_trim(self):
        self.on_pause()
        if not self.state_manager.video.valid:
            self.main_window.show_error("First, open the video file!")
            return
        
        print("Открытие диалога обрезки видео")

        dialog = VideoTrimmerDialog()
        controller = VideoTrimmerController(dialog, self.state_manager.video.model_copy())
        dialog.controller = controller
        if dialog.exec() == QDialog.Accepted:
            # print("Пользователь обрезал видео")
            new_settings = controller.get_configure()
            if new_settings.get("is_add_video", False) and new_settings.get("path_save", None):
                self.media_player.setSource(new_settings.get("path_save"))

                meta = self._get_video_metadata(new_settings.get("path_save"), self.state_manager.app.predictions_dir)
                self.state_manager.update_video(**meta)
        else:
            print("Отмена обрезки видео")

    @Slot()
    def on_detection(self):
        self.on_pause()
        if self.state_manager.video.video_name is None:
            self.main_window.show_error("Open video file first!")
            return
            
        model_name = self.state_manager.field.model
        annotate_dir = self.state_manager.video.annotate_dir

        dialog = LoadedDialog()
        controller = DetectionController(dialog, self.state_manager.video.copy(), model_name, annotate_dir)
        dialog.controller = controller
        if dialog.exec() == QDialog.Accepted:
            print("Успешная обработка видео")
            new_settings = controller.get_configuration()
            self.state_manager.update_video(**new_settings.dict())
            
            path = self.state_manager.video.annotate_dir + self.state_manager.video.video_name + "_annotated.mp4"
            self.media_player.setSource(path)

        else:
            print("Произошла ошибка в обработке видео")

    @Slot()
    def on_analysis(self):
        self.on_pause()
        self.analysis_widget = AnalysisWidget()
        self.analysis_widget.widget_closed.connect(self.on_analysis_closed)

        self.analysis_controller = AnalysisController(self.analysis_widget, self.state_manager)
        self.analysis_widget.controller = self.analysis_controller
        self.analysis_widget.show()

    def on_analysis_closed(self):
        new_settings = self.analysis_controller.get_configuration()
        self.state_manager.update_analysis(**new_settings.dict())
        print("Параметры объекта:", self.state_manager.analysis)

        self.analysis_widget = None
        self.analysis_controller = None

    @Slot()
    def on_heatmap(self):
        self.on_pause()
        self.heatmap_widget = HeatmapWidget()
        self.heatmap_widget.widget_closed.connect(self.on_heatmap_closed)

        self.heatmap_controller = HeatmapController(self.heatmap_widget, self.state_manager.heatmap, self.state_manager.app.predictions_dir, self.state_manager.app.heatmap_dir)
        self.heatmap_widget.controller = self.heatmap_controller
        self.heatmap_widget.show()

    def on_heatmap_closed(self):
        new_settings = self.heatmap_controller.get_configuration()
        self.state_manager.update_heatmap(**new_settings.dict())
        print("Параметры объекта:", self.state_manager.heatmap)

        self.heatmap_widget = None
        self.heatmap_controller = None

    def on_app_path_settings(self):
        self.on_pause()
        dialog = AppPathSettingsDialog(self.state_manager.app.model_copy())
        if dialog.exec() == QDialog.Accepted:
            print("Пользователь применил новые параметры путей")
            new_settings = dialog.get_configure()
            self.state_manager.update_app(**new_settings)
            print("Новые параметры путей:", self.state_manager.app)
        else:
            print("Отмена изменений параметров путей")

    def on_theme_language(self):
        self.on_pause()
        dialog = ThemeLanguageDialog(self.state_manager.app.model_copy())
        if dialog.exec() == QDialog.Accepted:
            print("Пользователь применил новые параметры путей")
            new_settings = dialog.get_configure()
            self.state_manager.update_app(**new_settings)
            print("Новые параметры путей:", self.state_manager.app)
            
        else:
            print("Отмена изменений параметров путей")


    @staticmethod
    def _get_video_metadata(file_path: str, prediction_dir: str) -> dict:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise ValueError("Unable to open video file")
        
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        
        cap.release()
        name = Path(file_path).stem

        timestamp = os.path.getctime(file_path)
        date = datetime.fromtimestamp(timestamp).date().strftime("%d.%m.%Y")
        time = datetime.fromtimestamp(timestamp).time().strftime('%H:%M:%S')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        annotate_dir = f"{prediction_dir}/{name}_date={timestamp}/"
        os.makedirs(annotate_dir)

        return {
            'video_name' : name,
            'width': width,
            'height': height,
            'fps': fps,
            'frame_count': frame_count,
            'fourcc': fourcc,
            'valid': True,
            'date': date,
            'time': time,
            'current_path': file_path,
            'is_annotated': False,
            'annotate_dir': annotate_dir
        }
