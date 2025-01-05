from models.models import (Client, Dossier, GenreEnum, Category, Document, Council, Room, 
                         Tribunal, Section, Demandeur, Defendeur, FieldValue, Bailiff, ArchiveBox)
from sqlalchemy import desc
from sqlalchemy.event import listens_for
from datetime import datetime
from sqlalchemy.orm import Session, joinedload
from helpers.logger import logger

class ClientServices:
    @staticmethod
    def create_client(db, obj: Client):
        """Crée un nouveau client dans la base de données."""
        try:
            # Convertir l'énumération en chaîne si nécessaire
            genre_value = obj.genre.value if isinstance(obj.genre, GenreEnum) else obj.genre
            
            client = Client(
                nom=obj.nom,
                genre=genre_value,  # Utiliser la valeur de l'énumération
                adresse=obj.adresse,
                phone=obj.phone,
                email=obj.email,
                mobile=obj.mobile,
                notes=obj.notes
            )
            db.add(client)
            db.commit()
            db.refresh(client)
            return client
        except Exception as e:
            db.rollback()
            logger.error(f"Erreur lors de la création du client: {str(e)}")
            return None

    @staticmethod
    def delete_client(db, client_id: int):
        """Supprime un client de la base de données."""
        try:
            client = db.query(Client).get(client_id)
            if client:
                db.delete(client)
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            logger.error(f"Erreur lors de la suppression du client: {str(e)}")
            return False

    @staticmethod
    def update_client(session, client):
        """Met à jour un client dans la base de données"""
        try:
            # Fusionner le client avec la session
            merged_client = session.merge(client)
            session.commit()
            # Rafraîchir pour avoir les données à jour
            session.refresh(merged_client)
            return merged_client
        except Exception as e:
            session.rollback()
            logger.error(f"Erreur lors de la mise à jour du client: {str(e)}")
            return None

    @staticmethod
    def get_all_clients(session):
        """Récupère tous les clients"""
        try:
            clients = session.query(Client).all()
            return clients
        except Exception as e:
            logger.error(f"Erreur lors de la récupération des clients: {str(e)}")
            return None

    @staticmethod
    def get_dossiers_client(db, client: Client):
        return db.query(Dossier).filter(Dossier.client_id == client.id).order_by(Dossier.date_modification).all()

    @staticmethod
    def get_client_by_id(db, client_id: int):
        """Récupère un client par son ID avec ses dossiers"""
        try:
            return db.query(Client).options(
                joinedload(Client.dossiers)
            ).filter(Client.id == client_id).first()
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du client {client_id}: {str(e)}")
            return None

    @staticmethod
    def get_client_by_nom(db, nom: str):
        return db.query(Client).filter(Client.nom == nom).first()

