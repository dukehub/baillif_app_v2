from PySide6.QtWidgets import QApplication
from controllers.MianWindow import MainWindow
from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale
from PySide6.QtCore import Qt

from helpers.config import css_file
from PySide6.QtGui import QFont
from helpers.init import initialize_app
import sys

if __name__ == "__main__":
    initialize_app()

    app = QApplication(sys.argv)
    
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    app.setStyleSheet(open(css_file, 'r', encoding='utf-8').read())
    

    translator = QTranslator()
    algeria_locale = QLocale(QLocale.Arabic, QLocale.Algeria)
    QLocale.setDefault(algeria_locale)
    
    if translator.load("qt_ar", QLibraryInfo.path(QLibraryInfo.TranslationsPath)):
        app.installTranslator(translator)
    else:
        print("Le fichier de traduction arabe n'a pas été trouvé.")
    window = MainWindow()
    window.setSizeIncrement(1500, 800)
    window.show()
    app.exec()

