from PySide6.QtWidgets import QWidget
from ui.page_archives_ui import Ui_page_archives

class PageArchives(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_archives()
        self.ui.setupUi(self)
       