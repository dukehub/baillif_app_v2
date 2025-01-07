from helpers.config import DB_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers.config import Base



DATABASE_URL = DB_CONFIG['url'] if 'url' in DB_CONFIG else f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"


# Initialisation de la connexion à la base de données
engine = create_engine(DATABASE_URL, echo=DB_CONFIG.get('echo', False), connect_args={"timeout": 10})
# Création de la session
Session = sessionmaker(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base pour définir les modèles SQLAlchemy
# Importé depuis helpers.config pour assurer une base unique dans l'application
# Utilisé par tous les modèles pour hériter la classe de base SQLAlchemy
def init_db():
    """Initialise la base de données avec les données de base"""
    # Import des modèles pour les créer dans la base de données
    from models import models
    Base.metadata.create_all(bind=engine)
    
    # Vérifier si les données existent déjà
    with SessionLocal() as session:
        # Vérifier si les catégories existent déjà
        existing_categories = session.query(models.Category).first()
        if not existing_categories:
            try:
                # Initialisation des catégories
                categories_data = [
                    {"id": 1, "nom": "التكليفات", "parent_id": None},
                    {"id": 2, "nom": "التبليغات", "parent_id": None},
                    {"id": 3, "nom": "القرارات", "parent_id": None},
                    {"id": 4, "nom": "الاوامر", "parent_id": None},
                    {"id": 5, "nom": "إنذار", "parent_id": None},
                    {"id": 8, "nom": "المحكمة", "parent_id": 1},
                    {"id": 9, "nom": "المجلس", "parent_id": 1},
                ]
                
                for cat_data in categories_data:
                    category = models.Category(**cat_data)
                    session.add(category)
                
                # Initialisation des documents
                documents_data = [
                    {"id": 1, "titre": "تكليف تسليم المحكمة", "path": "dev_trib_tpl1.docx", "category_id": 8},
                    {"id": 2, "titre": "تكليف تسليم المجلس", "path": "dev_council_tpl1.docx", "category_id": 9},
                ]
                
                for doc_data in documents_data:
                    document = models.Document(**doc_data)
                    session.add(document)
                
                session.commit()
                print("Base de données initialisée avec succès")
                
            except Exception as e:
                session.rollback()
                print(f"Erreur lors de l'initialisation de la base de données: {str(e)}")
                raise
        else:
            print("La base de données est déjà initialisée")
