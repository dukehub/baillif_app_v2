from PySide6.QtWidgets import QWidget
from ui.page_settings_ui import Ui_page_settings

class PageSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_settings()
        self.ui.setupUi(self)