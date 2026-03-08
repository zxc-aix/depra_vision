
import cv2
import numpy as np
from PySide6.QtCore import QObject, Slot

from app.ui.dialogs import LoadedDialog
from app.utils.selectable import RangeSlider
from app.utils.selectable.handler import Handler


class VideoTrimmerController(QObject):
    def __init__(self, dialog_ui, video_configure):
        super().__init__()
        self.dialog_ui = dialog_ui
        self.video_configure = video_configure
        self.mode = None
        self.handler = None

        self.crop_area = None
        self.selected_areas = []
        self.angle = 0

        self.currnet_frame_number = 1
        self.is_add_video = False
        self.path_save = None

        self._init_variables()
        self._setup_signals()

    def _setup_signals(self):
        self.slider.rangeChanged.connect(self.on_range_changed)
        self.slider.handleMoved.connect(self.on_frame_changed)
        self.dialog_ui.mode_changed.connect(self.on_mode_changed)
        self.dialog_ui.color_changed.connect(self.handler.set_color)
        self.dialog_ui.delete_zone_clicked.connect(self.handler.delete_last_area)
        self.dialog_ui.clear_zone_clicked.connect(self.handler.clear_select_areas)
        self.dialog_ui.angle_changed.connect(self.on_angle)
        self.dialog_ui.clear_crop_clicked.connect(self.handler.clear_crop)
        self.dialog_ui.save_clicked.connect(self.on_save)

    def _init_variables(self):
        self.cap = cv2.VideoCapture(self.video_configure.current_path)
        self.total_frames = self.video_configure.frame_count
        self.fps = self.video_configure.fps
        self.width_ = self.video_configure.width
        self.height_ = self.video_configure.height

        self.handler = Handler(mode = None)
        self.dialog_ui.ui.lblImage.set_handler(self.handler)
        self.handler.set_real_size(self.width_, self.height_)

        self.slider = RangeSlider(0, self.total_frames-1)
        self.dialog_ui.setup_slider(self.slider)

        self.on_frame_changed('start', 0)

    @Slot(int, int)
    def on_range_changed(self, start, end):
        start_time = self.format_time(start)
        end_time = self.format_time(end)
        self.dialog_ui.set_label_info(start_time, end_time)

    def format_time(self, frame_num):
        total_seconds = frame_num / self.fps
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int((total_seconds - int(total_seconds)) * 1000)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    
    @Slot(int, int)
    def on_frame_changed(self, handle=None, frame_number=None):
        if frame_number:
            self.currnet_frame_number = frame_number
        else:
            frame_number = self.currnet_frame_number

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.cap.read()
        if not ret:
            return
        
        rotated_frame = self.rotate_frame_keep_size(frame, self.angle)
        rotated_frame = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2RGB)

        try:
            self.dialog_ui.set_image(rotated_frame)
           
        except Exception as e:
            print(f"DEBUG: Ошибка при отображении кадра {frame_number}: {e}")


    @Slot(str)
    def on_mode_changed(self, new_mode):
        if new_mode != self.mode:
            self.handler.set_mode(new_mode)
            print("mode in apply_mode:", new_mode)
        # else:
        #     self.handler.set_mode(None)

    @Slot(float)
    def on_angle(self, value):
        self.angle = value
        self.on_frame_changed()

    def on_save(self):
        start_frame = self.slider.start
        end_frame = self.slider.end
        crop_area, selected_areas = self.handler.get_areas(is_scaled=True)
        bgr_color = self.handler.get_color()
        angle = self.angle
        self.path_save = self.video_configure.current_path.replace(".mp4", "_edited.mp4")
        self.is_add_video = self.dialog_ui.get_video_add()

        print(f"Сохранение с параметрами: start={start_frame}, end={end_frame}, angle={angle}, color={bgr_color}")
        print(f"Выбранные зоны: {selected_areas}")
        print(f"Зона обрезки: {crop_area}")

        dialog = LoadedDialog()
        dialog.start_requested.connect(lambda: self.process_video(start_frame, end_frame, angle, crop_area, selected_areas, bgr_color, dialog, save_path=self.path_save))
        dialog.exec()
        
        self.dialog_ui.accept()

    def process_video(self, start_frame, end_frame, angle, crop_area, selected_areas, bgr_color, dialog, save_path=None):
        total_frames = end_frame - start_frame + 1

        fps = self.cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = None
        dialog.show_processing()

        for i in range(total_frames):
            current_frame_number = start_frame + i
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_number)
            ret, frame = self.cap.read()
            if not ret:
                break

            rotated_frame = self.rotate_frame_keep_size(frame, angle)

            if selected_areas:
                cv2.fillPoly(rotated_frame, selected_areas, bgr_color)

            if crop_area is not None:
                x, y, w, h = cv2.boundingRect(crop_area)
                cropped = rotated_frame[y:y+h, x:x+w]

                mask = np.zeros((h, w), dtype=np.uint8)
                shifted = crop_area - np.array([x, y])
                cv2.fillPoly(mask, [shifted], 255)

                rotated_frame = cv2.bitwise_and(cropped, cropped, mask=mask)
        
            if save_path is not None and writer is None:
                h_out, w_out = rotated_frame.shape[:2]
                writer = cv2.VideoWriter(save_path, fourcc, fps, (w_out, h_out))

            if writer is not None:
                writer.write(rotated_frame)

            progress = int((i / total_frames) * 100)
            dialog.show_progress(progress)

        if writer is not None:
            writer.release()

        dialog.show_success("Видео успешно обработано!")

    def get_configure(self):
        return {
            "is_add_video": self.is_add_video,
            "path_save": self.path_save
        }

    @staticmethod
    def rotate_frame_keep_size(frame, angle):
        h, w = frame.shape[:2]
        center = (w // 2, h // 2)
        
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(frame, rotation_matrix, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
        return rotated