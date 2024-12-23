from PySide6.QtCore import QObject, Signal, QDate, Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QComboBox, QTextEdit, QDateEdit, QTimeEdit, QLabel, QLineEdit, QCheckBox, QSpinBox, QDoubleSpinBox, QDateTimeEdit, QWidget, QHBoxLayout, QFormLayout
from abc import ABC, abstractmethod
from typing import List, Dict
from core import event_manager
import logging

# Ajout du logger en haut du fichier
logger = logging.getLogger(__name__)

class AbstractValidator(ABC):
    """Classe de base pour les validateurs"""
    
    def __init__(self, error_message: str):
        self.error_message = error_message
    
    @abstractmethod
    def validate(self, value: any) -> bool:
        """Valide une valeur"""
        pass

class NotEmptyValidator(AbstractValidator):
    """Validateur qui vérifie qu'une valeur n'est pas vide"""
    
    def __init__(self, error_message: str = "هذا الحقل إلزامي"):
        super().__init__(error_message)
    
    def validate(self, value: any) -> bool:
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        return bool(value)

class EmailValidator(AbstractValidator):
    """Validateur qui vérifie qu'une valeur est une adresse email valide"""
    
    def __init__(self, error_message: str = "عنوان البريد الإلكتروني غير صالح", optional: bool = False):
        super().__init__(error_message)
        self.optional = optional
    
    def validate(self, value: str) -> bool:
        if not value:
            return self.optional  # Retourne True si le champ est optionnel, False sinon
        return '@' in value and '.' in value.split('@')[1]

class ValidationRule:
    """Règle de validation pour un champ"""
    
    def __init__(self, field_name: str, validators: List[AbstractValidator]):
        self.field_name = field_name
        self.validators = validators
class SelectionValidator(AbstractValidator):
    """Validateur pour les ComboBox"""
    
    def __init__(self, error_message: str = "يجب اختيار قيمة من القائمة"):
        super().__init__(error_message)
    
    def validate(self, value: any) -> bool:
        combo = value
        current_index = combo.currentIndex()
        current_text = combo.currentText()
        
        # Vérifie si une valeur est sélectionnée
        if current_index == -1 or not current_text.strip():
            return False
            
        # Vérifie si la valeur existe dans les items
        all_items = [combo.itemText(i) for i in range(combo.count())]
        if current_text not in all_items:
            return False
            
        return True

class DateValidator(AbstractValidator):
    def __init__(self, error_message: str = "التاريخ غير صالح"):
        super().__init__(error_message)

    def validate(self, value: any) -> bool:
        return isinstance(value, QDate)
    
class FieldValueGetter:
    """Classe utilitaire pour récupérer la valeur d'un champ selon son type"""
    
    @staticmethod
    def get_value(widget: QWidget) -> any:
        """Récupère la valeur d'un widget selon son type"""
        if isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QTextEdit):
            return widget.toPlainText()
        elif isinstance(widget, QComboBox):
            return widget.currentText()
        elif isinstance(widget, QDateEdit):
            return widget.date()
        elif isinstance(widget, QTimeEdit):
            return widget.time()
        elif isinstance(widget, QDateTimeEdit):
            return widget.dateTime()
        elif isinstance(widget, QCheckBox):
            return widget.isChecked()
        elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
            return widget.value()
        return None

