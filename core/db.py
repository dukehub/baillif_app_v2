from config import DB_CONFIG
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = DB_CONFIG['url'] if 'url' in DB_CONFIG else f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['dbname']}"

# Initialisation de la connexion à la base de données
engine = create_engine(DATABASE_URL, echo=DB_CONFIG.get('echo', False), connect_args={"timeout": 10})

# Création de la session
Session = sessionmaker(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Import all models here
  
    Base.metadata.create_all(bind=engine)
