from PySide6.QtCore import Qt, QAbstractTableModel
from models.models import Client
import logging
from core import state_manager, data_manager
from core import event_manager
logger = logging.getLogger(__name__)


class ClientTableModel(QAbstractTableModel):
    def __init__(self, clients=None):
        super().__init__()
        self.state_manager = state_manager
        self.data_manager = data_manager
        
        # Charger les clients initiaux
        self.clients = self.data_manager.get_all_clients() or []
        
        # S'abonner aux changements d'état et aux événements
        self.state_manager.subscribe('clients', self.on_clients_updated)
       
        
        self.headers = ["الصفة القانونية","الإسم و اللقب" ]

    def rowCount(self, parent=None):
        return len(self.clients)

    def columnCount(self, parent=None):
        return len(self.headers)  # Nombre de colonnes basé sur les en-têtes

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        try:
            client = self.clients[index.row()]
            column = index.column()

            if column == 0:
                return client.genre or "N/A"
            elif column == 1:
                return client.nom or "N/A"

        except Exception as e:
            logger.error(f"Erreur lors de l'affichage des données: {str(e)}")
            return "Error"

        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def on_clients_updated(self, clients):
        """Appelé quand l'état des clients change"""
        self.beginResetModel()
        self.clients = clients
        self.endResetModel()



