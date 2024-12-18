from PySide6.QtWidgets import QWidget
from ui.page_penal_ui import Ui_page_penal

class PagePenal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_penal()
        self.ui.setupUi(self)