from PySide6.QtCore import QObject
from core.data_services import (ClientServices, DocumentServices, SectionServices, CouncilServices, DemandeurServices,
                                    RoomServices, TribunalServices, DefendeurServices, DossierServices, FieldValueServices,
                                    CategoryServices, BailiffServices, ArchiveBoxServices)
from .db import Session
from core import state_manager, event_manager
from helpers import logger



class DataManager(QObject):
    def __init__(self, state_manager=None):
        super().__init__()
        self.state_manager = state_manager
        

    def set_state_manager(self, state_manager):
        self.state_manager = state_manager
    

    def _with_session(self, service_method, *args, **kwargs):
        session = Session()
        try:
            result = service_method(session, *args, **kwargs)
            return result
        except Exception as e:
            session.rollback()

            print(f"Erreur dans {service_method.__name__}: {e}")
            return None
        finally:
            session.close()

    def _update_clients_state(self):
        """Met à jour l'état des clients."""
        clients = self._with_session(ClientServices.get_all_clients)
        if clients is not None:
            self.state_manager.set_state("clients", clients)
        return clients

    def _update_dossiers_state(self):
        """Met à jour l'état des dossiers."""
        dossiers = self._with_session(DossierServices.get_all_dossiers)
        if dossiers is not None:
            self.state_manager.set_state("dossiers", dossiers)
        return dossiers
    def _update_demandeurs_state(self):
        """Met à jour l'état des demandeurs."""
        demandeurs = self._with_session(DemandeurServices.get_all_demandeurs)
        if demandeurs is not None:
            self.state_manager.set_state("demandeurs", demandeurs)
        return demandeurs

    def _update_defendeurs_state(self):
        """Met à jour l'état des defendeurs."""
        defendeurs = self._with_session(DefendeurServices.get_all_defendeurs)
        if defendeurs is not None:
            self.state_manager.set_state("defendeurs", defendeurs)
        return defendeurs

    def _update_sections_state(self):
        """Met à jour l'état des sections."""
        sections = self._with_session(SectionServices.get_all_sections)
        if sections is not None:
            self.state_manager.set_state("sections", sections)
        return sections

    def _update_tribunals_state(self):
        """Met à jour l'état des tribunals."""
        tribunals = self._with_session(TribunalServices.get_all_tribunals)
        if tribunals is not None:
            self.state_manager.set_state("tribunals", tribunals)
        return tribunals

    def _update_rooms_state(self):
        """Met à jour l'état des rooms."""
        rooms = self._with_session(RoomServices.get_all_rooms)
        if rooms is not None:
            self.state_manager.set_state("rooms", rooms)
        return rooms

    def _update_councils_state(self):
        """Met à jour l'état des councils."""
        councils = self._with_session(CouncilServices.get_all_councils)
        if councils is not None:
            self.state_manager.set_state("councils", councils)
        return councils

    def _update_documents_state(self):
        """Met à jour l'état des documents."""
        documents = self._with_session(DocumentServices.get_all_documents)
        if documents is not None:
            self.state_manager.set_state("documents", documents)
        return documents

    def _update_categories_state(self):
        """Met à jour l'état des categories."""
        categories = self._with_session(CategoryServices.get_all_categories)
        if categories is not None:
            self.state_manager.set_state("categories", categories)
        return categories

    def _update_bailiff(self):
        bailiffs = self._with_session(BailiffServices.get_all_bailiffs)
        if bailiffs is not None:
            self.state_manager.set_state("bailiffs", bailiffs)
        return bailiffs

    def _update_archive_boxes(self):
        archive_boxes = self._with_session(ArchiveBoxServices.get_all_archive_boxes)
        if archive_boxes is not None:
            self.state_manager.set_state("archive_boxes", archive_boxes)
        return archive_boxes
    

    def get_all_clients(self):
        """Récupère tous les clients."""
        return self._update_clients_state()

    def get_client_by_name(self, nom):
        return self._with_session(ClientServices.get_client_by_nom, nom)
        
    def get_client_by_id(self, id):
        return self._with_session(ClientServices.get_client_by_id, id)
        
    def add_client(self, new_client):
        """Ajoute un nouveau client et met à jour l'état."""
        result = self._with_session(ClientServices.create_client, new_client)
        if result:
            return self._update_clients_state()
        return None
    
    def delete_client(self, client_id):
        """Supprime un client et met à jour l'état."""
        success = self._with_session(ClientServices.delete_client, client_id)
        if success:
            return self._update_clients_state()
        return None
    
    def update_client(self, client):
        """Met à jour un client existant"""
        updated_client = self._with_session(ClientServices.update_client, client)
        if updated_client:
            # Récupérer la liste complète des clients mise à jour
            all_clients = self._with_session(ClientServices.get_all_clients)
            # Mettre à jour l'état avec la nouvelle liste
            self.state_manager.set_state("clients", all_clients)
            # Émettre l'événement avec le client mis à jour
            event_manager.emit('client_updated', updated_client)
            return updated_client
        return None

    def get_all_councils(self):
        return self._with_session(CouncilServices.get_all_councils)

    def add_council(self, new_council):
        result = self._with_session(CouncilServices.create_council, new_council)
        if result:
            self._update_councils_state()
        return result

    def update_council(self, council_data):
        result = self._with_session(CouncilServices.update_council, council_data)
        if result:
            self._update_councils_state()
        return result

    def get_council_by_name(self, nom):
        return self._with_session(CouncilServices.get_council_by_nom, nom)

    def get_all_tribunals(self):
        return self._with_session(TribunalServices.get_all_tribunals)

    def add_tribunal(self, new_tribunal):
        result = self._with_session(TribunalServices.create_tribunal, new_tribunal)
        if result:
            self._update_tribunals_state()
        return result

    def update_tribunal(self, tribunal_data):
        result = self._with_session(TribunalServices.update_tribunal, tribunal_data)
        if result:
            self._update_tribunals_state()
        return result

    def get_tribunal_by_name(self, nom):
        return self._with_session(TribunalServices.get_tribunal_by_nom, nom)

    def get_all_rooms(self):
        return self._with_session(RoomServices.get_all_rooms)

    def add_room(self, new_room):
        result = self._with_session(RoomServices.create_room, new_room)
        if result:
            self._update_rooms_state()
        return result

    def update_room(self, room_data):
        result = self._with_session(RoomServices.update_room, room_data)
        if result:
            self._update_rooms_state()
        return result

    def get_room_by_name(self, nom):
        return self._with_session(RoomServices.get_room_by_nom, nom)

    def get_all_sections(self):
        return self._with_session(SectionServices.get_all_sections)

    def add_section(self, new_section):
        result = self._with_session(SectionServices.create_section, new_section)
        if result:
            self._update_sections_state()
        return result

    def update_section(self, section_data):
        result = self._with_session(SectionServices.update_section, section_data)
        if result:
            self._update_sections_state()
        return result

    def get_section_by_name(self, nom):
        return self._with_session(SectionServices.get_section_by_nom, nom)

    def get_all_documents(self):
        return self._with_session(DocumentServices.get_all_documents)

    def get_document_by_category_id(self, category_id):
        return self._with_session(DocumentServices.get_document_by_category_id, category_id)

    def get_document_by_id(self, id):
        return self._with_session(DocumentServices.get_document_by_id, id)

    def get_all_demandeurs(self):
        return self._with_session(DemandeurServices.get_all_demandeurs)

    def add_demandeur(self, new_demandeur):
        result = self._with_session(DemandeurServices.create_demandeur, new_demandeur)
        if result:
            self._update_demandeurs_state()
        return result

    def update_demandeur(self, demandeur):
        result = self._with_session(DemandeurServices.update_demandeur, demandeur)
        if result:
            self._update_demandeurs_state()
        return result

    def get_demandeur_by_name(self, nom):
        return self._with_session(DemandeurServices.get_demandeur_by_nom, nom)

    def get_demandeur_by_id(self, id):
        return self._with_session(DemandeurServices.get_demandeur_by_id, id)

    def get_all_defendeurs(self):
        return self._with_session(DefendeurServices.get_all_defendeurs)

    def add_defendeur(self, new_defendeur):
        result = self._with_session(DefendeurServices.create_defendeur, new_defendeur)
        if result:
            self._update_defendeurs_state()
        return result

    def update_defendeur(self, defendeur):
        result = self._with_session(DefendeurServices.update_defendeur, defendeur)
        if result:
            self._update_defendeurs_state()
        return result

    def get_defendeur_by_name(self, nom):
        return self._with_session(DefendeurServices.get_defendeur_by_nom, nom)

    def get_defendeur_by_id(self, id):
        return self._with_session(DefendeurServices.get_defendeur_by_id, id)

    def get_all_dossiers(self):
        return self._with_session(DossierServices.get_all_dossiers)

    def get_dossier_att_by_id(self, id):
        return self._with_session(DossierServices.get_dossier_att_by_id, id)

    def get_dossier_by_id(self, id):
        return self._with_session(DossierServices.get_dossier_by_id, id)

    def get_dossiers_not_archived(self):
        return self._with_session(DossierServices.get_dossiers_not_archived)

    def get_dossiers_client(self, client):
        """Récupère tous les dossiers d'un client."""
        dossiers = self._with_session(DossierServices.get_dossiers_by_client_id, client.id)
        if dossiers:
            self.state_manager.set_state("dossiers_client", dossiers)
        return dossiers

    def add_dossier(self, client_id, demandeur_id, defendeur_id, document_id):
        result = self._with_session(DossierServices.create_dossier, client_id, demandeur_id, defendeur_id, document_id)
        if result:
            self._update_dossiers_state()
        return result

    def update_dossier(self, dossier):
        result = self._with_session(DossierServices.update_dossier, dossier)
        if result:
            self._update_dossiers_state()
        return result

    def delete_dossier(self, dossier_id):
        success = self._with_session(DossierServices.delete_dossier, dossier_id)
        if success:
            self._update_dossiers_state()
        return success

    def get_dossier_by_code(self, code):
        return self._with_session(DossierServices.get_dossier_by_code, code)

    def get_dossier_code(self, code):
        return self._with_session(DossierServices.get_dossier_code, code)

    def add_field(self, new_field, dossier_id, document_id):
        result = self._with_session(FieldValueServices.create_field_value, new_field, dossier_id, document_id)
        if result:
            self._update_fields_state()
        return result

    def update_field(self, field_value):
        return self._with_session(FieldValueServices.update_field, field_value)

    def get_fields_by_document_id_dossier_id(self, document_id, dossier_id):
        return self._with_session(FieldValueServices.get_fields_by_document_id_dossier_id, document_id, dossier_id)

    def get_fields_by_dossier_id(self, dossier_id):
        return self._with_session(FieldValueServices.get_fields_by_dossier_id, dossier_id)

    def get_categories(self):
        return self._with_session(CategoryServices.get_categories)

    def get_category_by_nom(self, nom):
        return self._with_session(CategoryServices.get_category_by_nom, nom)

    def get_category_by_id(self, id):
        return self._with_session(CategoryServices.get_category_by_id, id)

    def add_bailiff(self, new_bailiff):
        result = self._with_session(BailiffServices.create_bailiff, new_bailiff)
        if result:
            self.state_manager.set_state("bailiffs", result)
        return result

    def update_bailiff(self, bailiff):
        result = self._with_session(BailiffServices.update_bailiff, bailiff)
        if result:
            self.state_manager.set_state("bailiffs", result)
        return result

    def get_bailiff(self):
        return self._with_session(BailiffServices.get_bailiff)

    def add_archive_box(self, archive_box):
        result = self._with_session(ArchiveBoxServices.create_archive_box, archive_box)
        if result:
            self._update_archive_boxes_state()
        return result

    def get_all_archive_boxes(self):
        return self._with_session(ArchiveBoxServices.get_all_archive_boxes)

    def get_archive_box_by_name(self, name):
        return self._with_session(ArchiveBoxServices.get_archive_box_by_name, name)

    def get_archive_boxes(self):
        """Récupère toutes les boîtes d'archives avec leurs dossiers."""
        return self._with_session(ArchiveBoxServices.get_archive_boxes)