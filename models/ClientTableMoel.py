from PySide6.QtCore import Qt, QAbstractTableModel
from models.models import Client
import logging

logger = logging.getLogger(__name__)


class ClientTableModel(QAbstractTableModel):
    def __init__(self, clients=None):
        super().__init__()
        self.clients = clients or []
        self.headers = ["الإسم و اللقب", "الصفة القانونية"]

    def rowCount(self, parent=None):
        return len(self.clients)

    def columnCount(self, parent=None):
        return 2  # Seulement 2 colonnes

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
                return client.nom or "N/A"
            elif column == 1:
                return client.genre or "N/A"

        except Exception as e:
            logger.error(f"Erreur lors de l'affichage des données: {str(e)}")
            return "Error"

        return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