class DossierServices:
    @staticmethod
    def get_all_dossiers(db):
        
        return db.query(
            Dossier.id.label("id"),
            Dossier.code,
            Dossier.client_id,
            Dossier.demandeur_id,
            Dossier.defendeur_id,   
            Dossier.document_id,
            Client.nom.label("client_nom"),
            Demandeur.nom.label("demandeur_nom"),
            Defendeur.nom.label("defendeur_nom"),
            Document.titre.label("document_titre"),
            Dossier.date_creation,
            Dossier.date_modification
        ).join(Client, Dossier.client_id == Client.id).join(Demandeur, Dossier.demandeur_id == Demandeur.id).join(Defendeur, Dossier.defendeur_id == Defendeur.id).join(Document, Dossier.document_id == Document.id).order_by(desc(Dossier.date_modification)).all()
    
    
    @staticmethod
    def get_dossier_att_by_id(db, dossier_id: int):
        return db.query(
            Dossier.id,
            Dossier.code,
            Dossier.client_id,
            Dossier.demandeur_id,
            Dossier.defendeur_id,   
            Dossier.document_id,
            Client.nom.label("client_nom"),
            Client.adresse.label("client_adresse"),
            Demandeur.nom.label("demandeur_nom"),
            Demandeur.adresse.label("demandeur_adresse"),
            Defendeur.nom.label("defendeur_nom"),
            Defendeur.adresse.label("defendeur_adresse"),
            Document.titre.label("document_titre"),
            Document.path.label("document_path"),
            Dossier.date_creation,
            Dossier.date_modification
        ).join(Client, Dossier.client_id == Client.id).join(Demandeur, Dossier.demandeur_id == Demandeur.id).join(Defendeur, Dossier.defendeur_id == Defendeur.id).join(Document, Dossier.document_id == Document.id).filter(Dossier.id == dossier_id).first()
   
    @staticmethod
    def get_dossier_by_id(db, dossier_id: int):
        return db.query(Dossier).filter(Dossier.id == dossier_id).first()
    
    @staticmethod
    def create_dossier(db, client_id: int, demandeur_id: int, defendeur_id: int, document_id:int):
        dossier = Dossier(
            client_id=client_id,
            demandeur_id=demandeur_id,
            defendeur_id=defendeur_id, 
            document_id=document_id
        )
        db.add(dossier)
        db.commit()
        db.refresh(dossier)
        return dossier
    @staticmethod
    def update_dossier(db, obj: Dossier):
        dossier = db.query(Dossier).filter(Dossier.id == obj.id).first()
        if dossier:
            dossier.client_id = obj.client_id
            dossier.document_id = obj.document_id
            dossier.demandeur_id = obj.demandeur_id
            dossier.defendeur_id = obj.defendeur_id
            dossier.assignment = obj.assignment
            dossier.archive_box_id = obj.archive_box_id
            dossier.honoraires = obj.honoraires
            dossier.date_accus = obj.date_accus
            dossier.path_file = obj.path_file
            dossier.archive_status = obj.archive_status
            dossier.valid_status = obj.valid_status
            dossier.print_status = obj.print_status
            dossier.paye_status = obj.paye_status
            
            dossier.date_modification = obj.date_modification
            dossier.date_reminder = obj.date_reminder
            dossier.uplaod_at = obj.uplaod_at


            db.commit()
            db.refresh(dossier)
        return dossier
    # Delete dossier and all field values
    @staticmethod
    def delete_dossier(db, id: int):
        # Delete all field values
        db.query(FieldValue).filter(FieldValue.dossier_id == id).delete()
        dossier = db.query(Dossier).filter(Dossier.id == id).first()
        if dossier:
            db.delete(dossier)
            db.commit()
        return dossier
    @listens_for(Dossier, "before_insert")
    def generate_dossier_code(mapper, connection, target):
        current_year = datetime.now().year % 100
        prefix = f"{current_year:02}"
        # Obtenir la session en cours
        session = Session.object_session(target)
        if not session:
            raise RuntimeError("Impossible de générer le code : session introuvable.")

        # Récupérer le dernier code généré pour l'année courante
        last_code = session.query(Dossier.code)\
                           .filter(Dossier.code.like(f"{prefix}%"))\
                           .order_by(Dossier.id.desc())\
                           .first()

        # Extraire le dernier numéro ou initialiser à 0
        if last_code and last_code[0]:
            last_number = int(last_code[0].split('-')[1])
        else:
            last_number = 0
        # Générer un nouveau code incrémental
        new_number = last_number + 1
        target.code = f"{prefix}-{new_number:04d}"  # Ex : "24-0001"
    @staticmethod
    def get_dossier_by_code(db, code: str):
        return db.query(
            Dossier,
            Demandeur.nom.label("demandeur_nom"),
            Defendeur.nom.label("defendeur_nom"),
        ).filter(Dossier.code == code).join(Demandeur, Dossier.demandeur_id == Demandeur.id).join(Defendeur, Dossier.defendeur_id == Defendeur.id).first()
    
    @staticmethod
    def get_dossier_code(db, code: str):
        return db.query(Dossier).filter(Dossier.code == code).first()
    @staticmethod
    def get_dossiers_not_archived(db):
        return db.query(Dossier).filter(Dossier.archive_status == False).all()
    @staticmethod
    def get_dossiers_by_client_id(session, client_id):
        """Récupère tous les dossiers d'un client avec les relations nécessaires."""
        try:
            return (
                session.query(Dossier)
                .filter(Dossier.client_id == client_id)
                .options(
                    joinedload(Dossier.document),
                    joinedload(Dossier.demandeur),
                    joinedload(Dossier.defendeur)
                )
                .all()
            )
        except Exception as e:
            print(f"Erreur lors de la récupération des dossiers: {e}")
            return None

class DossiersServices:
    @staticmethod
    def get_all_documents(db):
        return db.query(Dossier).all()
    
   

