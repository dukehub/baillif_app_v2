from models.models import Client
from ui.widgets.form_client_ui import Ui_form_client
from PySide6.QtWidgets import QDialog

class FormClient(QDialog):
    def __init__(self, client: Client = None):
        super().__init__()
        self.ui = Ui_form_client()
        self.ui.setupUi(self)