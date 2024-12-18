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


def init_db():
    # Import des modèles pour les créer dans la base de données
    from models import models
    Base.metadata.create_all(bind=engine)
