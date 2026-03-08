from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal, Slot
from app.ui.components import UI_Load

class LoadedDialog(QDialog):
    start_requested = Signal()

    def __init__(self):
        super().__init__()
        self.ui = UI_Load()
        self.ui.setupUi(self)
        self._elements_settings()

        self.ui.btnStart.clicked.connect(self.btnStart_clicked)

    def _elements_settings(self):
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)

    def btnStart_clicked(self):
        self.ui.btnStart.setEnabled(False)
        self.start_requested.emit()

    @Slot()
    def show_processing(self, msg="Processing..."):
        self.ui.label.setText(msg)

    @Slot()
    def show_success(self, msg="Processing completed"):
        QMessageBox.information(self, "Success", msg)
        self.accept()

    @Slot(int)
    def show_progress(self, value: int):
        self.ui.progressBar.setValue(value)

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)
        self.reject()

        
