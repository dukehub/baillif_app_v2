from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import QObject, Slot
from ui.page_clients_ui import Ui_page_clients
from models.models import Client, GenreEnum
from core.validators import ValidatorManager, NotEmptyValidator, EmailValidator
from models.ClientTableMoel import ClientTableModel
from core import event_manager, state_manager, data_manager
from helpers.logger import logger

class PageClients(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_page_clients()
        self.ui.setupUi(self)
        
        # Créer le contrôleur et lui passer la référence de la vue
        self.controller = PageClientsController(self)
        
        # Configuration initiale de l'UI
        self._setup_ui()
        
        # Connecter les signaux de changement de page et de fermeture
        event_manager.subscribe('before_page_change', self._on_before_page_change)
        event_manager.subscribe('before_app_close', self._on_before_app_close)
        
    def _setup_ui(self):
        """Configure l'interface utilisateur initiale"""
        # Setup table view
        self.ui.tableView_client.setColumnWidth(0, 100)
        self.ui.tableView_client.setColumnWidth(1, 200)
        self.ui.tableView_client.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
  
        self.ui.tableView_client.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_client.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView_client.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Désactiver les boutons et champs au démarrage
        self.set_buttons_enabled(False)
        self.set_fields_enabled(False)

    def set_buttons_enabled(self, edit_enabled: bool, delete_enabled: bool = None, save_enabled: bool = None):
        """Configure l'état des boutons"""
        if delete_enabled is None:
            delete_enabled = edit_enabled
        if save_enabled is None:
            save_enabled = edit_enabled
            
        self.ui.pb_edit.setEnabled(edit_enabled)
        self.ui.pb_delete.setEnabled(delete_enabled)
        self.ui.pb_save.setEnabled(save_enabled)

    def set_fields_enabled(self, enabled: bool):
        """Active/désactive les champs du formulaire"""
        self.ui.le_full_name.setEnabled(enabled)
        self.ui.cb_legal_status.setEnabled(enabled)
        self.ui.le_address.setEnabled(enabled)
        self.ui.le_mail.setEnabled(enabled)
        self.ui.le_phone.setEnabled(enabled)
        self.ui.le_mobile.setEnabled(enabled)
        self.ui.txe_notes.setEnabled(enabled)

    def clear_fields(self):
        """Vide les champs du formulaire"""
        self.ui.le_full_name.clear()
        self.ui.cb_legal_status.setCurrentIndex(0)
        self.ui.le_address.clear()
        self.ui.le_mail.clear()
        self.ui.le_phone.clear()
        self.ui.le_mobile.clear()
        self.ui.txe_notes.clear()

    def get_form_data(self):
        """Récupère les données du formulaire"""
        return {
            'nom': self.ui.le_full_name.text(),
            'genre': self.ui.cb_legal_status.currentText(),
            'adresse': self.ui.le_address.text(),
            'email': self.ui.le_mail.text(),
            'phone': self.ui.le_phone.text(),
            'mobile': self.ui.le_mobile.text(),
            'notes': self.ui.txe_notes.toPlainText()
        }

    def set_form_data(self, client):
        """Remplit le formulaire avec les données du client"""
        logger.debug(f"Remplissage du formulaire avec: {client.__dict__}")
        self.ui.le_full_name.setText(client.nom)
        self.ui.cb_legal_status.setCurrentText(client.genre)
        self.ui.le_address.setText(client.adresse or '')
        self.ui.le_mail.setText(client.email or '')
        self.ui.le_phone.setText(client.phone or '')
        self.ui.le_mobile.setText(client.mobile or '')
        self.ui.txe_notes.setPlainText(client.notes or '')
        logger.debug("Formulaire rempli")

    def _on_before_page_change(self, new_page):
        """Vérifie les changements non sauvegardés avant de changer de page"""
        if self.controller.has_unsaved_changes:
            reply = QMessageBox.question(
                self,
                "تغييرات غير محفوظة",
                "لديك تغييرات غير محفوظة. هل تريد تجاهل هذه التغييرات؟",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.No:
                # Empêcher le changement de page
                event_manager.emit('cancel_page_change')
                return False
            
        # Réinitialiser le formulaire si on change de page
        self._reset_form()
        return True
        
    def _on_before_app_close(self, event=None):
        """Vérifie les changements non sauvegardés avant de fermer l'application"""
        if self.controller.has_unsaved_changes:
            reply = QMessageBox.question(
                self,
                "تغييرات غير محفوظة",
                "لديك تغييرات غير محفوظة. هل تريد تجاهل هذه التغييرات؟",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.No:
                # Empêcher la fermeture
                event_manager.emit('cancel_app_close')
                if event:
                    event.ignore()
                return False
                
        # Réinitialiser le formulaire
        self._reset_form()
        return True
        
    def _reset_form(self):
        """Réinitialise le formulaire et son état"""
        self.controller.current_mode = None
        self.controller.has_unsaved_changes = False
        self.controller.initial_form_data = {}
        self.clear_fields()
        self.set_fields_enabled(False)
        self.set_buttons_enabled(False)


class PageClientsController(QObject):
    def __init__(self, view) -> None:
        super().__init__()
        self.view = view
        self.clients = []
        self.model = ClientTableModel(self.clients)
        self.current_mode = None  # 'add' ou 'edit'
        self.has_unsaved_changes = False
        self.initial_form_data = {}  # Pour stocker les données initiales du formulaire
        logger.debug("Initialisation du PageClientsController")
        
        # Setup du modèle
        self.view.ui.tableView_client.setModel(self.model)
        
        # Setup des validateurs
        self.validator_manager = ValidatorManager(self.view.ui)
        self._setup_validators()
        
        # Setup des connexions
        self._setup_signals()
        self._setup_events()
        
        # Chargement initial des données
        self.refresh_clients()
        self.load_legal_status()
        logger.debug("Initialisation terminée")

    def _setup_validators(self):
        """Configure les règles de validation"""
        self.validator_manager.add_validation_rule(
            "le_full_name", 
            "error_full_name", 
            [NotEmptyValidator("الاسم إلزامي")]
        )
        self.validator_manager.add_validation_rule(
            "cb_legal_status", 
            "error_legal_status", 
            [NotEmptyValidator("الصفة القانونية إلزامية")]
        )
        self.validator_manager.add_validation_rule(
            "le_address", 
            "error_address", 
            [NotEmptyValidator("العنوان إلزامي")]
        )
        self.validator_manager.add_validation_rule(
            "le_mail", 
            "error_mail", 
            [EmailValidator("صيغة البريد الإلكتروني غير صحيحة", optional=True)]
        )

        # Connecter les validateurs
        self.validator_manager.validationStateChanged.connect(self._on_validation_changed)
        
    def _setup_signals(self):
        """Configure les connexions des signaux"""
        # Boutons
        self.view.ui.pb_add.clicked.connect(self.add_client)
        self.view.ui.pb_edit.clicked.connect(self.edit_client)
        self.view.ui.pb_delete.clicked.connect(self.delete_client)
        self.view.ui.pb_save.clicked.connect(self.save_client)
        
        # Validation en temps réel
        self.view.ui.le_full_name.textChanged.connect(self._on_form_changed)
        self.view.ui.cb_legal_status.currentTextChanged.connect(self._on_form_changed)
        self.view.ui.le_address.textChanged.connect(self._on_form_changed)
        self.view.ui.le_mail.textChanged.connect(self._on_form_changed)
        self.view.ui.le_phone.textChanged.connect(self._on_form_changed)
        self.view.ui.le_mobile.textChanged.connect(self._on_form_changed)
        self.view.ui.txe_notes.textChanged.connect(self._on_form_changed)

    def _setup_events(self):
        """Configure les abonnements aux événements"""
        logger.debug("Configuration des événements")
        event_manager.subscribe('client_save_requested', self.on_client_saved)
        event_manager.subscribe('client_delete_requested', self.on_client_deleted)
        event_manager.subscribe('client_update_requested', self.on_client_updated)
        
        if self.view.ui.tableView_client.model():
            selection_model = self.view.ui.tableView_client.selectionModel()
            if selection_model:
                selection_model.selectionChanged.connect(self._on_selection_changed)
                logger.debug("Signal de sélection connecté")

    def load_legal_status(self):
        """Charge les types de clients"""
        self.view.ui.cb_legal_status.clear()
        self.view.ui.cb_legal_status.addItem("")
        for genre in GenreEnum:
            self.view.ui.cb_legal_status.addItem(genre.value)

    @Slot()
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
