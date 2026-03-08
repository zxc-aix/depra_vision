from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QPixmap, QImage
from app.ui.components import UI_Analysis

class AnalysisWidget(QWidget):
    start_analysis_clicked = Signal()
    save_graph_clicked = Signal(QImage)
    data_export_clicked = Signal()
    load_data_clicked = Signal()
    widget_closed = Signal()
    
    def __init__(self,):
        super().__init__()
        self.ui = UI_Analysis()
        self.ui.setupUi(self)
        self.ui.lblTrajectory.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image = None
        self.elemtns = [
            self.ui.btnExportDataMorris, self.ui.chbBuildBr, self.ui.sbThick, self.ui.lblThick, 
            self.ui.sbAngleDist, self.ui.lblAngleDist, self.ui.sbAngleTime, self.ui.lblAngleTime, 
            self.ui.sbAnglePer, self.ui.lblAnglePer, self.ui.sbTimeStart, self.ui.lblTimeStart,
            self.ui.sbTimeEnd, self.ui.lblTimeEnd, self.ui.checkbDiveTraj, self.ui.sbT0, 
            self.ui.lblT0, self.ui.sbT1, self.ui.lblT1, self.ui.sbT2, self.ui.lblT2, self.ui.sbT3, self.ui.lblT3
        ]

        self._setup_signals()
        self._elements_settings()

    def _setup_signals(self,):
        self.ui.btnBuildGraph.clicked.connect(self.start_analysis_clicked.emit)
        self.ui.btnSaveGraph.clicked.connect(self.on_save_clicked)
        self.ui.btnExportDataAll.clicked.connect(self.data_export_clicked.emit)
        self.ui.btnLoadData.clicked.connect(self.load_data_clicked.emit)

    def _elements_settings(self):
        self.ui.lblTrajectory.setAlignment(Qt.AlignmentFlag.AlignCenter)

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)

    def collect_params(self):
        return {
            'ThError': self.ui.dsbThError.value(),
            'speed_threshold': self.ui.dsbSpdThFS.value(),
            'freeze_threshold': self.ui.dsbStopSpdTh.value(),
            'min_freeze_duration': self.ui.dsbStopTimeTh.value(),
            'AngleDist': self.ui.sbAngleDist.value(),
            'AngleTime': self.ui.sbAngleTime.value(),
            'AnglePer': self.ui.sbAnglePer.value(),
            'TimeStart': self.ui.sbTimeStart.value(),
            'TimeEnd': self.ui.sbTimeEnd.value(),
            'Thick': self.ui.sbThick.value(),
            'T0': self.ui.sbT0.value(),
            'T1': self.ui.sbT1.value(),
            'T2': self.ui.sbT2.value(),
            'T3': self.ui.sbT3.value(),
        }
    
    def collect_settings(self):
        return {
            'ShStEn': self.ui.chbShStEn.isChecked(),
            'DiveTraj': self.ui.checkbDiveTraj.isChecked(),
            'ThError': self.ui.dsbThError.value(),
            'AddZones': self.ui.chbAddZones.isChecked(),
            'Scale': self.ui.dsbScale.value(),
            'Wrap': self.ui.chbWrap.isChecked(),
            'BuildBr': self.ui.chbBuildBr.isChecked(),
            'Thick': self.ui.sbThick.value(),
            'WidthTraj': self.ui.dsblWidthTraj.value(),
            'WidthMarkup': self.ui.dsbWidthMarkup.value()
        }
    
    def get_size_label(self):
        return self.ui.lblTrajectory.width(), self.ui.lblTrajectory.height()
    
    def set_image(self, image):
        self.image = image
        pix = QPixmap.fromImage(image)
        self.ui.lblTrajectory.setPixmap(pix)

    def on_save_clicked(self):
        if not self.image:
            self.show_error("First, create a graph!")
            return
        
        self.save_graph_clicked.emit(self.image)

    def enabled_elements(self, is_activate=False):
        for el in self.elemtns:
            el.setEnabled(is_activate)

    def closeEvent(self, event):
        print("AnalysisWidget closed")
        self.widget_closed.emit()
        event.accept()
