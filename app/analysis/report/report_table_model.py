from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QBrush

class ReportTableModel(QAbstractTableModel):
    HEADERS = ["Parameter", "Type", "Value"]

    def __init__(self, rows: list[dict]):
        super().__init__()
        self._rows = rows

    def rowCount(self, parent=QModelIndex()):
        return len(self._rows)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.HEADERS[section]
        return None

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row_idx = index.row()
        col = index.column()

        if row_idx < 0 or row_idx >= len(self._rows):
            return None

        row = self._rows[row_idx]

        if role == Qt.DisplayRole:
            if col == 0:
                return row.get("label", "")
            elif col == 1:
                return "manual" if row.get("editable") else "auto"
            elif col == 2:
                value = row.get("value")
                return "" if value is None else str(value)
            return None

        if role == Qt.BackgroundRole:
            if col == 1 and row.get("editable"):
                return QBrush(Qt.darkBlue)
            if col == 2 and not row.get("editable"):
                return QBrush(Qt.gray)
            return None

        if role == Qt.TextAlignmentRole and col in (1, 2):
            return Qt.AlignCenter

        return None

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags

        row_idx = index.row()
        if row_idx < 0 or row_idx >= len(self._rows):
            return Qt.NoItemFlags

        flags = super().flags(index)

        if index.column() == 2 and self._rows[row_idx].get("editable"):
            return flags | Qt.ItemIsEditable

        return flags & ~Qt.ItemIsEditable


    def setData(self, index: QModelIndex, value, role=Qt.EditRole):
        if role != Qt.EditRole or not index.isValid():
            return False

        row_idx = index.row()
        if row_idx < 0 or row_idx >= len(self._rows):
            return False

        if index.column() == 2:
            cleaned_value = value.strip() if value else None
            self._rows[row_idx]["value"] = cleaned_value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True

        return False


    def get_rows(self) -> list[dict]:
        return [row.copy() for row in self._rows]
