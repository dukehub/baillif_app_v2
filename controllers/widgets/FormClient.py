from models.models import Client, GenreEnum
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QObject
from core import data_manager, state_manager, event_manager
from core.validators import ValidatorManager, NotEmptyValidator, EmailValidator, SelectionValidator
from ui.widgets.form_client_ui import Ui_form_client
from helpers.logger import logger

class FormClient(QDialog):
    def __init__(self, client: Client = None):
        super().__init__()
        self.ui = Ui_form_client()
        self.ui.setupUi(self)
        self.data_manager = data_manager
        
        self.validator_manager = ValidatorManager(self.ui)
        self.validator_manager.validationStateChanged.connect(self.on_validation_state_changed)
        
        # Mode édition ou création
        self.edit_mode = client is not None
        self.client = client
        
        self.load_legal_status()
        self._setup_validators()
        self._setup_signals()
        
        # Charger les données du client si en mode édition
        if self.edit_mode:
            self.load_client_data()
            self.setWindowTitle("تعديل بيانات العميل")
        else:
            self.ui.pb_save.setEnabled(False)

    def _setup_validators(self):
        """Configure les règles de validation pour chaque champ"""
        # Champs obligatoires
        self.validator_manager.add_validation_rule(
            "le_full_name", 
            "error_full_name", 
            [NotEmptyValidator("الاسم إلزامي")]
        )
        self.validator_manager.add_validation_rule(
            "cb_legal_status", 
            "error_legal_status", 
            [NotEmptyValidator("الصفة القانونية إلزامية")]
        )
        self.validator_manager.add_validation_rule(
            "le_address", 
            "error_address", 
            [NotEmptyValidator("العنوان إلزامي")]
        )
        
        # Champs optionnels
        self.validator_manager.add_validation_rule(
            "le_mail", 
            "error_mail", 
            [EmailValidator("صيغة البريد الإلكتروني غير صحيحة")],
            optional=True  # Rend le champ vraiment optionnel
        )
       

    def _setup_signals(self):
        """Configure les connexions des signaux"""
        # Boutons
        self.ui.pb_save.clicked.connect(self.on_save_clicked)
        self.ui.pb_cancel.clicked.connect(self.on_cancel_clicked)

        # Validation en temps réel
        self.ui.le_full_name.textChanged.connect(
            lambda: self.validator_manager._validate_field("le_full_name"))
        self.ui.le_mail.textChanged.connect(
            lambda: self.validator_manager._validate_field("le_mail"))
        self.ui.le_address.textChanged.connect(
            lambda: self.validator_manager._validate_field("le_address"))
        self.ui.cb_legal_status.currentTextChanged.connect(
            lambda: self.validator_manager._validate_field("cb_legal_status"))

    def load_legal_status(self):
        """Charge les types de clients depuis GenreEnum dans la combobox"""
        self.ui.cb_legal_status.addItem("")  # Option vide par défaut
            
            # Ajoute chaque type depuis l'énumération
        for genre in GenreEnum:
            self.ui.cb_legal_status.addItem(genre.value)  # On utilise .value pour obtenir la chaîne en arabe
    
    def load_client_data(self):
        """Charge les données du client dans le formulaire"""
        if self.client:
            self.ui.le_full_name.setText(self.client.nom)
            self.ui.cb_legal_status.setCurrentText(self.client.genre)
            self.ui.le_address.setText(self.client.adresse)
            self.ui.le_phone.setText(self.client.phone)
            self.ui.le_mobile.setText(self.client.mobile)
            self.ui.le_mail.setText(self.client.email)
            self.ui.txe_notes.setPlainText(self.client.notes)

    def on_save_clicked(self):
        """Gère le clic sur le bouton Enregistrer"""
        if self._validator_form():
            client_data = {
                'nom': self.ui.le_full_name.text(),
                'genre': self.ui.cb_legal_status.currentText(),
                'adresse': self.ui.le_address.text(),
                'email': self.ui.le_mail.text(),
                'phone': self.ui.le_phone.text(),
                'mobile': self.ui.le_mobile.text(),
                'notes': self.ui.txe_notes.toPlainText()
            }
            
            if self.edit_mode:
                # Vérifier que quelqu'un écoute l'événement avant de le déclencher
                subscribers_count = event_manager.get_subscribers_count('client_updated')
                logger.debug(f"FormClient: {subscribers_count} abonnés trouvés pour client_updated")
                
                self.client.update(**client_data)
                updated_client = self.data_manager.update_client(self.client)
                
                if not updated_client:
                    logger.error("FormClient: Échec de la mise à jour du client")
                    QMessageBox.warning(self, "خطأ", "حدث خطأ أثناء تحديث بيانات العميل")
                    return
            else:
                self.client = Client(**client_data)
                self.data_manager.add_client(self.client)
            
            self.close()

    def on_cancel_clicked(self):
        self.close()

    def _validator_form(self) -> bool:
        """Valide le formulaire complet"""
        is_valid, errors = self.validator_manager.validate()
        if not is_valid:
            error_messages = []
            for field, field_errors in errors.items():
                if isinstance(field_errors, list):
                    error_messages.extend(field_errors)
                else:
                    error_messages.append(f"{field}: {field_errors}")
            
            QMessageBox.warning(
                self,
                "أخطاء التحقق",  # Titre de la boîte de dialogue
                "\n".join(error_messages)
            )
        return is_valid

    def on_validation_state_changed(self, is_valid: bool):
        """Gère le changement d'état de la validation"""
        self.ui.pb_save.setEnabled(is_valid)
    
    def get_client_data(self):
        return self.client

   

   

   
        
