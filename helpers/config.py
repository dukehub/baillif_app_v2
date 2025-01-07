import os
from pathlib import Path
from PySide6.QtCore import QSettings
from sqlalchemy.ext.declarative import declarative_base
# revinir au repertoire parent

basedir = Path(__file__).parent.parent
archive_dir = os.path.join(basedir, "archives")
templates_dir = os.path.join(basedir, "templates")
css_file = os.path.join(basedir, "ui", "style.qss")
logs_dir = os.path.join(basedir, "logs")

# Création des répertoires s'ils n'existent pas
for directory in [archive_dir, logs_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)
        
Base = declarative_base()
DB_CONFIG_DEV = {
    'url': f'sqlite:///{os.path.join(basedir, "db_dev.db")}?charset=utf8',
    'echo': False
}

# Configuration pour SQLite en production
DB_CONFIG_PROD = {
    'url': f'sqlite:///{os.path.join(basedir, "db_bailiff.db")}?charset=utf8',
    'echo': False
}

# Basculter entre SQLite et PostgreSQL
ENV = os.getenv('APP_ENV', 'prod')
DB_CONFIG = DB_CONFIG_DEV if ENV == 'dev' else DB_CONFIG_PROD

# Configuration de l'application
APP_NAME = 'Bailiff_App'
APP_VERSION = '1.0.0'
APP_ORGANIZATION = 'DEVOXX'
APP_DOMAIN = 'devoxx.dz'
APP_SETTINGS = QSettings(APP_ORGANIZATION, APP_NAME)
APP_SETTINGS.setValue('version', APP_VERSION)
APP_SETTINGS.setValue('domain', APP_DOMAIN)
APP_SETTINGS.setValue('env', ENV)
APP_SETTINGS.setValue('db_config', DB_CONFIG)
APP_SETTINGS.setValue('basedir', basedir)
APP_SETTINGS.setValue('app_name', APP_NAME)
APP_SETTINGS.setValue('app_version', APP_VERSION)
APP_SETTINGS.setValue('app_organization', APP_ORGANIZATION)
APP_SETTINGS.setValue('app_domain', APP_DOMAIN)
APP_SETTINGS.setValue('app_settings', APP_SETTINGS)
APP_SETTINGS.sync()

