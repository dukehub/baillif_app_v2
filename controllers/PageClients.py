from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import QObject, Slot
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient
from models.models import Client
from models.ClientTableMoel import ClientTableModel
from helpers.logger import logger

from models.models import GenreEnum

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        self.ui.tableView_client.doubleClicked.connect(self.edit_client)
        
        self.clients_model = ClientTableModel()
        self.ui.tableView_client.setModel(self.clients_model)
        
        
        self._setup_signals() 
        
    def _setup_signals(self):
        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)


    # Les fonctions des boutons
    def add_client(self):
        self.form_client = FormClient()
        self.form_client.exec_()

    def edit_client(self):
        self.form_client = FormClient()
        self.form_client.exec_()

    def delete_client(self):
        pass

