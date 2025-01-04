from PySide6.QtWidgets import QDialog, QCompleter, QMessageBox
from PySide6.QtCore import QDate, QTime, Qt, QDateTime
from ui.widgets.form_act_ui import Ui_form_act
from models.models import Dossier, Client, Demandeur, Defendeur, RapportType, FieldValue, Document, Category, Tribunal, Council, Room, Section, GenreEnum
from core import data_manager, state_manager
from core.validators import ValidatorManager, NotEmptyValidator,  DateValidator, SelectionValidator
from controllers.widgets.FormClient import FormClient
from helpers.logger import logger

class FormAct(QDialog):
    def __init__(self, dossier: Dossier=None):
        super().__init__()
        self.ui = Ui_form_act()
        self.ui.setupUi(self)
        self.data_manager = data_manager
        self.state_manager = state_manager
        
        # Charger les données initiales dans le state_manager
        self.data_manager._update_clients_state()
        self.data_manager._update_demandeurs_state()
        self.data_manager._update_defendeurs_state()
        self.data_manager._update_councils_state()
        self.data_manager._update_rooms_state()
        self.data_manager._update_sections_state()
        self.data_manager._update_tribunals_state()
        
        self.validator_manager = ValidatorManager(self.ui)
        self.init_validation()
        
        self.setWindowTitle("إضافة محضر جديد")
        self.council_visible(False)

        self.dossier: Dossier = None    
        self.client : Client = None
        self.demandeur: Demandeur = None
        self.defendeur: Defendeur = None
       
        self.tribunal_field = FieldValue()
        self.council_field  = FieldValue()
        self.tribunal_registary_field  = FieldValue()
        self.council_registary_field = FieldValue()
        self.room_field  = FieldValue()
        self.section_field = FieldValue ()
        self.hall_field  = FieldValue()
        self.date_registary_field  = FieldValue()
        self.date_audience_field  = FieldValue()
        self.hour_audience_field  = FieldValue()
        self.case_number_field  = FieldValue()
        
      
        self.ui.pb_add_client.clicked.connect(self.add_client)
        self.ui.cb_client.currentTextChanged.connect(self.on_client_changed)
        self.ui.chb_same.checkStateChanged.connect(self.set_same)

        self.ui.cb_demandeur.currentTextChanged.connect(self.on_demandeur_changed)
        self.ui.cb_defendeur.currentTextChanged.connect(self.on_defendeur_changed)
        self.ui.cb_tribunal.currentTextChanged.connect(self.on_tribunal_changed)
        self.ui.cb_tribunal_registary.currentTextChanged.connect(self.on_tribunal_registary_changed)
        self.ui.cb_council.currentTextChanged.connect(self.on_council_changed)
        self.ui.cb_council_registary.currentTextChanged.connect(self.on_council_registary_changed)
        self.ui.cb_room.currentTextChanged.connect(self.on_room_changed)
        self.ui.cb_section.currentTextChanged.connect(self.on_section_changed) 
        self.ui.tb_save.setDisabled(True)
        self.validator_manager.validationStateChanged.connect(self.on_validation_state_changed)
        self.ui.tb_save.clicked.connect(self.save_dossier)
        self.ui.tb_close.clicked.connect(self.close)
        self.ui.cb_type_rapport.addItems( [item.value for item in RapportType])
        self.ui.cb_type_rapport.currentIndexChanged.connect(self.on_type_rapport_changed)
        self.ui.cb_type_rapport.setCurrentIndex(0)

        

        self.init_forms()
        if dossier:
            self.dossier = self.data_manager.get_dossier_by_id(dossier.id)
            self.set_form_dossier(dossier)

    def init_forms(self):
        """Initialise tous les formulaires avec les données du state_manager"""
        self.load_data_client(self.state_manager.get_state("clients", []))
        self.load_data_demandeur(self.state_manager.get_state("demandeurs", []))
        self.load_data_defendeur(self.state_manager.get_state("defendeurs", []))
        self.load_data_council(self.state_manager.get_state("councils", []))
        self.load_data_room(self.state_manager.get_state("rooms", []))
        self.load_data_section(self.state_manager.get_state("sections", []))
        self.load_data_tribunal(self.state_manager.get_state("tribunals", []))
        
        # Initialiser les dates et l'heure
        self.ui.de_audience.setDate(QDate.currentDate())
        self.ui.de_registary.setDate(QDate.currentDate())
        self.ui.te_audience.setTime(QDateTime.currentDateTime().time())
    
    def init_validation(self):
        self.validator_manager.add_validation_rule("cb_client", "error_client", [NotEmptyValidator(), SelectionValidator()])
        self.validator_manager.add_validation_rule("cb_demandeur", "error_demandeur", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_defendeur", "error_defendeur", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("le_address_demandeur", "error_adr_demandeur", [ NotEmptyValidator()])
        self.validator_manager.add_validation_rule("le_address_defendeur", "error_adr_defendeur", [ NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_council", "error_council", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_council_registary", "error_council_reg", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_tribunal", "error_tribunal", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_tribunal_registary", "error_tribunal_reg", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_section", "error_section", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("cb_room", "error_room", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("te_audience", "error_hour", [ NotEmptyValidator()])
        self.validator_manager.add_validation_rule("de_registary", "error_date_reg", [NotEmptyValidator(), DateValidator()])
        self.validator_manager.add_validation_rule("de_audience", "error_date_audience", [NotEmptyValidator(), DateValidator()])
        self.validator_manager.add_validation_rule("le_hall", "error_hall", [NotEmptyValidator()])
        self.validator_manager.add_validation_rule("le_case", "error_case", [NotEmptyValidator()])
        
       # Validation en temps réel
       

    def on_validation_state_changed(self, is_valid: bool):
        """Gère le changement d'état de la validation"""
        self.ui.tb_save.setEnabled(is_valid)    
        
    def  set_form_dossier(self, dossier):
        self.client = self.data_manager.get_client_by_id(dossier.client_id)
        self.demandeur = self.data_manager.get_demandeur_by_id(dossier.demandeur_id)
        self.defendeur = self.data_manager.get_defendeur_by_id(dossier.defendeur_id)
        self.document : Document = self.data_manager.get_document_by_id(dossier.document_id)
        self.fields = self.data_manager.get_fields_by_document_id_dossier_id(self.document.id, self.dossier.id)
        category = self.data_manager.get_category_by_id(self.document.category_id)
        self.ui.cb_type_rapport.setCurrentText(category.nom)

        self.ui.cb_client.setCurrentText(self.client.nom)
        self.ui.cb_demandeur.setCurrentText(self.demandeur.nom)
        self.ui.cb_defendeur.setCurrentText(self.defendeur.nom)
        self.ui.chb_same.setChecked(True) if self.client.nom == self.demandeur.nom and self.client.adresse == self.demandeur.adresse else self.ui.chb_same.setChecked(False)
        
        list_fields = self.data_manager.get_fields_by_document_id_dossier_id(self.document.id, self.dossier.id)

        field_dict = {field.field_name: field for field in list_fields}
        
        if category.nom == "المحكمة":
            self.ui.cb_tribunal.setCurrentText(field_dict.get("tribunal", "").field_value)
            self.ui.cb_tribunal_registary.setCurrentText(field_dict.get("tribunal_registary", "").field_value)
            self.ui.cb_section.setCurrentText(field_dict.get("section", "").field_value)
        else:
            self.ui.cb_council.setCurrentText(field_dict.get("council", "").field_value)
            self.ui.cb_room.setCurrentText(field_dict.get("room", "").field_value)
            self.ui.cb_council_registary.setCurrentText(field_dict.get("council_registary", "").field_value)

        self.ui.de_registary.setDate(QDate.fromString(field_dict.get("date_registary", "").field_value, "yyyy-MM-dd") if field_dict.get("date_registary", "") else "")
        self.ui.de_audience.setDate(QDate.fromString(field_dict.get("date_audience", "").field_value, "yyyy-MM-dd") if field_dict.get("date_audience", "") else "")
        self.ui.te_audience.setTime(QTime.fromString(field_dict.get("hour_audience", "").field_value, "hh:mm") if field_dict.get("hour_audience", "") else "")
        self.ui.le_case.setText(field_dict.get("case_number", "").field_value)
        self.ui.le_hall.setText(field_dict.get("hall", "").field_value)
       
    def on_type_rapport_changed(self, index):
        if index == 0:        
            self.tribunal_visible(True)
            self.council_visible(False)
        else:
            self.tribunal_visible(False)
            self.council_visible(True)
        # refraichir la validation
        self.validator_manager.validate_all()

    def tribunal_visible(self, visible):
        self.load_data_tribunal(self.state_manager.get_state("tribunaux", []))
        self.load_data_section(self.state_manager.get_state("sections", []))
        
        self.ui.gb_tribunal.setVisible(visible)
        self.ui.lbl_tribunal_reg.setVisible(visible)
        self.ui.cb_tribunal_registary.setVisible(visible)
        self.ui.error_tribunal_reg.setVisible(visible)
      
        if visible: 
            self.validator_manager.add_validation_rule("cb_tribunal", "error_tribunal", [NotEmptyValidator()])
            self.validator_manager.add_validation_rule("cb_tribunal_registary", "error_tribunal_reg", [NotEmptyValidator()])
            self.validator_manager.add_validation_rule("cb_section", "error_section", [NotEmptyValidator()])
            
        else:
            self.validator_manager.remove_validation_rule("cb_tribunal")
            self.validator_manager.remove_validation_rule("cb_tribunal_registary")
            self.validator_manager.remove_validation_rule("cb_section")

    def council_visible(self, visible):
        self.load_data_council(self.state_manager.get_state("councils", []))
        self.load_data_room(self.state_manager.get_state("rooms", []))
      
    
        self.ui.gb_council.setVisible(visible)
        self.ui.cb_council_registary.setVisible(visible)
        self.ui.lbl_council_reg.setVisible(visible)
        self.ui.error_council_reg.setVisible(visible)
        
        if visible: 
            self.validator_manager.add_validation_rule("cb_council", "error_council", [NotEmptyValidator()])
            self.validator_manager.add_validation_rule("cb_council_registary", "error_council_reg", [NotEmptyValidator()])
            self.validator_manager.add_validation_rule("cb_room", "error_room", [NotEmptyValidator()])
            
        else:
            self.validator_manager.remove_validation_rule("cb_council")
            self.validator_manager.remove_validation_rule("cb_council_registary")
            self.validator_manager.remove_validation_rule("cb_room")
        

    def load_data_client(self, clients):
        self.ui.cb_client.clear()
        self.list_clients = [client.nom for client in clients]
        self.completer = QCompleter(self.list_clients, self)
        self.ui.cb_client.addItems(self.list_clients)
        self.ui.cb_client.setCompleter(self.completer)

    def load_data_tribunal(self, tribunals):

        self.list_tribunal = [tribunal.nom for tribunal in tribunals]  
        self.ui.cb_tribunal.clear()
        self.ui.cb_tribunal_registary.clear() 
        self.tribunal_completer = QCompleter(self.list_tribunal, self)
        self.tribunal_reg_completer = QCompleter(self.list_tribunal, self)
        self.ui.cb_tribunal.addItems(self.list_tribunal)
        self.ui.cb_tribunal.setCompleter(self.tribunal_completer)

        self.ui.cb_tribunal_registary.addItems(self.list_tribunal)
        self.ui.cb_tribunal_registary.setCompleter(self.tribunal_reg_completer)
        

    def load_data_council(self, councils):
        #self.list_council = [council.nom for council in self.data_manager.get_all_councils()]
        self.list_council = [council.nom for council in councils]
        self.ui.cb_council.clear()
        self.ui.cb_council_registary.clear()  
        self.council_completer = QCompleter(self.list_council, self)
        self.council_reg_completer = QCompleter(self.list_council, self)
        self.ui.cb_council.addItems(self.list_council)
        self.ui.cb_council.setCompleter(self.council_completer)
        self.ui.cb_council_registary.addItems(self.list_council)
        self.ui.cb_council_registary.setCompleter(self.council_reg_completer)
        

    def load_data_room(self, rooms):
        self.ui.cb_room.clear()        
        self.list_rooms = [room.nom for room in rooms]
        self.room_completer = QCompleter(self.list_rooms, self)
        self.ui.cb_room.addItems(self.list_rooms)
        self.ui.cb_room.setCompleter(self.room_completer)

    def load_data_section(self, sections):
        self.ui.cb_section.clear()        
        self.list_sections = [section.nom for section in sections]
        self.section_completer = QCompleter(self.list_sections, self)
        self.ui.cb_section.addItems(self.list_sections)
        self.ui.cb_section.setCompleter(self.section_completer) 

    def load_data_demandeur(self, demandeurs):
        """Load demandeur data from state."""
        self.ui.cb_demandeur.clear()
        self.list_demandeurs = [demandeur.nom for demandeur in demandeurs]
        self.demandeur_completer = QCompleter(self.list_demandeurs, self)
        self.demandeur_completer.setFilterMode(Qt.MatchContains)
        self.ui.cb_demandeur.addItems(self.list_demandeurs)
        self.ui.cb_demandeur.setCompleter(self.demandeur_completer)

    def load_data_defendeur(self, defendeurs):
        self.ui.cb_defendeur.clear()
        self.list_defendeurs = [defendeur.nom for defendeur in defendeurs]
        self.defendeur_completer = QCompleter(self.list_defendeurs, self)
        self.defendeur_completer.setFilterMode(Qt.MatchContains)
        self.ui.cb_defendeur.addItems(self.list_defendeurs)
        self.ui.cb_defendeur.setCompleter(self.defendeur_completer)
        
    def add_client(self):        
        dlg = FormClient()
        dlg.exec()
        client_data = dlg.get_client_data()
        if client_data:
            self.load_data_client(self.state_manager.get_state("clients", []))
            self.ui.cb_client.setCurrentIndex(self.list_clients.index(client_data.nom))
    def set_same(self):
        if self.ui.chb_same.isChecked():
            self.ui.cb_demandeur.setCurrentText(self.client.nom)
            self.ui.le_address_demandeur.setText(self.client.adresse)
            self.ui.gb_demandeur_info.setDisabled(True)
        else:
            self.ui.gb_demandeur_info.setEnabled(True)
            self.load_data_demandeur(self.state_manager.get_state("demandeurs", []))
            self.ui.le_address_demandeur.setText("")
            


    def on_client_changed(self, noms):
        self.client : Client = self.data_manager.get_client_by_name(noms)
        if self.client:
            if self.ui.chb_same.isChecked():
                self.ui.cb_demandeur.setCurrentText(self.client.nom)
                self.ui.le_address_demandeur.setText(self.client.adresse)
            
    def on_demandeur_changed(self, noms):
        demandeur : Demandeur = self.data_manager.get_demandeur_by_name(noms)
        if demandeur:
            self.ui.le_address_demandeur.setText(demandeur.adresse)
    def on_defendeur_changed(self, noms):
        defendeur = self.data_manager.get_defendeur_by_name(noms)
        if defendeur:
            self.ui.le_address_defendeur.setText(defendeur.adresse)

    def on_tribunal_changed(self, nom):
        tribunal = self.data_manager.get_tribunal_by_name(nom)
        if tribunal:
            self.ui.cb_tribunal.setCurrentIndex(self.list_tribunal.index(tribunal.nom))
    
    def on_tribunal_registary_changed(self, nom):
        tribunal = self.data_manager.get_tribunal_by_name(nom)
        if tribunal:
            self.ui.cb_tribunal_registary.setCurrentIndex(self.list_tribunal.index(tribunal.nom))
    def on_council_changed(self, nom):
        council = self.data_manager.get_council_by_name(nom)
        if council:
            self.ui.cb_council.setCurrentIndex(self.list_council.index(council.nom))
    def on_council_registary_changed(self, nom):
        council = self.data_manager.get_council_by_name(nom)
        if council:
            self.ui.cb_council_registary.setCurrentIndex(self.list_council.index(council.nom))
    def on_room_changed(self, nom):
        room = self.data_manager.get_room_by_name(nom)
        if room:
            self.ui.cb_room.setCurrentIndex(self.list_rooms.index(room.nom))
    def on_section_changed(self, nom):
        section = self.data_manager.get_section_by_name(nom)
        if section:
            self.ui.cb_section.setCurrentIndex(self.list_sections.index(section.nom))
    
    def save_tribunal_registary(self):
        try:
            tribunal = self.data_manager.get_tribunal_by_name(self.ui.cb_tribunal_registary.currentText())
            if tribunal is None:
                tribunal = Tribunal()
                tribunal.nom = self.ui.cb_tribunal_registary.currentText()
                self.tribunal_registary = self.data_manager.add_tribunal(tribunal)
                self.ui.cb_tribunal_registary.setCurrentIndex(self.list_tribunal.index(tribunal.nom))
        except Exception as e:
            print(f"Error saving tribunal registary: {str(e)}")
            
    def save_council(self):
        try:
            council = self.data_manager.get_council_by_name(self.ui.cb_council.currentText())
            if council:
                self.council = council
                council.nom = self.ui.cb_council.currentText()
                self.data_manager.update_council(self.council)
            else:
                council = Council()
                council.nom = self.ui.cb_council.currentText()
                self.council = self.data_manager.add_council(council)
                self.ui.cb_council.setCurrentIndex(self.list_council.index(council.nom))
        except Exception as e:
            print(f"Error saving council: {str(e)}")
        
    def save_council_registary(self):
        try:
            council = self.data_manager.get_council_by_name(self.ui.cb_council_registary.currentText())
            if council:
                self.council_registary = council
                council.nom = self.ui.cb_council_registary.currentText()
                self.data_manager.update_council(self.council)

            else:
                council = Council()
                council.nom = self.ui.cb_council_registary.currentText()
                self.council_registary = self.data_manager.add_council(council)
                self.ui.cb_council_registary.setCurrentIndex(self.list_council.index(council.nom))
        except Exception as e:
            print(f"Error saving council registary: {str(e)}")
    def save_room(self):
        try:
            room = self.data_manager.get_room_by_name(self.ui.cb_room.currentText())
            if room:
                self.room = room
                self.room.nom = self.ui.cb_room.currentText()
                self.data_manager.update_room(self.room)
            else:
                room = Room()
                room.nom = self.ui.cb_room.currentText()
                self.room = self.data_manager.add_room(room)
                self.ui.cb_room.setCurrentIndex(self.list_rooms.index(room.nom))
        except Exception as e:
            print(f"Error saving room: {str(e)}")
        

    def save_section(self):
        try:
            section = self.data_manager.get_section_by_name(self.ui.cb_section.currentText())
            if section is None:
                section = Section()
                section.nom = self.ui.cb_section.currentText()
                self.section = self.data_manager.add_section(section)
                self.ui.cb_section.setCurrentIndex(self.list_sections.index(section.nom))
        except Exception as e:
            print(f"Error saving section: {str(e)}")
    
    def save_demandeur(self):
        try:
            if self.data_manager.get_demandeur_by_name(self.ui.cb_demandeur.currentText()):
                self.demandeur = self.data_manager.get_demandeur_by_name(self.ui.cb_demandeur.currentText())
                self.demandeur.nom = self.ui.cb_demandeur.currentText()
                self.demandeur.adresse = self.ui.le_address_demandeur.text()
                self.data_manager.update_demandeur(self.demandeur)
            else:
                demandeur = Demandeur()
                demandeur.nom = self.ui.cb_demandeur.currentText()
                demandeur.adresse = self.ui.le_address_demandeur.text()
                self.demandeur = self.data_manager.add_demandeur(demandeur)
                self.ui.cb_demandeur.setCurrentIndex(self.list_demandeurs.index(demandeur.nom))
        except Exception as e:
            print(f"Error saving demandeur: {str(e)}")
    
    def save_defendeur(self):
        logger.info(f"Defendeur:")
        try:
            if self.data_manager.get_defendeur_by_name(self.ui.cb_defendeur.currentText()):
                self.defendeur = self.data_manager.get_defendeur_by_name(self.ui.cb_defendeur.currentText())
                self.defendeur.nom = self.ui.cb_defendeur.currentText()
                self.defendeur.adresse = self.ui.le_address_defendeur.text()
                
                self.data_manager.update_defendeur(self.defendeur)
            else:
                defendeur = Defendeur() 
                defendeur.nom = self.ui.cb_defendeur.currentText()
                defendeur.adresse = self.ui.le_address_defendeur.text()
                
                self.defendeur = self.data_manager.add_defendeur(defendeur)
                self.ui.cb_defendeur.setCurrentIndex(self.list_defendeurs.index(defendeur.nom))
                
        except Exception as e:
            print(f"Error saving defendeur: {str(e)}")
    def save_tribunal(self):
        try:
            tribunal = self.data_manager.get_tribunal_by_name(self.ui.cb_tribunal.currentText())
            if tribunal is None:
                tribunal = Tribunal()
                tribunal.nom = self.ui.cb_tribunal.currentText()
                self.tribunal = self.data_manager.add_tribunal(tribunal)
                self.ui.cb_tribunal.setCurrentIndex(self.list_tribunal.index(tribunal.nom))     
        except Exception as e:
            print(f"Error saving tribunal: {str(e)}")
    
    def init_fields(self):
        
        
        self.tribunal_field.field_value = self.ui.cb_tribunal.currentText()
        self.tribunal_field.field_name = "tribunal"
        self.tribunal_field.field_type = "text"
        
        self.tribunal_registary_field.field_value = self.ui.cb_tribunal_registary.currentText()
        self.tribunal_registary_field.field_name = "tribunal_registary"
        self.tribunal_registary_field.field_type = "text"
        
        self.council_field.field_value = self.ui.cb_council.currentText()
        self.council_field.field_name = "council"
        self.council_field.field_type = "text"
      
        self.council_registary_field.field_value = self.ui.cb_council_registary.currentText()
        self.council_registary_field.field_name = "council_registary"
        self.council_registary_field.field_type = "text"
       
        self.room_field.field_value = self.ui.cb_room.currentText()
        self.room_field.field_name = "room"
        self.room_field.field_type = "text"
        
        self.section_field.field_value = self.ui.cb_section.currentText()
        self.section_field.field_name = "section"
        self.section_field.field_type = "text"
        
        self.hall_field.field_value = self.ui.le_hall.text()
        self.hall_field.field_name = "hall"
        self.hall_field.field_type = "text"
        
        self.date_audience_field.field_value = self.ui.de_audience.date().toString("yyyy-MM-dd")
        self.date_audience_field.field_name = "date_audience"
        self.date_audience_field.field_type = "DateTime"
        
        self.hour_audience_field.field_value = self.ui.te_audience.time().toString("hh:mm")
        self.hour_audience_field.field_name = "hour_audience"
        self.hour_audience_field.field_type = "Time"
        
        self.date_registary_field.field_value = self.ui.de_registary.date().toString("yyyy-MM-dd")
        self.date_registary_field.field_name = "date_registary"
        self.date_registary_field.field_type = "DateTime"
        
        self.case_number_field.field_value = self.ui.le_case.text()
        self.case_number_field.field_name = "case_number"
        self.case_number_field.field_type = "text"

    def save_dossier(self):
        try:
            # Préparer les documents
            documents = [
                self.tribunal_field, self.section_field, self.tribunal_registary_field,
                self.council_field, self.room_field, self.council_registary_field,
                self.hall_field, self.date_audience_field, self.hour_audience_field,
                self.case_number_field, self.date_registary_field
            ]
            
            # Récupérer les données nécessaires
            self.client = self.data_manager.get_client_by_name(self.ui.cb_client.currentText())
            category = self.data_manager.get_category_by_nom(self.ui.cb_type_rapport.currentText())
            self.document = self.data_manager.get_document_by_category_id(category.id)
            
            # Initialiser les champs
            self.init_fields()

            # Sauvegarder les entités liées
            self.save_demandeur()
            self.save_defendeur()
            if category.nom == "المحكمة":
                self.save_tribunal()
                self.save_tribunal_registary()
                self.save_section()
            else:
                self.save_council()
                self.save_room()
                self.save_council_registary()
            
            
            if self.dossier is not None:  # Mode édition
                # Mettre à jour le dossier existant
                self.dossier.client_id = self.client.id
                self.dossier.demandeur_id = self.demandeur.id
                self.dossier.defendeur_id = self.defendeur.id
                self.dossier.document_id = self.document.id
                
                updated_dossier = self.data_manager.update_dossier(self.dossier)
                if not updated_dossier:
                    raise Exception("Échec de la mise à jour du dossier")
                
                # Mettre à jour les champs
                for field in self.fields:
                    next_field = next((x for x in documents if x.field_name == field.field_name), None)
                   
                    if next_field:
                        field.document_id = self.document.id
                        field.field_value = next_field.field_value
                        self.data_manager.update_field(field)
                    
            else:  # Mode création
                if not all([self.client, self.demandeur, self.defendeur, self.document]):
                    raise Exception("Données manquantes pour la création du dossier")
                    
                # Créer le nouveau dossier
                logger.info(f"client: {self.client}")
                logger.info(f"demandeur: {self.demandeur}")
                logger.info(f"defendeur: {self.defendeur}")
                logger.info(f"document: {self.document}")
                self.dossier = self.data_manager.add_dossier(
                    self.client.id,
                    self.demandeur.id,
                    self.defendeur.id,
                    self.document.id
                )
                
                if not self.dossier:
                    raise Exception("Échec de la création du dossier")
                    
                # Ajouter les champs
                
                for field in documents:
                    self.data_manager.add_field(field, self.dossier.id, self.document.id)
            
            self.close()
            
        except Exception as e:
            logger.error(f"Error saving dossier: {str(e)}")
            QMessageBox.critical(
                self,
                "خطأ",
                "حدث خطأ أثناء حفظ الملف"
            )
   
        
    def export_dossier(self):
        pass
    def print_dossier(self):
        pass
        