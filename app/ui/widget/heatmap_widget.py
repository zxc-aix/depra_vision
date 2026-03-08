from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog, QTreeView, QListView, QColorDialog
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon, QColor, QPixmap, QImage
from pathlib import Path

from app.ui.components import UI_HeatMap
from app.utils import ColormapManager

class HeatmapWidget(QWidget):
    add_folder_clicked = Signal(list)
    remove_folder_clicked = Signal()
    clear_folders_clicked = Signal()
    build_graph_clicked = Signal()
    save_image_clicked = Signal(QImage)
    widget_closed = Signal()

    def __init__(self):
        super().__init__()
        self.ui = UI_HeatMap()
        self.ui.setupUi(self)

        self.model = QStandardItemModel()
        self.image = None
        self.directory = ""
        self.colormap_manager = ColormapManager()
        self.rgb_values = (0, 0, 255)

        self._setup_signals()
        self._elements_settings()
        self._update_colormap_combobox()
        
    def _setup_signals(self):
        self.ui.btnAddFolder.clicked.connect(self.select_folders)
        self.ui.btnRemove.clicked.connect(self.remove_folder_clicked)
        self.ui.btnClearFolder.clicked.connect(self.clear_folders_clicked)
        self.ui.btnBuildGraph.clicked.connect(self.build_graph_clicked)
        self.ui.btnSaveImage.clicked.connect(self.on_save_clicked)
        
        self.folders_list = self.ui.lvFolderList
        self.folders_list.setViewMode(QListView.ListMode)
        self.folders_list.setFlow(QListView.TopToBottom)
        self.folders_list.setWrapping(False)
        self.folders_list.setVerticalScrollMode(QListView.ScrollPerPixel)
        self.folders_list.setModel(self.model)

        self.folder_dialog = QFileDialog(self)
        self.folder_dialog.setWindowTitle("Choose folders")  
        self.folder_dialog.setFileMode(QFileDialog.FileMode.Directory)
        self.folder_dialog.setOption(QFileDialog.Option.DontUseNativeDialog, True)
        self.folder_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        
        tree_view = self.folder_dialog.findChild(QTreeView, "treeView")
        if tree_view:
            tree_view.setSelectionMode(tree_view.SelectionMode.ExtendedSelection)

    def _elements_settings(self):
        self.ui.lblImage.setAlignment(Qt.AlignCenter)
        
        self.ui.dsbBoxScale.setRange(0.1, 5)
        self.ui.dsbBoxScale.setSingleStep(0.1)
        self.ui.dsbBoxScale.setDecimals(1)

        self.ui.sbGausSigma.setRange(0, 201)

        self.ui.dsbZoom.setRange(0.1, 4)
        self.ui.dsbZoom.setSingleStep(0.01)

        self.ui.dsbGamma.setRange(0.01, 4)
        self.ui.dsbGamma.setSingleStep(0.01)

        self.ui.dsbAlpha.setRange(0.01, 4)
        self.ui.dsbAlpha.setSingleStep(0.01)

        self.ui.dsbContrast.setRange(0.01, 4)
        self.ui.dsbContrast.setSingleStep(0.01)

        self.ui.frameColor.setLineWidth(2)
        self.ui.frameColor.setStyleSheet(f"border: 1px solid black; background-color: rgb{self.rgb_values};")
        self.ui.frameColor.setCursor(Qt.PointingHandCursor)
        self.ui.frameColor.mousePressEvent = self.choose_color

    def _update_colormap_combobox(self):
        self.ui.cbColorGamma.clear()
        available_maps = self.colormap_manager.get_available_colormaps()
        
        display_names = {
            'jet': 'Jet (по умолчанию)',
            'viridis': 'Viridis',
            'plasma': 'Plasma',
            'inferno': 'Inferno',
            'magma': 'Magma',
            'turbo': 'Turbo',
            'custom_jet': 'Custom Jet',
            'hot': 'Hot',
            'cool': 'Cool',
            'spring': 'Spring',
            'autumn': 'Autumn',
            'winter': 'Winter',
            'bone': 'Bone',
            'rainbow': 'Rainbow',
            'ocean': 'Ocean',
            'summer': 'Summer',
            'pink': 'Pink',
            'hsv': 'HSV',
            'parula': 'Parula',
        }
        
        for map_name in available_maps:
            display_name = display_names.get(map_name, map_name.title())
            self.ui.cbColorGamma.addItem(display_name, map_name)
        
        # Устанавливаем jet по умолчанию
        index = self.ui.cbColorGamma.findData('jet')
        if index >= 0:
            self.ui.cbColorGamma.setCurrentIndex(index)
        
    def setup_dialog_dir(self, dir):
        self.directory = dir

    def select_folders(self):
        self.folder_dialog.setDirectory(self.directory)
        if self.folder_dialog.exec():
            folders = self.folder_dialog.selectedFiles()
            self.add_folder_clicked.emit(folders)
        else:
            self.add_folder_clicked.emit([])

    def add_folder_in_list(self, folder_path):
        folder_path = str(Path(folder_path).resolve())
        item = QStandardItem(Path(folder_path).name)
        item.setIcon(QIcon.fromTheme("folder"))
        item.setToolTip(folder_path)
        self.model.appendRow(item)

        try:
            self.update_counter()
            return True
        except Exception as e:
            self.model.removeRow(self.model.rowCount()-1)
            self.show_error(f"Error adding folder:\n{e}")
            return False
        
    def remove_last_folder(self):
        self.model.removeRow(self.model.rowCount() - 1)
        self.update_counter()

    def clear_folders(self):
        self.image = None
        self.model.clear()
        self.update_counter()
        self.show_info("Cleared folder list")

    def update_counter(self):
        count = self.model.rowCount()
        self.ui.lblInfo.setText(f"Folders selected: {count}")
    
    def on_save_clicked(self):
        if not self.image:
            self.show_error("First, create a graph!")
            return
        
        self.save_image_clicked.emit(self.image)

    def collect_settings(self):
        current_map_name = self.ui.cbColorGamma.currentData()
        
        return {
            'gaussian_kernel': 101,
            'gaussian_sigma': int(self.ui.sbGausSigma.value()),
            'bilateral_d': 15,
            'bilateral_color_sigma': 80,
            'bilateral_space_sigma': 80,
            'upscale_factor': 2,
            'box_scale': float(self.ui.dsbBoxScale.value()),
            'overlaps': self.ui.chbOverlaps.isChecked(),
            'markup': self.ui.chbMarkup.isChecked(),
            'colormap_name': current_map_name,  # ← используем только название
            'zoom': self.ui.dsbZoom.value(),
            'platform_allowed': self.ui.chbAddPlatform.isChecked(),
            'filter': self.ui.cbFillter.currentIndex(),
            'gamma': self.ui.dsbGamma.value(), 
            'alpha': self.ui.dsbAlpha.value(),
            'contrast': self.ui.dsbContrast.value(),
            'is_add_colorbar': self.ui.cbAddColorbar.isChecked(),
            'interpolate': self.ui.cbInterpolate.isChecked(),
            'rgb_values': self.rgb_values
        }

    def choose_color(self, event):
        if event.button() == Qt.LeftButton:
            current_color = QColor(*self.rgb_values)
            color = QColorDialog.getColor(current_color, None, "Choose color for zone")
            
            if color.isValid():
                self.rgb_values = (color.red(), color.green(), color.blue())
                self.ui.frameColor.setStyleSheet(f"border: 1px solid black; background-color: rgb{self.rgb_values};")

    def set_image(self, image):
        self.image = image
        # pix = QPixmap.fromImage(image)
        scaled = QPixmap.fromImage(image).scaled(
            self.ui.lblImage.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.ui.lblImage.setPixmap(scaled)
        # self.ui.lblImage.setScaledContents(True)

    def clear_image(self):
        self.image = ""
        self.ui.lblImage.clear()

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_warning(self, msg: str):
        QMessageBox.warning(self, "Warning", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)

    def closeEvent(self, event):
        print("HeatmapWidget closed")
        self.widget_closed.emit()
        event.accept()