class FieldValueServices:
    @staticmethod
    def get_all_field_values(db):
        return db.query(FieldValue).all()
    
    @staticmethod
    def create_field_value(db, obj: FieldValue, dossier_id: int, document_id: int):
        field_value = FieldValue(
            field_name=obj.field_name,
            field_type=obj.field_type,
            field_value=obj.field_value,
            document_id=document_id,
            dossier_id=dossier_id
        )
        db.add(field_value)
        db.commit()
        db.refresh(field_value)
        return field_value
    @staticmethod
    def get_fields_by_document_id_dossier_id(db, document_id, dossier_id):
        return db.query(FieldValue).filter(FieldValue.document_id == document_id).filter(FieldValue.dossier_id == dossier_id).all()
    
    @staticmethod
    def update_field(db, obj: FieldValue):
        field : FieldValue=  db.query(FieldValue).filter(FieldValue.id == obj.id).first()
        if field:
            field.field_name = obj.field_name
            field.field_type = obj.field_type
            field.field_value = obj.field_value
            field.document_id = obj.document_id
          
        
            db.commit()
            db.refresh(field)
        return field
    
    @staticmethod
    def get_fields_by_dossier_id(db, dossier_id):
        return db.query(FieldValue).filter(FieldValue.dossier_id == dossier_id).all()
class CategoryServices:
    @staticmethod
    def get_categories(db):
        return db.query(Category).filter(Category.parent_id == None).options(joinedload(Category.subcategories)).all()
    
    @staticmethod
    def get_category_by_id(db, category_id: int):
        return db.query(Category).filter(Category.id == category_id).first()
    
    def get_category_by_nom(db, nom: str):
        return db.query(Category).filter(Category.nom == nom).first()
    
    def get_documents_by_category(db, category_id: int):
        return db.query(Document).filter(Document.category_id == category_id).all()

    @staticmethod
    def create_category(db, obj: Category):
        category = Category(
            nom=obj.nom,
            parent_id=obj.parent_id
        )
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

