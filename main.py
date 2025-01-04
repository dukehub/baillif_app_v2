from PySide6.QtWidgets import QApplication
from controllers.MianWindow import MainWindow
from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale, Qt
from PySide6.QtGui import QFont, QScreen
from helpers.config import css_file
from helpers.init import initialize_app
import sys

if __name__ == "__main__":
    initialize_app()

    app = QApplication(sys.argv)
    app.setFont(QFont("Cairo", 11))
    
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    app.setStyleSheet(open(css_file, 'r', encoding='utf-8').read())
    
    # Configuration de la traduction
    translator = QTranslator()
    algeria_locale = QLocale(QLocale.Arabic, QLocale.Algeria)
    QLocale.setDefault(algeria_locale)
    
    if translator.load("qt_ar", QLibraryInfo.path(QLibraryInfo.TranslationsPath)):
        app.installTranslator(translator)
    else:
        print("Le fichier de traduction arabe n'a pas été trouvé.")

    window = MainWindow()
    
    # Récupérer la taille de l'écran avec la nouvelle méthode
    screen = app.primaryScreen()
    screen_geometry = screen.availableGeometry()
    
    # Régler la taille de la fenêtre    
    window.setSizeIncrement(screen_geometry.width(), screen_geometry.height())
    
    window.show()
    app.exec()

