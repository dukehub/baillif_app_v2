from PySide6.QtCore import QAbstractTableModel, Qt, Signal
from core import data_manager, state_manager

class DossiersTableModel(QAbstractTableModel):
    def __init__(self, row_per_page = 30):
        layoutChangedSignal = Signal()
        super().__init__()
        self._dossiers = data_manager._update_dossiers_state()
        self._row_per_page = row_per_page
        self.current_page = 0
        state_manager.subscribe("dossiers", self.refresh)

    def rowCount(self, parent=None):
        return min(self._row_per_page, len(self._dossiers) - self.current_page * self._row_per_page)
    
    def columnCount(self, parent=None):
        return 7

    def data(self, index, role):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        
        row = self.current_page * self._row_per_page + index.row()
        dossier = self._dossiers[row]
        column_mapping = {
            0: dossier.code,
            1: dossier.document_titre,
            2: dossier.client_nom,  
            3: dossier.demandeur_nom,
            4: dossier.defendeur_nom,
            5: dossier.date_creation.strftime('%Y-%m-%d') if dossier.date_creation else "",
            6: dossier.date_modification.strftime('%Y-%m-%d') if dossier.date_modification else "",
        }
        
        return column_mapping.get(index.column(), None)
    
    def setPage(self, page):
        self.current_page = page
        self.layoutChanged.emit()
    def totalPage(self):
        return (len(self._dossiers) + self._row_per_page - 1) // self._row_per_page
    
    def sort(self, column, order=Qt.AscendingOrder):
        """
        Tri les données du modèle en fonction de la colonne et de l'ordre spécifié.
        """
        if column == 0:
            # Exemple : Tri par le titre du document
            self._dossiers.sort(key=lambda dossier: dossier.code, reverse=(order == Qt.DescendingOrder))
        elif column == 1:
            self._dossiers.sort(key=lambda dossier: dossier.document_titre, reverse=(order == Qt.DescendingOrder))
        elif column == 2:
            self._dossiers.sort(key=lambda dossier: dossier.client_nom, reverse=(order == Qt.DescendingOrder))
        elif column == 3:
            # Exemple : Tri par le nom du demandeur
            self._dossiers.sort(key=lambda dossier: dossier.demandeur_nom, reverse=(order == Qt.DescendingOrder))
        elif column == 4:
            # Exemple : Tri par le nom du défendeur
            self._dossiers.sort(key=lambda dossier: dossier.defendeur_nom, reverse=(order == Qt.DescendingOrder))
        elif column == 5:
            # Exemple : Tri par la date de création
            self._dossiers.sort(key=lambda dossier: dossier.date_creation or "", reverse=(order == Qt.DescendingOrder))
        elif column == 6:
            # Exemple : Tri par la date de modification
            self._dossiers.sort(key=lambda dossier: dossier.date_modification or "", reverse=(order == Qt.DescendingOrder))
        self.layoutChanged.emit()
    def filter_dossier(self, text):
        self.layoutAboutToBeChanged.emit()

        if not hasattr(self, "_original_dossiers"):
            # Crée une copie immuable de la liste d'origine si elle n'existe pas déjà
            self._original_dossiers = self._dossiers.copy()

        if text.strip():  # Si un texte de recherche est fourni
            text_lower = text.lower()
            self._dossiers = [
                dossier for dossier in self._original_dossiers
                if any(text_lower in (field.lower() if field else '') for field in (
                    dossier.document_titre,
                    dossier.demandeur_nom,
                    dossier.defendeur_nom
                ))
            ]
        else:
            # Si le texte est vide, restaure la liste complète des dossiers
            self._dossiers = self._original_dossiers.copy()

        self.layoutChanged.emit()
        
    def refresh(self, dossiers):
        if dossiers:
            self.layoutAboutToBeChanged.emit()
            self._dossiers = dossiers
            self.layoutChanged.emit()
            
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
        # Numérotation des lignes dans les en-têtes verticaux
            if orientation == Qt.Vertical:
                return str(section + 1)  # Numérotation des lignes
            # Noms des colonnes dans les en-têtes horizontaux
            elif orientation == Qt.Horizontal:
                headers = ["رقم المحضر","نوع المحضر", "العميل", "الطالب", "المطلوب", "تاريخ الإنشاء", "تاريخ التعديل"]
                return headers[section]
        return None
    