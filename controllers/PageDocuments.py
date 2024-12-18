from PySide6.QtWidgets import QWidget
from ui.page_documents_ui import Ui_page_documents

class PageDocuments(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_documents()
        self.ui.setupUi(self)
       

        
        