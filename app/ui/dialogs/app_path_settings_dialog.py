from PySide6.QtWidgets import QDialog, QFileDialog

from app.ui.components import UI_AppSettings

class AppPathSettingsDialog(QDialog, UI_AppSettings):
    def __init__(self, app_configure, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.app_configure = app_configure

        self._setup_signals()
        self.set_settings()

    def _setup_signals(self):
        self.btnPathVideo.clicked.connect(lambda: self.browse_path(self.lePathVideo, "Choose folder for videos"))
        self.btnPathTr.clicked.connect(lambda: self.browse_path(self.lePathTr, "Choose folder for trajectories"))
        self.btnPathHm.clicked.connect(lambda: self.browse_path(self.lePathHm, "Choose folder for heatmaps"))
        self.btnPathDet.clicked.connect(lambda: self.browse_path(self.lePathDet, "Choose folder for detections"))
        self.btnAccept.clicked.connect(self.accept)
        self.btnReject.clicked.connect(self.reject)

        self.lePathDet.setReadOnly(True)
        self.lePathTr.setReadOnly(True)
        self.lePathHm.setReadOnly(True)
        self.lePathVideo.setReadOnly(True)

    def browse_path(self, line_edit, title):
        folder_path = QFileDialog.getExistingDirectory(
            self,
            title,
            line_edit.text() or "",
            QFileDialog.ShowDirsOnly
        )
        if folder_path:
            line_edit.setText(folder_path)

    def get_configure(self):
        return {
            'videos_dir': self.lePathVideo.text(),
            'predictions_dir': self.lePathDet.text(),
            'trajectory_dir': self.lePathTr.text(),
            'heatmap_dir': self.lePathHm.text()
        }
    
    def set_settings(self):

        self.lePathVideo.setText(self.app_configure.videos_dir)
        self.lePathDet.setText(self.app_configure.predictions_dir)
        self.lePathTr.setText(self.app_configure.trajectory_dir)
        self.lePathHm.setText(self.app_configure.heatmap_dir)