from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import QObject, Slot
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient
from models.models import Client
from models.ClientTableMoel import ClientTableModel
from helpers.logger import logger
from core import event_manager, data_manager

from models.models import GenreEnum

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        self.ui.tableView_client.doubleClicked.connect(self.edit_client)
        
        # Configuration du modèle
        self.clients_model = ClientTableModel()
        self.ui.tableView_client.setModel(self.clients_model)
        
        # Configuration de la table
        self._setup_table()
        self._setup_signals()
        
        # Initialiser les labels vides
        self.clear_client_info()
        
        # Désactiver le bouton supprimer au démarrage
        self.ui.pb_delete.setEnabled(False)
        self.ui.pb_edit.setEnabled(False)
        
        # S'abonner aux événements de mise à jour
        event_manager.subscribe('client_updated', self.on_client_updated)
        
    def _setup_table(self):
        """Configure l'apparence et le comportement de la table"""
        table = self.ui.tableView_client
        
        # Ajuster les colonnes au contenu
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        table.horizontalHeader().setStretchLastSection(True)
        
        # Style de la table
        table.setAlternatingRowColors(True)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        
        # Masquer la grille
        table.setShowGrid(False)
        
        # Hauteur des lignes
        table.verticalHeader().setDefaultSectionSize(40)
        table.verticalHeader().hide()  # Cacher les numéros de lignes

    def _setup_signals(self):
        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)
        
        # Connecter la sélection de la table à l'affichage des détails
        self.ui.tableView_client.selectionModel().selectionChanged.connect(self.on_client_selected)

    def clear_client_info(self):
        """Efface les informations du client des labels"""
        self.ui.lbl_legal_status.setText("")
        self.ui.lbl_full_name.setText("")
        self.ui.lbl_address.setText("")
        self.ui.lbl_phone.setText("")
        self.ui.lbl_mobile.setText("")
        self.ui.lbl_email.setText("")
        self.ui.lbl_notes.setText("")

    def display_client_info(self, client: Client):
        """Affiche les informations du client dans les labels avec un format amélioré"""
        if client:
            # Format des informations avec des titres en gras
            self.ui.lbl_legal_status.setText(f"<b>الصفة القانونية:</b> {client.genre or '-'}")
            self.ui.lbl_full_name.setText(f"<b>الإسم و اللقب:</b> {client.nom or '-'}")
            self.ui.lbl_address.setText(f"<b>العنوان:</b> {client.adresse or '-'}")
            self.ui.lbl_phone.setText(f"<b>الهاتف:</b> {client.phone or '-'}")
            self.ui.lbl_mobile.setText(f"<b>الجوال:</b> {client.mobile or '-'}")
            self.ui.lbl_email.setText(f"<b>البريد الإلكتروني:</b> {client.email or '-'}")
            self.ui.lbl_notes.setText(f"<b>ملاحظات:</b> {client.notes or '-'}")
            
            # Activer le groupe d'informations
            self.ui.gb_infos.setEnabled(True)
        else:
            self.clear_client_info()
            self.ui.gb_infos.setEnabled(False)

    def on_client_selected(self, selected, deselected):
        """Appelé quand un client est sélectionné dans la table"""
        indexes = selected.indexes()
        if indexes:
            # Récupérer le client sélectionné
            row = indexes[0].row()
            selected_client = self.clients_model.clients[row]
            # Afficher ses informations
            self.display_client_info(selected_client)
            # Activer les boutons
            self.ui.pb_delete.setEnabled(True)
            self.ui.pb_edit.setEnabled(True)
        else:
            self.clear_client_info()
            # Désactiver les boutons
            self.ui.pb_delete.setEnabled(False)
            self.ui.pb_edit.setEnabled(False)

    def add_client(self):
        self.form_client = FormClient()
        self.form_client.exec_()

    def edit_client(self):
        """Édite le client sélectionné"""
        # Récupérer l'index de la ligne sélectionnée
        selected_indexes = self.ui.tableView_client.selectedIndexes()
        if not selected_indexes:
            QMessageBox.warning(
                self,
                "تحذير",
                "الرجاء اختيار عميل من القائمة"
            )
            return
        
        # Récupérer le client sélectionné depuis le modèle
        selected_row = selected_indexes[0].row()
        selected_client = self.clients_model.clients[selected_row]
        
        # Ouvrir le formulaire d'édition avec le client sélectionné
        self.form_client = FormClient(selected_client)
        self.form_client.exec_()

    def delete_client(self):
        """Supprime le client sélectionné"""
        # Récupérer l'index de la ligne sélectionnée
        selected_indexes = self.ui.tableView_client.selectedIndexes()
        if not selected_indexes:
            return
        
        # Récupérer le client sélectionné
        row = selected_indexes[0].row()
        client_to_delete = self.clients_model.clients[row]
        
        # Demander confirmation
        reply = QMessageBox.question(
            self,
            "تأكيد الحذف",
            f"هل أنت متأكد من حذف العميل {client_to_delete.nom}؟",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Supprimer le client
            if data_manager.delete_client(client_to_delete.id):
                # Effacer les informations affichées
                self.clear_client_info()
                # Désactiver les boutons
                self.ui.pb_delete.setEnabled(False)
                self.ui.pb_edit.setEnabled(False)
                # Message de succès
                QMessageBox.information(
                    self,
                    "نجاح",
                    "تم حذف العميل بنجاح"
                )
            else:
                QMessageBox.warning(
                    self,
                    "خطأ",
                    "حدث خطأ أثناء حذف العميل"
                )

    def on_client_updated(self, updated_client):
        """Appelé quand un client est mis à jour"""
        if updated_client is not None:
            # Si le client affiché est celui qui a été mis à jour
            current_selection = self.ui.tableView_client.selectedIndexes()
            if current_selection:
                row = current_selection[0].row()
                displayed_client = self.clients_model.clients[row]
                if displayed_client.id == updated_client.id:
                    # Mettre à jour l'affichage avec le client mis à jour
                    self.display_client_info(updated_client)

