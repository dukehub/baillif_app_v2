from PySide6.QtWidgets import QWidget
from ui.page_rapport_ui import Ui_page_rapports



class PageRapports(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_rapports()
        self.ui.setupUi(self)
        