import logging
import os
from logging.handlers import RotatingFileHandler
from helpers.config import basedir

# Création du dossier logs s'il n'existe pas
logs_dir = os.path.join(basedir, 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Configuration du logger
def setup_logger(name='bailiff_app'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Format du log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler pour fichier avec rotation
    file_handler = RotatingFileHandler(
        os.path.join(logs_dir, 'app.log'),
        maxBytes=1024 * 1024,  # 1 MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler pour la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Ajout des handlers au logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Logger par défaut de l'application
logger = setup_logger()

# Fonction pour obtenir un logger personnalisé
def get_logger(name):
    return setup_logger(name)
