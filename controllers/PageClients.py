from PySide6.QtWidgets import QWidget
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        
        self.ui.tableView_clients.doubleClicked.connect(self.edit_client)

        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)



    def add_client(self):
        form = FormClient()
        form.exec()

    def edit_client(self, client: Client):
        form = FormClient(client)
        form.exec()

    def delete_client(self, client: Client):
        pass