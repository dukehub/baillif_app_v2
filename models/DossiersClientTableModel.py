from typing import Any
from PySide6.QtCore import QAbstractTableModel, Qt, Signal
from PySide6.QtGui import QIcon
from core import state_manager, data_manager

class DossiersClientTableModel(QAbstractTableModel):
    dataChangedSignal = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dossiers = []
        self.current_client_id = None
        self._true_icon = QIcon(":/icons/icons/green_flag.png")  
        self._false_icon = QIcon(":/icons/icons/red_flag.png")
        
        # S'abonner aux changements d'état des dossiers
        state_manager.subscribe("dossiers_client", self.on_dossiers_updated)

    def set_client(self, client):
        """Définit le client actuel et charge ses dossiers"""
        if client:
            self.current_client_id = client.id
            self.dossiers = data_manager.get_dossiers_client(client.id)
            self.beginResetModel()
            self.endResetModel()
            self.dataChangedSignal.emit()

    def on_dossiers_updated(self, dossiers):
        """Mise à jour des dossiers"""
        if dossiers:
            # Ne mettre à jour que si les dossiers concernent le client actuel
            if self.current_client_id and any(d.client_id == self.current_client_id for d in dossiers):
                self.dossiers = [d for d in dossiers if d.client_id == self.current_client_id]
                self.beginResetModel()
                self.endResetModel()
                self.dataChangedSignal.emit()

    def rowCount(self, parent = None):
        return len(self.dossiers)
    
    def columnCount(self, parent = None):
        return 8
    
    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.dossiers):
            return None

        dossier = self.dossiers[index.row()]
        column = index.column()


        if role == Qt.DisplayRole:
            return {
                0: dossier.code,
                1: dossier.document.titre,
                2: dossier.demandeur.nom,
                3: dossier.defendeur.nom,
                4: dossier.date_creation.strftime("%d-%m-%Y") if dossier.date_creation else "N/A",
                5: dossier.date_modification.strftime("%d-%m-%Y") if dossier.date_modification else "N/A",
             
            }.get(column)

        elif role == Qt.DecorationRole and column in (6,7):
            value = (
                dossier.paye_status if column == 6 else
                dossier.valid_status 
                
            )
            return self._true_icon if value else self._false_icon

        return None
        
    def sort(self, column, order=Qt.AscendingOrder):
        """
        Tri les données du modèle en fonction de la colonne et de l'ordre spécifié.
        """
        if column == 0:
            # Exemple : Tri par le titre du document
            self.dossiers.sort(key=lambda dossier: dossier.code, reverse=(order == Qt.DescendingOrder))
        elif column == 1:
            # Exemple : Tri par le titre du document
            self.dossiers.sort(key=lambda dossier: dossier.document.titre, reverse=(order == Qt.DescendingOrder))
        elif column == 2:
            # Exemple : Tri par le nom du demandeur
            self.dossiers.sort(key=lambda dossier: dossier.demandeur.nom, reverse=(order == Qt.DescendingOrder))
        elif column == 3:
            # Exemple : Tri par le nom du défendeur
            self.dossiers.sort(key=lambda dossier: dossier.defendeur.nom, reverse=(order == Qt.DescendingOrder))
        elif column == 4:
            # Exemple : Tri par la date de création
            self.dossiers.sort(key=lambda dossier: dossier.date_creation or "", reverse=(order == Qt.DescendingOrder))
        elif column == 5:
            # Exemple : Tri par la date de modification
            self.dossiers.sort(key=lambda dossier: dossier.date_modification or "", reverse=(order == Qt.DescendingOrder))
        elif column in (6, 7):
            # Exemple : Tri par les colonnes booléennes
            if column == 6:
                self.dossiers.sort(key=lambda dossier: dossier.paye_status, reverse=(order == Qt.DescendingOrder))
            elif column == 7:
                self.dossiers.sort(key=lambda dossier: dossier.valid_status, reverse=(order == Qt.DescendingOrder))
       

        # Après le tri, émettez le signal de mise à jour des données
        self.layoutChanged.emit()

    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole) -> Any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Vertical:
            return section + 1
        if orientation == Qt.Horizontal:
            headers = ["رقم المحضر","نوع المحضر","الطالب","المطلوب","التاريخ","تاريخ التعديل","تم الدفع","تم التبليغ",]
            return headers[section]
    
    
    def refresh(self, new_data):
        if new_data != self.dossiers:
            self.beginResetModel()
            self.dossiers = new_data
            self.endResetModel()
            
            self.dataChangedSignal.emit()
    
    def filter_dossiers(self, text):
        if not text.strip():  # Si le texte est vide
            # Recharger tous les dossiers
            self.dossiers = data_manager.get_dossiers_client(self.current_client_id) or []
        else:
            # Filtrer les dossiers existants
            all_dossiers =  data_manager.get_dossiers_client(self.current_client_id) or []
            self.dossiers = [dossier for dossier in all_dossiers if text.lower() in dossier.code.lower() or text.lower() in dossier.document.titre.lower() or text.lower() in dossier.demandeur.nom.lower() or text.lower() in dossier.defendeur.nom.lower()]
         # Notifier le changement
        self.layoutAboutToBeChanged.emit()
        self.layoutChanged.emit()


