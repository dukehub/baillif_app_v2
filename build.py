import PyInstaller.__main__
import os
import shutil

def build_app():
    # Nettoyer les dossiers de build précédents
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')

    PyInstaller.__main__.run([
        'main.py',  # Script principal
        '--name=BailiffApp',  # Nom de l'exécutable
        '--windowed',  # Retiré pour avoir la console
        '--onedir',  # Créer un dossier avec tous les fichiers
        '--icon=ui/icons/bailiff_logo.ico',  # Icône de l'application
        '--add-data=ui;ui',  # Inclure le dossier ui
        '--add-data=templates;templates',  # Inclure le dossier templates
        '--debug=all',  # Ajouter les informations de débogage
        '--clean',  # Nettoyer avant la construction
        '--noconfirm',  # Ne pas demander de confirmation
    ])

    # Copier les fichiers supplémentaires nécessaires
    # shutil.copytree('migrations', 'dist/BailiffApp/migrations')
    #shutil.copy('alembic.ini', 'dist/BailiffApp/')
    
 

if __name__ == '__main__':
    build_app() 