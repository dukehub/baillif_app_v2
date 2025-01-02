from pickle import FALSE
from sqlalchemy import Column, Integer, CheckConstraint, ForeignKey, String, Boolean, Float, DateTime, Text, Enum, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from helpers.config import Base

import enum, json
from datetime import datetime


# Enums
class RapportType(enum.Enum):
    TRIBUNAL = "المحكمة"
    COUNCIL = "المجلس"

class Templates(enum.Enum):
    SIMPLE = "عادي"
    SIMPLE_TABLE = "عادي بهامش"
    LOGO_TABLE = "بهامش مع شعار"

class GenreEnum(enum.Enum):
    PERSON = "شخص طبيعي"
    COMPANY = "شركة"
    AVOCAT = "محامي"
    HUISSIER = "محضر"
    EXPERT = "خبير"
    PUBLIC = "هيئة عمومية"
    OTHER = "اخرى"

    @classmethod
    def from_arabic(cls, value):
        """Convertit une valeur arabe en énumération"""
        try:
            return next(genre for genre in cls if genre.value == value)
        except StopIteration:
            return None

    def to_arabic(self):
        """Retourne la valeur arabe de l'énumération"""
        return self.value

    def __str__(self):
        return self.value

# Tables
class Demandeur(Base):
    __tablename__ = "demandeurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(Text, nullable=False, index=True)
    adresse = Column(Text)
    dossiers = relationship("Dossier", back_populates="demandeur")

class Defendeur(Base):
    __tablename__ = "defendeurs"
    id = Column(Integer, primary_key=True, index=True)  
    nom = Column(Text, nullable=False, index=True)
    adresse = Column(Text)
    dossiers = relationship("Dossier", back_populates="defendeur")

class ArchiveBox(Base):
    __tablename__ = 'archive_boxes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # Nom de la boîte d'archive
    description = Column(Text, nullable=True)  # Description ou détails supplémentaires
    created_at = Column(DateTime, default=func.now(), nullable=False)  # Date de création

    # Relation avec les dossiers
    dossiers = relationship("Dossier", back_populates="archive_box")

class Dossier(Base):
    __tablename__ = 'dossiers'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    document_id = Column(Integer, ForeignKey('documents.id'), nullable=False)
    demandeur_id = Column(Integer, ForeignKey('demandeurs.id'), nullable=False)
    defendeur_id = Column(Integer, ForeignKey('defendeurs.id'), nullable=False)
    archive_box_id = Column(Integer, ForeignKey('archive_boxes.id'), nullable=True)
    
    code = Column(String(10), unique=True, nullable=False, index=True)
    assignment = Column(Text, nullable=True)
    path_file = Column(Text, nullable=True)
    paye_status = Column(Boolean, default=False, index=True)
    print_status = Column(Boolean, default=False, index=True)
    valid_status = Column(Boolean, default=False)
    num_archive = Column(String(10), nullable=True)
    archive_status = Column(Boolean, default=False)
    date_creation = Column(DateTime, server_default=func.now())
    date_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())
    date_reminder = Column(DateTime)
    date_accus = Column(DateTime)
    uplaod_at = Column(DateTime)
    honoraires = Column(Numeric(20, 2), nullable=True)
        
    document = relationship("Document", back_populates="dossiers")
    client = relationship("Client", back_populates="dossiers")
    demandeur = relationship("Demandeur", back_populates="dossiers")
    defendeur = relationship("Defendeur", back_populates="dossiers")
    fields = relationship("FieldValue", back_populates="dossier")
    archive_box = relationship("ArchiveBox", back_populates="dossiers")
    paiements = relationship("Paiement", back_populates="dossier")
    factures = relationship("Facture", secondary="facture_dossiers", back_populates="dossiers")
    __table_args__ = (  
        CheckConstraint('demandeur_id IS NOT NULL', name='check_demandeur_not_null'),
        CheckConstraint('defendeur_id IS NOT NULL', name='check_defendeur_not_null'),
    )