class ValidatorManager(QObject):
    """Gestionnaire de validation de formulaire"""
    
    validationStateChanged = Signal(bool)
    
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.validation_rules = []
        self.error_labels = {}
        self.validated_fields = set()  # Pour suivre les champs qui ont été validés
        
        # Chargement des icônes
        self.error_icon = QPixmap(":/icons/icons/high_importance.png")
        if self.error_icon.isNull():
            logger.error("Impossible de charger l'icône d'erreur")
        else:
            self.error_icon = self.error_icon.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Émettre les événements de validation via event_manager
        self.validationStateChanged.connect(
            lambda state: event_manager.emit('validation_state_changed', state)
        )

    def add_validation_rule(self, field_name: str, error_label_name: str, validators: List[AbstractValidator]):
        """Ajoute une règle de validation"""
        if not hasattr(self.ui, field_name):
            logger.warning(f"Le champ {field_name} n'existe pas")
            return
            
        widget = getattr(self.ui, field_name)
        
        # Trouve le label d'erreur correspondant
        error_label_name = error_label_name # Convertit 'le_full_name' en 'error_name'
        if hasattr(self.ui, error_label_name):
            error_label = getattr(self.ui, error_label_name)
            self.error_labels[field_name] = error_label
            
            # Configure le label d'erreur
            if not error_label.pixmap() or error_label.pixmap().isNull():
                error_label.setPixmap(self.error_icon)
            error_label.hide()
        else:
            logger.warning(f"Label d'erreur {error_label_name} non trouvé pour {field_name}")
            return
        
        self.validation_rules.append(ValidationRule(field_name, validators))
        
        # Connecte le validateur aux événements du widget
        self.connect_field_validators(widget)
    
    def _show_error(self, widget: QWidget, message: str):
        """Affiche une erreur pour un widget"""
        error_label = self.error_labels.get(widget.objectName())
        if error_label:
            if not error_label.pixmap() or error_label.pixmap().isNull():
                error_label.setPixmap(self.error_icon)
            error_label.setToolTip(message)
            error_label.show()
    
    def _clear_error(self, widget: QWidget):
        """Efface l'erreur pour un widget"""
        error_label = self.error_labels.get(widget.objectName())
        if error_label:
            error_label.hide()
            error_label.setToolTip("")

    def _validate_field(self, field_name: str) -> tuple[bool, list[str]]:
        """Valide un champ spécifique"""
        try:
            widget = getattr(self.ui, field_name)
            value = FieldValueGetter.get_value(widget)
            error_messages = []

            rule = next((r for r in self.validation_rules if r.field_name == field_name), None)
            if not rule:
                return True, []

            # Ajouter le champ à l'ensemble des champs validés
            self.validated_fields.add(field_name)

            # Vérifier si c'est un champ email optionnel vide
            is_optional_email = any(
                isinstance(validator, EmailValidator) and 
                validator.optional and 
                not value 
                for validator in rule.validators
            )

            # Si c'est un email optionnel vide, on le considère comme valide
            if is_optional_email:
                self._clear_error(widget)
            else:
                # Sinon on vérifie tous les validateurs
                for validator in rule.validators:
                    if not validator.validate(value):
                        error_messages.append(validator.error_message)

            if error_messages:
                self._show_error(widget, "\n".join(error_messages))
            else:
                self._clear_error(widget)

            # Vérifier si tous les champs sont valides
            all_fields_valid = True
            for validation_rule in self.validation_rules:
                field_widget = getattr(self.ui, validation_rule.field_name)
                error_label = self.error_labels.get(validation_rule.field_name)
                
                # Un champ est invalide si son label d'erreur est visible
                if error_label and error_label.isVisible():
                    all_fields_valid = False
                    break
                
                # Vérifier si c'est un champ obligatoire non vide
                field_value = FieldValueGetter.get_value(field_widget)
                has_required = any(isinstance(v, NotEmptyValidator) for v in validation_rule.validators)
                
                if has_required and not field_value:
                    all_fields_valid = False
                    break

            self.validationStateChanged.emit(all_fields_valid)
            return not bool(error_messages), error_messages

        except AttributeError as e:
            logger.error(f"Erreur d'attribut pour le champ {field_name}: {e}")
            return False, ["Erreur interne de validation"]

    def validate(self) -> tuple[bool, dict[str, list[str]]]:
        """Valide tous les champs"""
        logger.info("Début de la validation")
        is_valid = True
        all_errors = {}

        for rule in self.validation_rules:
            field_valid, errors = self._validate_field(rule.field_name)
            if not field_valid:
                is_valid = False
                all_errors[rule.field_name] = errors

        # Émettre le résultat de la validation complète
        event_manager.emit('form_validation_complete', {
            'is_valid': is_valid,
            'errors': all_errors
        })
        
        self.validationStateChanged.emit(is_valid)
        return is_valid, all_errors

    def connect_field_validators(self, widget):
        """Connecte les validateurs aux événements du widget"""
        if isinstance(widget, QLineEdit):
            widget.textChanged.connect(lambda: self._validate_field(widget.objectName()))
        elif isinstance(widget, QTextEdit):
            widget.textChanged.connect(lambda: self._validate_field(widget.objectName()))
        elif isinstance(widget, QComboBox):
            widget.currentIndexChanged.connect(lambda: self._validate_field(widget.objectName()))
        elif isinstance(widget, (QDateEdit, QTimeEdit, QDateTimeEdit)):
            widget.dateTimeChanged.connect(lambda: self._validate_field(widget.objectName()))
        elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
            widget.valueChanged.connect(lambda: self._validate_field(widget.objectName()))
        elif isinstance(widget, QCheckBox):
            widget.stateChanged.connect(lambda: self._validate_field(widget.objectName()))
        else:
            logger.warning(f"Type de widget non pris en charge pour la validation: {type(widget)}")

    def clear_validation(self):
        """Réinitialise l'état de validation"""
        self.validated_fields.clear()
        for error_label in self.error_labels.values():
            error_label.hide()
        self.validationStateChanged.emit(False)

class PriceValidator(AbstractValidator):
    """Validateur pour le prix"""
    
    def __init__(self, error_message: str = "يجب أن يكون السعر رقمًا موجبًا"):
        super().__init__(error_message)
    
    def validate(self, value: str) -> bool:
        try:
            price = float(value)
            return price > 0
        except ValueError:
            return False
