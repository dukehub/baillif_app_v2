from models.models import Client, GenreEnum
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QObject
from core import data_manager, state_manager, event_manager
from core.validators import ValidatorManager, NotEmptyValidator, EmailValidator, SelectionValidator
from ui.widgets.form_client_ui import Ui_form_client

class FormClient(QDialog):
    def __init__(self, client: Client = None):
        super().__init__()
        self.ui = Ui_form_client()
        self.ui.setupUi(self)
        self.controller = FormClientController()
        self.validator_manager = ValidatorManager(self.ui)
        self.validator_manager.validationStateChanged.connect(self.on_validation_state_changed)
        self.load_legal_status()
        self._setup_validators()
        self._setup_signals()
        # Désactiver le bouton save au démarrage
        self.ui.pb_save.setEnabled(False)

    def _setup_validators(self):
        """Configure les règles de validation pour chaque champ"""
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
        # Email est optionnel mais doit être valide s'il est rempli
        self.validator_manager.add_validation_rule(
            "le_mail", 
            "error_mail", 
            [EmailValidator("صيغة البريد الإلكتروني غير صحيحة")],
            optional=True
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

    def on_save_clicked(self):
        """Gère le clic sur le bouton Enregistrer"""
        if self._validator_form():
            client_data = {
                'nom': self.ui.le_full_name.text(),
                'genre': self.ui.cb_legal_status.currentText(),
                'adresse': self.ui.le_address.text(),
                'email': self.ui.le_mail.text(),
                'phone': self.ui.le_phone.text(),
                'notes': self.ui.txe_notes.toPlainText()
            }
            # Émettre l'événement de sauvegarde
            event_manager.emit('client_save_requested', client_data)
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

class FormClientController(QObject):
    def __init__(self):
        super().__init__()
        self.state_manager = state_manager
        self.data_manager = data_manager

   

   
        
