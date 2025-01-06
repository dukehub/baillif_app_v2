from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import QObject, Slot
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient
from models.models import Client
from models.ClientTableModel import ClientTableModel
from models.DossiersClientTableModel import DossiersClientTableModel
from helpers.logger import logger
from core import event_manager, data_manager, state_manager

from models.models import GenreEnum

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        
        # Ajouter une variable pour suivre le client sélectionné
        self.selected_client_id = None
        
        # Configuration du modèle
        self.clients_model = ClientTableModel()
        self.ui.tableView_client.setModel(self.clients_model)
        
        self.dossiers_client_model = DossiersClientTableModel()
        self.ui.tableView_dossiers.setModel(self.dossiers_client_model)
        self.dossiers_client_model.dataChangedSignal.connect(self.on_dossiers_data_changed)
        # Configuration de la table
        
     
        self._setup_signals()
        
        # Initialiser les labels vides
        self.clear_client_info()
        
        # Désactiver le bouton supprimer au démarrage
        self.ui.pb_delete.setEnabled(False)
        self.ui.pb_edit.setEnabled(False)
        
        # S'abonner aux changements d'état
        self.state_manager = state_manager
        self.state_manager.subscribe("current_client", self.on_current_client_changed)

   
       

    def _setup_signals(self):
        """Configure les signaux"""
        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)
        # filtre la table
        self.ui.le_find_clients.textChanged.connect(self.filter_clients)
        self.ui.le_find_dossiers.textChanged.connect(self.filter_dossiers)
        # Connecter la sélection de la table à l'affichage des détails
        self.ui.tableView_client.selectionModel().selectionChanged.connect(self.on_client_selected)
        # Ajouter le double-clic pour modifier
        self.ui.tableView_client.doubleClicked.connect(self.edit_client)

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
        """Affiche les informations du client dans les labels"""
        if client:
            # S'assurer d'utiliser les données les plus récentes
            self.ui.lbl_legal_status.setText(f"<b>الصفة القانونية:</b> {client.genre or '-'}")
            self.ui.lbl_full_name.setText(f"<b>الإسم و اللقب:</b> {client.nom or '-'}")
            self.ui.lbl_address.setText(f"<b>العنوان:</b> {client.adresse or '-'}")
            self.ui.lbl_phone.setText(f"<b>الهاتف:</b> {client.phone or '-'}")
            self.ui.lbl_mobile.setText(f"<b>الجوال:</b> {client.mobile or '-'}")
            self.ui.lbl_email.setText(f"<b>البريد الإلكتروني:</b> {client.email or '-'}")
            self.ui.lbl_notes.setText(f"<b>ملاحظات:</b> {client.notes or '-'}")
            
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
            # Stocker l'ID du client sélectionné
            self.selected_client_id = selected_client.id
            # Afficher ses informations
            self.display_client_info(selected_client)
            # Mettre à jour le modèle des dossiers
            self.dossiers_client_model.set_client(selected_client)
            # Activer les boutons
            self.ui.pb_delete.setEnabled(True)
            self.ui.pb_edit.setEnabled(True)
        else:
            self.selected_client_id = None
            self.clear_client_info()
            # Réinitialiser le modèle des dossiers
            self.dossiers_client_model.set_client(None)
            # Désactiver les boutons
            self.ui.pb_delete.setEnabled(False)
            self.ui.pb_edit.setEnabled(False)

    def add_client(self):
        self.form_client = FormClient()
        self.form_client.exec()

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
        self.form_client.exec()

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

    def on_current_client_changed(self, updated_client):
        """Appelé quand le client courant change"""
        if updated_client is not None:
            # Mettre à jour le modèle de la table
            self.clients_model.update_client(updated_client)
            
            # Si c'est le client actuellement sélectionné, mettre à jour l'affichage
            if self.selected_client_id == updated_client.id:
                self.display_client_info(updated_client)
    
    def filter_clients(self, text):
        """Filtre les clients dans la table"""
        self.clients_model.filter_clients(text)
    
    def on_dossiers_data_changed(self):
        """Appelé quand les données des dossiers changent"""
        self.ui.tableView_dossiers.resizeColumnsToContents()
        self.ui.tableView_dossiers.resizeRowsToContents()
    def filter_dossiers(self, text):
        """Filtre les dossiers dans la table"""
        self.dossiers_client_model.filter_dossiers(text)

