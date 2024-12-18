from PySide6.QtWidgets import QWidget
from ui.page_auction_ui import Ui_page_auction

class PageAuction(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_auction()
        self.ui.setupUi(self)