import os
from config import archive_dir, templates_dir, logs_dir
from helpers.logger import logger
from core.db import init_db

def check_required_directories():
    """
    Vérifie et crée les répertoires nécessaires au démarrage de l'application.
    """
    directories = {
        'archives': archive_dir,
        'templates': templates_dir,
        'logs': logs_dir
    }
    
    for dir_name, dir_path in directories.items():
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                logger.info(f"Répertoire {dir_name} créé avec succès: {dir_path}")
            else:
                logger.debug(f"Répertoire {dir_name} existe déjà: {dir_path}")
                
            # Vérification des permissions
            if not os.access(dir_path, os.W_OK):
                logger.warning(f"Attention: Pas de permission d'écriture sur le répertoire {dir_name}: {dir_path}")
                
        except Exception as e:
            logger.error(f"Erreur lors de la création/vérification du répertoire {dir_name}: {str(e)}")
            raise Exception(f"Erreur critique: Impossible d'initialiser le répertoire {dir_name}")

def initialize_app():
    """
    Initialise l'application en vérifiant tous les prérequis nécessaires.
    """
    logger.info("Démarrage de l'initialisation de l'application...")
    
    try:
        # Vérification des répertoires
        check_required_directories()
        logger.info("Tous les répertoires requis sont prêts")
        
        # Initialisation de la base de données
        init_db()
        logger.info("Base de données initialisée avec succès")
        
    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation de l'application: {str(e)}")
        raise
    
    logger.info("Initialisation de l'application terminée avec succès")
