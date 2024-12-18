from PySide6.QtWidgets import QWidget
from ui.page_dashboard_ui import Ui_page_dashboard
class PageDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_dashboard()
        self.ui.setupUi(self)