class ComboBoxManager:
    def __init__(self, combo_box, default_values=None):
        self.combo_box = combo_box
        self.default_values = default_values or []
        self._setup_combobox()

    def _setup_combobox(self):
        self.combo_box.setEditable(True)
        self.combo_box.lineEdit().setReadOnly(True)
        self.combo_box.addItem("")  
        self.combo_box.addItems(self.default_values)
        self.combo_box.setCurrentIndex(-1)

    def set_placeholder(self, text):
        self.combo_box.lineEdit().setPlaceholderText(text)

    def enable_input(self, enabled=True):
        self.combo_box.setEnabled(enabled)
        if not enabled:
            self.combo_box.lineEdit().setReadOnly(True)

    def connect_signals(self, selection_handler=None, return_handler=None):
        if selection_handler:
            self.combo_box.currentIndexChanged.connect(selection_handler)
        if return_handler:
            self.combo_box.lineEdit().returnPressed.connect(return_handler)

    def handle_selection(self, index):
        if index == 0 and self.combo_box.isEnabled():
            self.combo_box.lineEdit().setReadOnly(False)
            self.combo_box.lineEdit().setFocus()
        else:
            self.combo_box.lineEdit().setReadOnly(True)

    def add_custom_item(self, text):
        text = text.strip()
        if text and self.combo_box.findText(text) == -1:
            self.combo_box.insertItem(1, text)
            self.combo_box.setCurrentText(text)
            return text
        return None

    def update_items(self, new_items, keep_custom=True):
        current_text = self.combo_box.currentText()
        is_custom = current_text and current_text not in self.default_values + new_items

        self.combo_box.clear()
        self.combo_box.addItem("")
        self.combo_box.addItems(new_items)

        if keep_custom and is_custom:
            self.combo_box.insertItem(1, current_text)
            self.combo_box.setCurrentText(current_text)
        else:
            self.combo_box.setCurrentIndex(-1)