from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QCompleter
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QDoubleValidator
from core.validators import ValidatorManager
from core.validators import NotEmptyValidator, SelectionValidator
from core.data_manager import DataManager
from ui.widgets.form_archive_ui import Ui_form_archhive
from core import data_manager
from helpers import generators
import os, shutil
from datetime import datetime
from helpers.config import archive_dir


class FormArchive(QDialog):
    def __init__(self):
        super().__init__()
        self.data_manager = data_manager
        self.ui = Ui_form_archhive()
        self.ui.setupUi(self)
        self.validator_manager = ValidatorManager(self.ui)
        self.codes = [d.code for d in self.data_manager.get_dossiers_not_archived()]
        self.ui.cb_num_doc.addItems(self.codes)
        completer = QCompleter(self.codes, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.cb_num_doc.setCompleter(completer)
        self.list_box = [d.name for d in self.data_manager.get_all_archive_boxes()]
        self.ui.cb_num_box.addItems(self.list_box)
        completer_box = QCompleter(self.list_box, self)
        self.ui.cb_num_box.setCompleter(completer_box) 
        self.ui.date_accus.setDate(QDate.currentDate())
        self.ui.pb_upload.clicked.connect(self.upload_file)
        hon_validator = QDoubleValidator(bottom=0.0, top=100000000, decimals=2)  # Limite entre 0.0 et 100.0 avec 2 décimales
        hon_validator.setNotation(QDoubleValidator.StandardNotation)
        self.ui.le_honoraires.setValidator(hon_validator)
        self.validator_manager.add_validation_rule("cb_num_doc", "error_num_doc", [NotEmptyValidator(), SelectionValidator()])
        self.validator_manager.add_validation_rule("cb_num_box", "error_num_box", [NotEmptyValidator(), SelectionValidator()])
        self.validator_manager.add_validation_rule("le_num_archive", "error_num_archive", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("le_file_name", "error_file_name", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("le_honoraires", "error_honoraires", [NotEmptyValidator()])
        self.setWindowTitle("إضافة أرشيف جديد")
        self.ui.cb_num_doc.currentTextChanged.connect(self.active_load_data)
        
        self.validator_manager.validationStateChanged.connect(lambda valid: self.ui.pb_save.setEnabled(valid))
        self.ui.pb_save.clicked.connect(self.save)
        self.ui.pb_cancel.clicked.connect(self.reject)
    def active_load_data(self, selected):
        if selected and selected in self.codes:
            self.dossier = self.data_manager.get_dossier_by_code(selected)
            self.ui.lbl_demandeur.setText(self.dossier.demandeur_nom)
            self.ui.lbl_defendeur.setText(self.dossier.defendeur_nom)
            self.ui.gb_archive.setEnabled(True)
        else:
            self.ui.gb_archive.setEnabled(False)
            self.ui.lbl_demandeur.setText("")
            self.ui.lbl_defendeur.setText("")
    def upload_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "اختر الملف", "", "PDF Files (*.pdf)")
        if self.file_name:
            self.ui.le_file_name.setText(self.file_name) 
    def save(self):
        original_path = os.path.basename(self.file_name)
        
        unique_file_name = generators.generate_unique_filename(original_path)
        destination_path = os.path.join(archive_dir, unique_file_name)
        
        try:
            shutil.copy(self.file_name,destination_path)
            
        except Exception as e:
            QMessageBox(self,e)

        code = self.ui.cb_num_doc.currentText()
        dossier  = self.data_manager.get_dossier_code(code)
        dossier.path_file = unique_file_name
        dossier.archive_box_id = self.data_manager.get_archive_box_by_name(self.ui.cb_num_box.currentText()).id
        
        dossier.date_accus = datetime.strptime(self.ui.date_accus.text(), '%Y/%m/%d')
        dossier.archive_status = True
        dossier.valid_status = True
        dossier.num_archive = self.ui.le_num_archive.text()
        dossier.honoraires = float(self.ui.le_honoraires.text().replace(" ", "")) if self.ui.le_honoraires.text() else None
        dossier.uplaod_at = datetime.now()      
        
        self.data_manager.update_dossier(dossier)
        self.accept()