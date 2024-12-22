from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QEvent
from ui.main_window_ui import Ui_MainWindow
from controllers.PageDashboard import PageDashboard
from controllers.PageClients import PageClients
from controllers.PageDocuments import PageDocuments
from controllers.PagePenal import PagePenal
from controllers.PageSettings import PageSettings
from controllers.PageAuction import PageAuction
from controllers.PageArchives import PageArchives
from controllers.PageRapports import PageRapports
from core import event_manager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.current_page = None
        self.page_change_cancelled = False

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
        self.current_page = 'dashboard'
        self.ui.pb_home.setChecked(True)

        # Configuration des événements
        event_manager.subscribe('cancel_page_change', self._on_page_change_cancelled)
        event_manager.subscribe('cancel_app_close', self._on_app_close_cancelled)

        # Configuration des boutons
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
        if self.current_page == page_name:
            return
            
        # Émettre l'événement before_page_change
        event_manager.emit('before_page_change', page_name)
        
        # Si le changement de page a été annulé, ne rien faire
        if self.page_change_cancelled:
            self.page_change_cancelled = False
            # Recocher le bouton de la page actuelle
            self._check_current_page_button()
            return
            
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
        self.current_page = page_name
        
    def closeEvent(self, event):
        """Gère l'événement de fermeture de l'application"""
        # Émettre l'événement before_app_close
        event_manager.emit('before_app_close', event)
        
    def _on_page_change_cancelled(self):
        """Appelé quand le changement de page est annulé"""
        self.page_change_cancelled = True
        
    def _on_app_close_cancelled(self):
        """Appelé quand la fermeture de l'application est annulée"""
        self.close_cancelled = True
        
    def _check_current_page_button(self):
        """Recoche le bouton de la page actuelle"""
        button_map = {
            'dashboard': self.ui.pb_home,
            'documents': self.ui.pb_repports_show,
            'penal': self.ui.pb_penal,
            'settings': self.ui.pb_control,
            'auction': self.ui.pb_auction,
            'clients': self.ui.pb_clients_show,
            'archives': self.ui.pb_archives,
            'rapports': self.ui.pb_repports_show
        }
        
        if self.current_page in button_map:
            button_map[self.current_page].setChecked(True)