class Paiement(Base):
    __tablename__ = "paiements"
    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float, CheckConstraint('montant >= 0.0', name='check_positive_montant'))
    date_paiment = Column(DateTime, default=func.now())
    remise = Column(Float, CheckConstraint('remise >= 0.0', name='check_positive_remise'))
    dossier_id = Column(Integer, ForeignKey("dossiers.id"), nullable=False)
    dossier = relationship("Dossier", back_populates="paiements")

    @property
    def montant_apres_remise(self):
        return self.montant - self.remise

class Facture(Base):
    __tablename__ = "factures"
    id = Column(Integer, primary_key=True, index=True)
    total_honoraires = Column(Numeric(20, 2), nullable=False, default=0.0)
    date_creation = Column(DateTime, server_default=func.now(), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    client = relationship("Client", back_populates="factures")
    total_paye = Column(Numeric(20, 2), nullable=False, default=0.0)
    reste_regler = Column(Numeric(20, 2), nullable=False, default=0.0)

    dossiers = relationship("Dossier",  secondary="facture_dossiers", back_populates="factures")

    def calculer_totaux(self):
        self.total_honoraires = sum(dossier.honoraires for dossier in self.dossiers)
        self.total_paye = sum(sum(paiement.montant_apres_remise for paiement in dossier.paiements) for dossier in self.dossiers)
        self.reste_regler = self.total_honoraires - self.total_paye

class FactureDossier(Base):
    __tablename__ = "facture_dossiers"
    id = Column(Integer, primary_key=True, index=True)
    dossier_id = Column(Integer, ForeignKey('dossiers.id', ondelete="CASCADE"), nullable=False)
    facture_id = Column(Integer, ForeignKey('factures.id', ondelete="CASCADE"), nullable=False)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
    parent = relationship('Category', remote_side=[id], backref='subcategories')

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    path = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', backref="documents")
    fields = relationship("FieldValue", back_populates="document")
    dossiers = relationship("Dossier", back_populates="document")

class FieldValue(Base):
    __tablename__ = "field_values"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey('documents.id'), nullable=False)
    dossier_id = Column(Integer, ForeignKey('dossiers.id'), nullable=False)  # Association avec le document
    
    # Informations sur le champ spécifique
    field_name = Column(String, nullable=False)  # Nom du champ, ex. "Date de signature"
    field_type = Column(String, nullable=False)  # Type du champ, ex. "String", "Date"
    field_value = Column(String, nullable=True)  # Valeur spécifique de ce champ pour ce document

    document = relationship("Document", back_populates="fields")
    dossier = relationship("Dossier", back_populates="fields")

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False, index=True)
    genre = Column(String, nullable=False)
    adresse = Column(String)
    phone = Column(String)
    mobile = Column(String)
    notes = Column(String)
    email = Column(String)
    date_creation = Column(DateTime, server_default=func.now())
    dossiers = relationship("Dossier", back_populates="client")
    factures = relationship("Facture", back_populates="client")

    @property
    def genre_enum(self):
        """Convertit la valeur string en énumération"""
        return GenreEnum.from_arabic(self.genre)

    @genre_enum.setter
    def genre_enum(self, value):
        """Convertit l'énumération en string"""
        if isinstance(value, GenreEnum):
            self.genre = value.value
        else:
            self.genre = value
    
    def update(self, **kwargs):
        """Met à jour les attributs du client avec les nouvelles valeurs"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        # Mettre à jour la date de modification
        self.updated_at = datetime.now()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    pseudo = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    role = Column(String)

class Tribunal(Base):
    __tablename__ = "tribunaux"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    
class Council(Base):
    __tablename__ = "councils"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)

class Bailiff(Base):
    __tablename__ = "bailiffs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    register_in = Column(String)
    address = Column(String)
    phone = Column(String)
    mobile = Column(String)
    email = Column(String)