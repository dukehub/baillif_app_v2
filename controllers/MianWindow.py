from PySide6.QtWidgets import QMainWindow
from ui.main_window_ui import Ui_MainWindow
from controllers.PageDashboard import PageDashboard
from controllers.PageClients import PageClients
from controllers.PageDocuments import PageDocuments
from controllers.PagePenal import PagePenal
from controllers.PageSettings import PageSettings
from controllers.PageAuction import PageAuction
from controllers.PageArchives import PageArchives
from controllers.PageRapports import PageRapports
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pages = {
                'dashboard': PageDashboard(),
                'clients': PageClients(),
                'documents': PageDocuments(),
                'penal': PagePenal(),
                'settings': PageSettings(),
                'auction': PageAuction(),
                'archives': PageArchives(),
                'rapports': PageRapports()
            }

        for page in self.pages.values():
            self.ui.stackedWidget.addWidget(page)
        
        self.ui.stackedWidget.setCurrentWidget(self.pages['dashboard'])
        self.ui.pb_home.setChecked(True)

        self.ui.pb_home.clicked.connect(lambda: self.show_page('dashboard'))
        self.ui.pb_repports_show.clicked.connect(lambda: self.show_page('documents'))
        self.ui.pb_penal.clicked.connect(lambda: self.show_page('penal'))
        self.ui.pb_control.clicked.connect(lambda: self.show_page('settings'))
        self.ui.pb_auction.clicked.connect(lambda: self.show_page('auction'))
        self.ui.pb_clients_show.clicked.connect(lambda: self.show_page('clients'))
        self.ui.pb_archives.clicked.connect(lambda: self.show_page('archives'))
        self.ui.pb_repports_show.clicked.connect(lambda: self.show_page('rapports'))
        self.ui.pb_settings.clicked.connect(lambda: self.show_settings())
        self.ui.pb_exit.clicked.connect(self.close)
    
    def show_page(self, page_name):
        # Obtenez le widget actuellement affiché
        current_widget = self.ui.stackedWidget.currentWidget()
        
        # Retirez le widget courant si différent du nouveau widget
        if current_widget and current_widget != self.pages[page_name]:
            self.ui.stackedWidget.removeWidget(current_widget)
        
        # Ajoutez le nouveau widget s'il n'est pas déjà dans le QStackedWidget
        if self.ui.stackedWidget.indexOf(self.pages[page_name]) == -1:
            self.ui.stackedWidget.addWidget(self.pages[page_name])
        
        # Définissez le widget courant
        self.ui.stackedWidget.setCurrentWidget(self.pages[page_name])