class DocumentServices:
    @staticmethod
    def create_document(db, obj: Document):
        document = Document(
            nom=obj.nom,
            category_id=obj.category_id
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        return document
    
    @staticmethod
    def get_all_documents(db):
        return db.query(Document).all()
    @staticmethod
    def get_document_by_id(db, document_id: int):
        return db.query(Document).filter(Document.id == document_id).first()

    @staticmethod
    def get_document_by_category_id(db, category_id: int):
        return db.query(Document).filter(Document.category_id == category_id).first()

class CouncilServices:
    @staticmethod
    def create_council(db, obj: Council):
        council = Council(
            nom=obj.nom
        )
        db.add(council)
        db.commit()
        db.refresh(council)
        return council

    @staticmethod
    def get_all_councils(db):
        return db.query(Council).all()
    
    @staticmethod
    def get_council_by_nom(db, nom: str):
        return db.query(Council).filter(Council.nom == nom).first()
    
    @staticmethod
    def update_council(db, obj: Council):
        council = db.query(Council).filter(Council.id == obj.id).first()
        if council:
            council.nom = obj.nom
            db.commit()
            db.refresh(council)
        return council

class RoomServices:
    @staticmethod
    def get_all_rooms(db):
        return db.query(Room).all()
    
    @staticmethod
    def create_room(db, obj: Room):
        room = Room(
            nom=obj.nom
        )
        db.add(room)
        db.commit()
        db.refresh(room)
        return room
    @staticmethod
    def update_room(db, obj: Room):
        room = db.query(Room).filter(Room.id == obj.id).first()        
        if room:
            room.nom = obj.nom
            db.commit()
            db.refresh(room)
        return room
    @staticmethod
    def delete_room(db, obj: Room):
        room = db.query(Room).filter(Room.id == obj.id).first()
        if room:
            db.delete(room)
            db.commit()
        return room
    @staticmethod
    def get_room_by_nom(db, nom: str):
        return db.query(Room).filter(Room.nom == nom).first()

class TribunalServices:
    @staticmethod
    def get_all_tribunals(db):
        return db.query(Tribunal).all()
    
    @staticmethod
    def create_tribunal(db, obj: Tribunal):
        tribunal = Tribunal(
            nom=obj.nom
        )
        db.add(tribunal)
        db.commit()
        db.refresh(tribunal)
        return tribunal
    @staticmethod
    def update_tribunal(db, obj: Tribunal):
        tribunal = db.query(Tribunal).filter(Tribunal.id == obj.id).first()
        if tribunal:
            tribunal.nom = obj.nom
            db.commit()
            db.refresh(tribunal)
        return tribunal
    
    @staticmethod
    def get_tribunal_by_nom(db, nom: str):
        return db.query(Tribunal).filter(Tribunal.nom == nom).first()
    
class SectionServices:
    @staticmethod
    def get_all_sections(db):
        return db.query(Section).all()
    
    @staticmethod
    def create_section(db, obj: Section):
        section = Section(
            nom=obj.nom
        )
        db.add(section)
        db.commit()
        db.refresh(section)
        return section
    
    @staticmethod
    def update_section(db, obj: Section):
        section = db.query(Section).filter(Section.id == obj.id).first()
        if section:
            section.nom = obj.nom
            db.commit()
            db.refresh(section)
        return section
    
    @staticmethod
    def get_section_by_nom(db, nom: str):
        return db.query(Section).filter(Section.nom == nom).first()
    
class DemandeurServices:
    @staticmethod
    def get_all_demandeurs(db):
        return db.query(Demandeur).all()
    
    @staticmethod
    def get_demandeur_by_nom(db, nom: str):
        return db.query(Demandeur).filter(Demandeur.nom == nom).first()
    @staticmethod
    def get_demandeur_by_id(db, demandeur_id: int):
        return db.query(Demandeur).filter(Demandeur.id == demandeur_id).first()
    @staticmethod
    def create_demandeur(db, obj: Demandeur):
        demandeur = Demandeur(
            nom=obj.nom,
            adresse=obj.adresse
        )
        db.add(demandeur)
        db.commit()
        db.refresh(demandeur)
        return demandeur
    @staticmethod
    def update_demandeur(db, obj: Demandeur):
        demandeur = db.query(Demandeur).filter(Demandeur.id == obj.id).first()
        if demandeur:
            demandeur.nom = obj.nom
            demandeur.adresse = obj.adresse
            db.commit() 
            db.refresh(demandeur)
        return demandeur
    
class DefendeurServices:
    @staticmethod
    def get_all_defendeurs(db):
        return db.query(Defendeur).all()
    
    @staticmethod
    def get_defendeur_by_nom(db, nom: str):
        return db.query(Defendeur).filter(Defendeur.nom == nom).first()
    @staticmethod
    def get_defendeur_by_id(db, defendeur_id: int):
        return db.query(Defendeur).filter(Defendeur.id == defendeur_id).first()
    @staticmethod
    def create_defendeur(db, obj: Defendeur):
        defendeur = Defendeur(
            nom= obj.nom,
            adresse=obj.adresse
        )
        db.add(defendeur)
        db.commit()
        db.refresh(defendeur)
        return defendeur
    
    @staticmethod
    def update_defendeur(db, obj: Defendeur):
        defendeur = db.query(Defendeur).filter(Defendeur.id == obj.id).first()
        if defendeur:
            defendeur.nom = obj.nom
            defendeur.adresse = obj.adresse
            db.commit()
            db.refresh(defendeur)
        return defendeur
    
class BailiffServices:
    @staticmethod
    def get_all_bailiffs(db):
        return db.query(Bailiff).all()
    
    def create_bailiff(db, obj: Bailiff):
        bailiff = Bailiff(
            nom=obj.nom
        )
        db.add(bailiff)
        db.commit()
        db.refresh(bailiff)
        return bailiff
    
    def get_bailiff(db):
        return db.query(Bailiff).first()
    def update_bailiff(db, obj: Bailiff):
        bailiff = db.query(Bailiff).filter(Bailiff.id == obj.id).first()
        if bailiff:
            bailiff.nom = obj.nom
            bailiff.register_in = obj.register_in
            bailiff.address = obj.address
            bailiff.phone = obj.phone
            bailiff.mobile = obj.mobile
            bailiff.email = obj.email
            db.commit()
            db.refresh(bailiff)
        return bailiff
    
class ArchiveBoxServices:
    @staticmethod
    def create_archive_box(db, obj: ArchiveBox):
        archive_box = ArchiveBox(
            name=obj.name,
            description=obj.description
        )
        db.add(archive_box)
        db.commit()
        db.refresh(archive_box)
        return archive_box
    
    @staticmethod
    def get_all_archive_boxes(db):
        return db.query(ArchiveBox).all()
    
    @staticmethod
    def get_archive_box_by_name(db, name: str):
        return db.query(ArchiveBox).filter(ArchiveBox.name == name).first()
    @staticmethod
    def get_archive_boxes(db):
        """Récupère toutes les boîtes d'archives avec leurs dossiers et relations"""
        return db.query(ArchiveBox).options(
        joinedload(ArchiveBox.dossiers)
        .joinedload(Dossier.demandeur),
        joinedload(ArchiveBox.dossiers)
        .joinedload(Dossier.defendeur),
    ).all()
