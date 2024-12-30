from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import QObject, Slot
from ui.page_clients_ui import Ui_page_clients
from controllers.widgets.FormClient import FormClient
from models.models import Client

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        self.validators_manager = ValidatorManager(self.ui)
        
        self.ui.tableView_client.doubleClicked.connect(self.edit_client)

        self.ui.pb_add.clicked.connect(self.add_client)
        self.ui.pb_edit.clicked.connect(self.edit_client)
        self.ui.pb_delete.clicked.connect(self.delete_client)



    def add_client(self):
        """Prépare le formulaire pour l'ajout d'un client"""
        if not self._check_unsaved_changes():
            return
            
        logger.debug("Mode ajout client")
        self.current_mode = 'add'
        # Désélectionner la ligne actuelle
        self.view.ui.tableView_client.clearSelection()
        self.view.clear_fields()
        self.view.set_fields_enabled(True)
        
        # Stocker les données initiales (vides) pour la comparaison
        self.initial_form_data = {
            'nom': '',
            'genre': '',
            'adresse': '',
            'email': '',
            'phone': '',
            'mobile': '',
            'notes': ''
        }
        self.has_unsaved_changes = False
        
        # En mode ajout : activer save (sera désactivé par la validation)
        self.view.set_buttons_enabled(False, delete_enabled=False, save_enabled=True)
        
        # Réinitialiser la validation
        self.validator_manager.clear_validation()
        # Forcer une validation initiale pour désactiver le bouton save
        self.validator_manager.validate()

    @Slot()
    def edit_client(self):
        """Active l'édition du client sélectionné"""
        logger.debug("Mode édition client")
        selected = self.view.ui.tableView_client.selectedIndexes()
        if not selected:
            logger.warning("Aucune ligne sélectionnée")
            return
            
        self.current_mode = 'edit'
        row = selected[0].row()
        client = self.clients[row]
        
        # Stocker les données initiales pour la comparaison
        self.initial_form_data = self.view.get_form_data()
        self.initial_form_data['id'] = client.id
        self.has_unsaved_changes = False
        
        # Réinitialiser la validation
        self.validator_manager.clear_validation()
        
        # Activer les champs pour l'édition
        self.view.set_fields_enabled(True)
        
        # En mode édition : activer save
        self.view.set_buttons_enabled(True, save_enabled=True)

    def save_client(self):
        """Sauvegarde les données du formulaire"""
        if not self.validator_manager.validate()[0]:
            logger.warning("Validation échouée")
            return
            
        client_data = self.view.get_form_data()
        logger.debug(f"Sauvegarde en mode {self.current_mode}")
        
        if self.current_mode == 'edit':
            selected = self.view.ui.tableView_client.selectedIndexes()
            if selected:
                row = selected[0].row()
                client = self.clients[row]
                client_data['id'] = client.id
                event_manager.emit('client_update_requested', client_data)
        else:  # mode add
            event_manager.emit('client_save_requested', client_data)
        
        # Réinitialiser le mode et l'interface après la sauvegarde
        self.current_mode = None
        self.has_unsaved_changes = False
        self.initial_form_data = {}
        self.view.clear_fields()
        self.view.set_fields_enabled(False)
        self.view.set_buttons_enabled(False)
        # Réinitialiser la validation
        self.validator_manager.clear_validation()

    def _on_validation_changed(self, is_valid: bool):
        """Gère le changement d'état de la validation"""
        logger.debug(f"État de validation changé: {is_valid}")
        # Activer le bouton save uniquement si la validation est ok
        if self.current_mode in ['add', 'edit']:
            self.view.ui.pb_save.setEnabled(is_valid)

    def _on_selection_changed(self):
        """Gère le changement de sélection dans la table"""
        if not self._check_unsaved_changes():
            # Annuler la sélection si l'utilisateur ne veut pas perdre les changements
            self.view.ui.tableView_client.clearSelection()
            return

        selected = self.view.ui.tableView_client.selectedIndexes()
        has_selection = bool(selected)
        
        if has_selection:
            # Charger les données du client sélectionné
            row = selected[0].row()
            client = self.clients[row]
            
            # Remplir le formulaire avec les données
            self.view.set_form_data(client)
            
            # Activer les boutons edit/delete
            self.view.set_buttons_enabled(True, save_enabled=False)
            
            # Réinitialiser le suivi des changements et le mode
            self.has_unsaved_changes = False
            self.current_mode = None
            self.initial_form_data = {}
            
            # Désactiver les champs jusqu'à ce que l'utilisateur clique sur edit
            self.view.set_fields_enabled(False)
        else:
            # Si aucune sélection
            self.view.clear_fields()
            self.view.set_fields_enabled(False)
            self.view.set_buttons_enabled(False)
            self.current_mode = None
            self.initial_form_data = {}

    @Slot(dict)
    def on_client_saved(self, client_data):
        """Appelé quand un client est sauvegardé"""
        try:
            logger.debug(f"Tentative de sauvegarde: {client_data}")
            
            # Convertir la valeur arabe en clé d'énumération
            genre_value = client_data['genre']
            genre_enum = None
            for genre in GenreEnum:
                if genre.value == genre_value:
                    genre_enum = genre
                    break
                    
            if not genre_enum:
                logger.error(f"Genre invalide: {genre_value}")
                event_manager.emit('client_save_error')
                return
            
            # Créer un objet Client avec l'énumération
            client = Client(
                nom=client_data['nom'],
                genre=genre_enum,  # Utiliser l'énumération directement
                adresse=client_data['adresse'],
                email=client_data['email'],
                phone=client_data['phone'],
                notes=client_data['notes']
            )
            
            result = data_manager.add_client(client)
            if result:
                logger.info("Client sauvegardé avec succès")
                self.refresh_clients()
                # Pas besoin de clear_fields() et set_fields_enabled() ici
                # car déjà fait dans save_client()
                event_manager.emit('client_save_success')
            else:
                logger.error("Échec de la sauvegarde du client")
                event_manager.emit('client_save_error')
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde du client: {str(e)}")
            event_manager.emit('client_save_error')

    def delete_client(self):
        """Supprime le client sélectionné"""
        selected = self.view.ui.tableView_client.selectedIndexes()
        if not selected:
            logger.warning("Aucun client sélectionné pour la suppression")
            return
            
        row = selected[0].row()
        client = self.clients[row]
        
        # Vérifier si le client a des dossiers associés en utilisant data_manager
        client_with_dossiers = data_manager.get_client_by_id(client.id)
        if client_with_dossiers and client_with_dossiers.dossiers and len(client_with_dossiers.dossiers) > 0:
            QMessageBox.warning(
                self.view,
                "تعذر الحذف",
                f"لا يمكن حذف العميل {client.nom} لأنه مرتبط بـ {len(client_with_dossiers.dossiers)} ملف(ات)",
                QMessageBox.Ok
            )
            return
        
        reply = QMessageBox.question(
            self.view,
            "تأكيد الحذف",
            f"هل أنت متأكد من حذف العميل {client.nom}؟",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            logger.debug(f"Tentative de suppression du client ID: {client.id}")
            event_manager.emit('client_delete_requested', client.id)

    @Slot(int)
    def on_client_deleted(self, client_id):
        """Appelé quand un client est supprimé"""
        try:
            result = data_manager.delete_client(client_id)
            if result:
                logger.info(f"Client {client_id} supprimé avec succès")
                self.refresh_clients()
                # Réinitialiser l'interface et la validation
                self.view.clear_fields()
                self.view.set_fields_enabled(False)
                self.view.set_buttons_enabled(False)
                self.validator_manager.clear_validation()
                event_manager.emit('client_delete_success')
            else:
                logger.error(f"Échec de la suppression du client {client_id}")
                QMessageBox.critical(
                    self.view,
                    "خطأ في الحذف",
                    "حدث خطأ أثناء حذف العميل",
                    QMessageBox.Ok
                )
                event_manager.emit('client_delete_error')
        except Exception as e:
            logger.error(f"Erreur lors de la suppression du client: {str(e)}")
            QMessageBox.critical(
                self.view,
                "خطأ في الحذف",
                "حدث خطأ غير متوقع أثناء حذف العميل",
                QMessageBox.Ok
            )
            event_manager.emit('client_delete_error')

    @Slot(dict)
    def on_client_updated(self, client_data):
        """Appelé quand un client est mis à jour"""
        try:
            # Convertir la valeur arabe en clé d'énumération
            genre_value = client_data['genre']
            genre_enum = None
            for genre in GenreEnum:
                if genre.value == genre_value:
                    genre_enum = genre
                    break
                    
            if not genre_enum:
                logger.error(f"Genre invalide: {genre_value}")
                event_manager.emit('client_update_error')
                return
            
            # Créer un objet Client avec l'énumération
            client = Client(
                id=client_data.get('id'),
                nom=client_data['nom'],
                genre=genre_enum,  # Utiliser l'énumération directement
                adresse=client_data['adresse'],
                email=client_data['email'],
                phone=client_data['phone'],
                notes=client_data['notes']
            )
            
            result = data_manager.update_client(client)
            if result:
                self.refresh_clients()
                self.view.clear_fields()
                self.view.set_fields_enabled(False)
                self.view.set_buttons_enabled(False)
                event_manager.emit('client_update_success')
            else:
                logger.error("Échec de la mise à jour du client")
                event_manager.emit('client_update_error')
        except Exception as e:
            logger.error(f"Erreur lors de la mise à jour du client: {str(e)}")
            event_manager.emit('client_update_error')

    def refresh_clients(self):
        """Rafraîchit la liste des clients"""
        try:
            logger.debug("Rafraîchissement de la liste des clients")
            clients = data_manager.get_all_clients()
            self.clients = clients if clients is not None else []
            # Debug des clients chargés
            for client in self.clients:
                logger.debug(f"Client chargé: ID={client.id}, Nom={client.nom}, Genre={client.genre}")
            self.model.clients = self.clients
            self.model.layoutChanged.emit()
            logger.debug(f"Nombre de clients chargés: {len(self.clients)}")
        except Exception as e:
            logger.error(f"Erreur lors du rafraîchissement des clients: {str(e)}")

    def _on_form_changed(self):
        """Appelé quand un champ du formulaire change"""
        if self.current_mode in ['add', 'edit']:
            current_data = self.view.get_form_data()
            self.has_unsaved_changes = current_data != self.initial_form_data
            logger.debug(f"Changements non sauvegardés: {self.has_unsaved_changes}")

    def _check_unsaved_changes(self):
        """Vérifie s'il y a des changements non sauvegardés"""
        if self.has_unsaved_changes:
            reply = QMessageBox.question(
                self.view,
                "تغييرات غير محفوظة",
                "لديك تغييرات غير محفوظة. هل تريد تجاهل هذه التغييرات؟",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            return reply == QMessageBox.Yes
        return True
