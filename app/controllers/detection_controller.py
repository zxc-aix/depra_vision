
import cv2
from PySide6.QtCore import QObject, QThread

from app.detection.factory import DetectionModelFactory
from app.detection.worker import DetectionWorker


class DetectionController(QObject):
    def __init__(self, dialog_ui, video_configure, model_name, save_dir):
        self.dialog_ui = dialog_ui
        self.video_configure = video_configure
        self.model_name = model_name
        self.save_dir = save_dir
        self.results = {}

        self._setup_signals()

    def _setup_signals(self):
        self.dialog_ui.start_requested.connect(self.start)

    def start(self):
        path = self.save_dir + self.video_configure.video_name + "_annotated.mp4"
        out = cv2.VideoWriter(
            path,
            self.video_configure.fourcc,
            self.video_configure.fps,
            (self.video_configure.width, self.video_configure.height),
        )

        model, model_type = DetectionModelFactory.create(mode=self.model_name)
        print(f"MODEL_TYPE: {model_type}")

        self.dialog_ui.show_processing()
        self.thread = QThread()

        self.worker = DetectionWorker(
            video_path=self.video_configure.current_path,
            model=model,
            model_type=model_type,
            out=out,
        )

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.progress.connect(self.dialog_ui.show_progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.dialog_ui.show_error)

        self.thread.start()

    def on_finished(self, result: dict):
        csv_name = result.get("csv_name")
        data = result.get("data")

        if csv_name and data is not None:
            data.to_csv(f"{self.video_configure.annotate_dir}/{csv_name}", index=False)
            self.video_configure.is_annotated = True
            self.dialog_ui.show_success()
        else:
            self.dialog_ui.show_error("Empty processing result")

    def get_configuration(self):
        return self.video_configure
