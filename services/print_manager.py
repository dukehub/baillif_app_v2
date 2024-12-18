import os
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWidgets import QMessageBox
import win32com.client


class PrintManager:
    """
    Classe dédiée à l'impression de documents.
    """

    def __init__(self, parent=None):
        self.parent = parent  # La fenêtre parente pour les dialogues, si nécessaire

    def print_with_dialog(self, file_path):
        """
        Imprime un fichier DOCX avec une boîte de dialogue pour sélectionner l'imprimante.
        """
        if not os.path.exists(file_path):
            QMessageBox.warning(self.parent, "Erreur", f"Fichier introuvable : {file_path}")
            return

        # Configurer une imprimante avec Qt
        printer = QPrinter()

        dialog = QPrintDialog(printer, self.parent)
        if dialog.exec():
            try:
                # Imprime le document avec les paramètres sélectionnés
                self._print_docx(file_path)
                QMessageBox.information(self.parent, "Succès", "Impression réussie.")
            except Exception as e:
                QMessageBox.critical(self.parent, "Erreur", f"Erreur lors de l'impression : {e}")

    def _print_docx(self, file_path):
        """
        Imprime un fichier DOCX directement via Word.
        """
        word_app = win32com.client.Dispatch("Word.Application")
        word_app.Visible = False  # Word en arrière-plan

        # Ouvrir le document
        doc = word_app.Documents.Open(file_path)

        # Lancer l'impression
        doc.PrintOut()

        # Fermer le document et quitter Word
        doc.Close(False)
        word_app.Quit()
