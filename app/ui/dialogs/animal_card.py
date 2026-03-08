from PySide6.QtWidgets import QDialog, QMessageBox
from app.ui.components import UI_AnimalCard
from app.utils.combobox_manager import ComboBoxManager



class AnimalCardDialog(QDialog):
    def __init__(self, animal_configure, parent=None):
        super().__init__(parent)
        self.ui = UI_AnimalCard()
        self.ui.setupUi(self)

        self.animal_configure = animal_configure # class AnimalConfig

        self._init_variables()
        self._init_base_values()
        self._setup_signals()


    def _init_variables(self):

        self.COLOR_VALUES = ["Albino", "Black", "Agouti", "Hooded", "Hairless", "Piebald", "Spotted", "Other"]

        self.TYPE_VALUES = [
            "Mus musculus", 
            "Rattus norvegicus domestica"
        ]

        self.MODEL_VALUES = [
            "Wild type (WT)", 
            "Transgenic line (TG)"
        ]

        self.MOUSE_LINE_VALUES = [
            "С57Bl/6", "BALB/c", "DBA/2J", "ICR (CD-1)", 
            "СВА", "HSP70in", "HSP70ex", "APP"
        ]

        self.RAT_LINE_VALUES = [
            "Wistar", "Wistar-Kyoto (WRY)", "Sprague Dawley", "Long–Evans"
        ]

        self.SUBLINE_VALUES = ["С57Bl/6J", "С57Bl/6N", "C57BL/6C"]

        self.line_manager = ComboBoxManager(self.ui.cbLine)
        self.subline_manager = ComboBoxManager(self.ui.cbSubLine, self.SUBLINE_VALUES)

        self.save_default = False

    def _init_base_values(self):
        # Количество объектов
        self.ui.spinbCountAnimal.setValue(1)
        self.ui.spinbCountAnimal.setMinimum(0)
        self.ui.spinbCountAnimal.setMaximum(10)
        self.ui.spinbCountAnimal.setSingleStep(1)

        # Окрас животного
        self.ui.cbColor.addItems(self.COLOR_VALUES)
        self.ui.cbColor.setCurrentIndex(-1)

        # Вид животного
        self.ui.cbType.addItems(self.TYPE_VALUES)
        self.ui.cbType.setCurrentIndex(-1)

        # Модельное животное
        self.ui.cbModel.addItems(self.MODEL_VALUES)
        self.ui.cbModel.setCurrentIndex(-1)

        # Настройка менеджеров ComboBox
        self.line_manager.set_placeholder('Select "Model animal"')
        self.line_manager.enable_input(False)
        self.subline_manager.enable_input(False)

    def _setup_signals(self):
        self.ui.btnAccept.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.btnReset.clicked.connect(self.reset_form)

        self.ui.chbDefault.stateChanged.connect(self.on_use_defaults_changed)
        self.ui.checkbSave.stateChanged.connect(lambda state: setattr(self, 'save_default', bool(state)))

        self.ui.cbType.currentTextChanged.connect(self._update_line_combobox)
        self.ui.cbModel.currentTextChanged.connect(self.on_change_model)
        self.ui.cbLine.currentTextChanged.connect(self.on_change_line)

        # Подключение сигналов для менеджера линии
        self.line_manager.connect_signals(
            selection_handler=self._handle_line_selection,
            return_handler=self._add_custom_line
        )
        self.subline_manager.connect_signals(
            selection_handler=self._handle_subline_selection,
            return_handler=self._add_custom_subline
        )

    def _handle_line_selection(self, index):
        """Обработчик выбора элемента в cbLine"""
        self.line_manager.handle_selection(index)

    def _add_custom_line(self):
        """Обработчик добавления пользовательской cbLine"""
        self.line_manager.add_custom_item(self.ui.cbLine.currentText())

    def _handle_subline_selection(self, index):
        """Обработчик выбора элемента в cbSubLine"""
        self.subline_manager.handle_selection(index)

    def _add_custom_subline(self):
        """Обработчик добавления пользовательской SubLine"""
        self.subline_manager.add_custom_item(self.ui.cbSubLine.currentText())

    def on_change_model(self, text):
        
        if text:  
            self.line_manager.enable_input()
            self._update_line_combobox()
        else:
            self.line_manager.enable_input(False)
            self.line_manager.set_placeholder('Выберите "Модельное животное"')
            
    def _update_line_combobox(self, text=None):
        if not self.ui.cbModel.currentText():
            return
            
        if self.ui.cbType.currentText() == 'Mus musculus': 
            self.line_manager.update_items(self.MOUSE_LINE_VALUES)
        elif self.ui.cbType.currentText() == 'Rattus norvegicus domestica':
            self.line_manager.update_items(self.RAT_LINE_VALUES)
        
        lbl_text = "Animal line"
        if self.ui.cbModel.currentText() == "Wild type (WT)":
            lbl_text = "Genetic background"
        
        self.ui.lblLine.setText(lbl_text)
        self.line_manager.set_placeholder("Select or enter")

    def on_change_line(self, text):

        if text == "С57Bl/6":
            self.subline_manager.enable_input()
            self.subline_manager.set_placeholder("Select or enter")
            self.ui.lblSubLine.setText("Animal subline")
        else:
            self.subline_manager.enable_input(False)

    def get_configuration(self):
        return self.animal_configure

    def on_use_defaults_changed(self):
        if  self.ui.chbDefault.isChecked():
            self._set_default_values()
        else:
            self._clear_form()

    def _set_default_values(self):
        if 'count_animal' in self.animal_configure:
            self.ui.spinbCountAnimal.setValue(self.animal_configure['count_animal'])
        
        self.ui.leId.setText(self.animal_configure.id)
        self.ui.leAge.setText(self.animal_configure.age)
        self.ui.leWeight.setText(self.animal_configure.weight)
        
        self._set_combobox_default(self.ui.cbColor, 'color')
        self._set_combobox_default(self.ui.cbType, 'type')
        self._set_combobox_default(self.ui.cbModel, 'model')
        
        self._update_line_combobox()

    def _set_combobox_default(self, combobox, key):
        if key in self.animal_configure.dict():
            value = self.animal_configure.dict()[key] 
            index = combobox.findText(value)
            if index >= 0:
                combobox.setCurrentIndex(index)
            else:
                combobox.setCurrentText(value)

    def _clear_form(self):
        """Очищает форму (аналогично reset_form)"""
        self.ui.spinbCountAnimal.setValue(1)
        self.ui.leId.clear()
        self.ui.leAge.clear()
        self.ui.leWeight.clear()
        self.ui.cbColor.setCurrentIndex(-1)
        self.ui.cbType.setCurrentIndex(-1)
        self.ui.cbModel.setCurrentIndex(-1)

        self.ui.cbLine.setCurrentIndex(-1)
        self.line_manager.enable_input(False)
        self.line_manager.update_items([])  
        self.line_manager.set_placeholder('Choose "Model animal"')

        self.subline_manager.enable_input(False)
        self.subline_manager.update_items([]) 
        self.ui.cbSubLine.setCurrentIndex(-1)
        
        self.ui.lblLine.setText("-")
        self.ui.lblSubLine.setText("-")

    def reset_form(self):
        self._clear_form()

    def _collect_config(self) -> dict:
        return {
            "count_animal": self.ui.spinbCountAnimal.value(),
            "id": self.ui.leId.text(),
            "age": self.ui.leAge.text(),
            "weight": self.ui.leWeight.text(),
            "color": self.ui.cbColor.currentText(),
            "type": self.ui.cbType.currentText(),
            "model": self.ui.cbModel.currentText(),
            "line": self.ui.cbLine.currentText(),
            "subline": self.ui.cbSubLine.currentText(),
        }
    
    def accept(self):
        config = self._collect_config()

        if not config.get('type'):
            QMessageBox.warning(self, "Error", "Please select an animal type!")
            return
        
        message = ""
        for key, value in config.items():
            if value:
                readable_key = {
                    'count_animal': 'Count of animals',
                    'id': 'ID',
                    'age': 'Age',
                    'weight': 'Weight',
                    'color': 'Color',
                    'type': 'Animal type',
                    'model': 'Model animal',
                    'line': self.ui.lblLine.text(),
                    'subline': 'Subline'
                }.get(key, key)

                message += f"{readable_key}: {value}\n"

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Check parameters")
        msg_box.setText("You have selected the following parameters:")
        msg_box.setInformativeText(message)
        
        msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Save)
        
        self.animal_configure = self.animal_configure.model_copy(update=config)
        
 
        result = msg_box.exec()
        if result == QMessageBox.Save:
            super().accept()
