from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QMessageBox
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem
from PySide6.QtCore import Signal, Qt, Slot

from app.ui.components import UI_MainWindow

class VideoPlayer(QMainWindow):
    # Сигналы UI
    open_clicked = Signal()
    play_clicked = Signal()
    pause_clicked = Signal()
    stop_clicked = Signal()
    slider_moved = Signal(int)
    field_settings_clicked = Signal()
    animal_card_clicked = Signal()
    detection_clicked = Signal()
    analysis_clicked = Signal()
    heatmap_clicked = Signal()
    video_trim_clicked = Signal()
    app_path_settings_clicked = Signal()
    theme_language_clicked = Signal()

    set_scene_signal = Signal(QGraphicsScene)

    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.video_item = QGraphicsVideoItem()
        self.scene.addItem(self.video_item)
        self.ui.viewVideo.setScene(self.scene)

        self._position = 0
        self._duration = 0

        self._setup_signals()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.fit_video_to_view()

    def fit_video_to_view(self):
        if not self.video_item:
            return

        view = self.ui.viewVideo
        self.video_item.setSize(view.size())
        view.fitInView(self.video_item, Qt.KeepAspectRatio)

    def _setup_signals(self):
        self.set_scene_signal.connect(self.set_scene)

        self.ui.btnOpen.clicked.connect(self.open_clicked.emit)
        self.ui.btnPlay.clicked.connect(self.play_clicked.emit)
        self.ui.btnPause.clicked.connect(self.pause_clicked.emit)
        self.ui.btnStop.clicked.connect(self.stop_clicked.emit)
        self.ui.btnSettings.clicked.connect(self.field_settings_clicked.emit)
        self.ui.btnAnimalCard.clicked.connect(self.animal_card_clicked.emit)
        self.ui.btnDetect.clicked.connect(self.detection_clicked.emit)
        self.ui.btnTrajectory.clicked.connect(self.analysis_clicked.emit)
        self.ui.btnHeatmap.clicked.connect(self.heatmap_clicked.emit)
        self.ui.btnTrim.clicked.connect(self.video_trim_clicked.emit)

        # self.ui.action_about.setEnabled(True) 
        self.ui.action_about.triggered.connect(self.show_about)

        # self.ui.action_settings.setEnabled(True)
        self.ui.action_settings.triggered.connect(self.app_path_settings_clicked.emit)

        self.ui.action_theme_language.triggered.connect(self.theme_language_clicked.emit)

        self.ui.progressSlider.sliderMoved.connect(self.slider_moved.emit)

    def set_scene(self, scene: QGraphicsScene):
        self.scene = scene
        self.ui.viewVideo.setScene(scene)

    def get_video_item(self):
        return self.video_item
    
    def set_position(self, pos: int):
        self._position = pos
        self._update_time_label()

    def set_duration(self, dur: int):
        self._duration = dur
        self._update_time_label()

    def _update_time_label(self):
        current = self._format_time(self._position)
        total = self._format_time(self._duration)
        self.ui.lblTime.setText(f"{current} / {total}")

    def show_about(self):
        QMessageBox.about(self, "About the application", "If you have any questions or suggestions about our software, we are always available: \nEmail: data.sup@yandex.ru \nTelegram: @aixgb")

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)

    @staticmethod
    def _format_time(ms):
        seconds = (ms // 1000) % 60
        minutes = (ms // (1000 * 60)) % 60
        hours = ms // (1000 * 60 * 60)
        return (
            f"{hours:02}:{minutes:02}:{seconds:02}"
            if hours > 0
            else f"{minutes:02}:{seconds:02}"
        )