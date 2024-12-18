from PySide6.QtWidgets import QLineEdit
import re
class NumberFormatLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textChanged.connect(self.format_number)

    def format_number(self):
        # Obtenir le texte actuel de l'utilisateur
        text = self.text().replace(" ", "")  # Supprimer les espaces
        if not text:
            return

        try:
            # Séparer la partie entière et décimale
            if "." in text:
                parts = text.split(".")
                integer_part = parts[0]
                decimal_part = parts[1][:2]  # Limiter à 2 décimales
            else:
                integer_part = text
                decimal_part = ""

            # Ajouter des espaces pour les milliers dans la partie entière
            integer_part = re.sub(r"(?<=\d)(?=(\d{3})+$)", " ", integer_part)

            # Reformater le texte
            if decimal_part:
                formatted_text = f"{integer_part}.{decimal_part}"
            else:
                formatted_text = integer_part

            # Mettre à jour le texte affiché
            self.blockSignals(True)
            self.setText(formatted_text)
            self.blockSignals(False)

        except ValueError:
            # Ne rien faire en cas d'erreur de formatage
            pass

