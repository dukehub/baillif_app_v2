from PySide6.QtWidgets import QWidget
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient
from models.models import Client
from services.validators import ValidatorManager, NotEmptyValidator, EmailValidator

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        self.validators_manager = ValidatorManager(self.ui)
        
        self.ui.tableView_client.doubleClicked.connect(self.edit_client)

        
        self._setup_signals()
        self._setup_validator()
        self._setup_validator_state()
        
    def _setup_signals(self):
        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)
        
        self.ui.le_full_name.textChanged.connect(self.on_text_changed)
        self.ui.le_address.textChanged.connect(self.on_text_changed)
        self.ui.le_phone.textChanged.connect(self.on_text_changed)
        self.ui.le_mail.textChanged.connect(self.on_text_changed)
        
    def on_text_changed(self):
        self.validators_manager.validate()
        

    def _setup_validator(self):
        self.validators_manager.add_validation_rule("le_full_name", "error_full_name", [ NotEmptyValidator()])
        self.validators_manager.add_validation_rule("le_address", "error_address", [ NotEmptyValidator()])
        self.validators_manager.add_validation_rule("le_phone", "error_phone", [ NotEmptyValidator()])
        self.validators_manager.add_validation_rule("le_mail", "error_mail", [ EmailValidator()])    

    def _setup_validator_state(self):
        self.validators_manager.validationStateChanged.connect(self.on_validator_state_changed)

    def on_validator_state_changed(self, is_valid: bool):
        self.ui.pb_add.setEnabled(is_valid)
        self.ui.pb_edit.setEnabled(is_valid)
        self.ui.pb_delete.setEnabled(is_valid)


    def add_client(self):
        form = FormClient()
        form.exec()

    def edit_client(self, client: Client=None):
        form = FormClient(client)
        form.exec()

    def delete_client(self, client: Client=None):
        pass