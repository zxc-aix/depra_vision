from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Slot

from app.ui.components import UI_OutputResults
from app.analysis.report import ReportTableModel
from app.analysis.report import Exporter

class OutputResultsDialog(QDialog):
    def __init__(self, rows, save_path, parent=None):
        super().__init__(parent)
        self.ui = UI_OutputResults()
        self.ui.setupUi(self)

        self.model = ReportTableModel(rows)
        self.ui.tableView.setModel(self.model)

        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setVisible(False)
        
        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.save_path = save_path
        self._setup_signals()

    def _setup_signals(self):
        self.ui.btnConfirm.clicked.connect(self.on_confirm)
        self.ui.btnCancel.clicked.connect(self.reject)

    def on_confirm(self):
        try:
            rows = self.model.get_rows()
            
            # missing_values = []
            # for i, row in enumerate(rows):
            #     if row["editable"] and (row["value"] is None or str(row["value"]).strip() == ""):
            #         missing_values.append(f"Строка {i+1}: {row['label']}")
            
            # if missing_values:
            #     self.show_warning("Пожалуйста, заполните все поля:\n" + "\n".join(missing_values))
            #     return
            
            df = Exporter.to_dataframe(rows)
            Exporter.to_excel(df, self.save_path)

            self.show_info(f"Report saved to file:\n{self.save_path}")
            
            super().accept()

        except Exception as e:
           self.show_error(f"Failed to save file:\n{str(e)}")

    @Slot(str)
    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    @Slot(str)
    def show_warning(self, msg: str):
        QMessageBox.warning(self, "Warning", msg)

    @Slot(str)
    def show_info(self, msg: str):
        QMessageBox.information(self, "Success", msg)
