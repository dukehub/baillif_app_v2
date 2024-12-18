from PySide6.QtCore import QObject, Signal, QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QComboBox, QTextEdit, QDateEdit, QTimeEdit, QLabel, QLineEdit, QCheckBox, QSpinBox, QDoubleSpinBox, QDateTimeEdit
from abc import ABC, abstractmethod
from typing import List, Dict
import logging
from services.data_manager import DataManager

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
data_manager = DataManager()
class AbstractValidator(ABC):
    def __init__(self, error_message: str):
        self.error_message = error_message

    @abstractmethod
    def validate(self, value) -> bool:
        pass

class NotEmptyValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Ce champ ne peut pas être vide")

    def validate(self, value):
        return bool(value)
class NotExistsValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Cette valeur n'existe pas")

 

class EmailValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Adresse email invalide")

    def validate(self, value):
        return '@' in value and '.' in value

class DateValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Date invalide")

    def validate(self, value):
        return isinstance(value, QDate)

class SelectionValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Veuillez sélectionner une option valide")
        self.combo_box = None

    def validate(self, value):
        if self.combo_box is None:
            return True
        return self.combo_box.currentIndex() != -1

class SelectionEditValidator(AbstractValidator):
    def __init__(self):
        super().__init__("Veuillez sélectionner ou entrer une option valide")
        self.combo_box = None

    def validate(self, value):
        if self.combo_box is None:
            return True
        return value in [self.combo_box.itemText(i) for i in range(self.combo_box.count())]

class ValidationRule:
    def __init__(self, field_name: str, error_label: str, validators: List[AbstractValidator]):
        self.field_name = field_name
        self.error_label = error_label
        self.validators = validators

class FieldValueGetter:
    @staticmethod
    def get_value(widget):
        if isinstance(widget, QComboBox):
            return widget.currentText()
        elif isinstance(widget, QTextEdit):
            return widget.toPlainText()
        elif isinstance(widget, QDateEdit):
            return widget.date()
        elif isinstance(widget, QTimeEdit):
            return widget.time()
        elif hasattr(widget, 'text'):
            return widget.text()
        else:
            return ""

class ValidatorManager(QObject):
    validationStateChanged = Signal(bool)

    def __init__(self, ui, error_icon_path=":/icons/icons/exclamation_mark.png"):
        super().__init__()
        self.error_icon_red = QPixmap(error_icon_path)
        if self.error_icon_red.isNull():
            logger.error(f"Impossible de charger l'icône d'erreur: {error_icon_path}")
        else:
            self.error_icon_red = self.error_icon_red.scaled(20, 20)
        self.ui = ui
        self.validation_rules = []

    def add_validation_rule(self, field_name: str, error_label: str, validators: List[AbstractValidator]):
        rule = ValidationRule(field_name, error_label, validators)
        self.validation_rules.append(rule)
        logger.debug(f"Règle de validation ajoutée pour le champ: {field_name}")

    def remove_validation_rule(self, field_name):
        self.validation_rules = [r for r in self.validation_rules if r.field_name != field_name]

    def _clear_error(self, error_label_widget):
        if isinstance(error_label_widget, QLabel):
            error_label_widget.clear()
            error_label_widget.setToolTip("")
            logger.debug(f"Erreur effacée pour le label: {error_label_widget.objectName()}")
        else:
            logger.warning(f"Le widget d'erreur n'est pas un QLabel: {type(error_label_widget)}")

    def _set_error(self, error_label_widget, error_messages):
        if isinstance(error_label_widget, QLabel):
            error_label_widget.setPixmap(self.error_icon_red)
            error_label_widget.setToolTip("\n".join(error_messages))
            logger.debug(f"Erreur définie pour le label: {error_label_widget.objectName()} avec messages: {error_messages}")
        else:
            logger.warning(f"Le widget d'erreur n'est pas un QLabel: {type(error_label_widget)}")

    def validate(self) -> tuple[bool, dict[str, list[str]]]:
        logger.info("Début de la validation")
        is_valid = True
        errors = {}

        for rule in self.validation_rules:
            field_is_valid, field_errors = self._validate_field(rule)
            if not field_is_valid:
                is_valid = False
                errors[rule.field_name] = field_errors

        logger.info(f"Validation terminée. Résultat: {'Valide' if is_valid else 'Invalide'}")
        self.validationStateChanged.emit(is_valid)
        return is_valid, errors

    def _validate_field(self, rule):
        try:
            widget = getattr(self.ui, rule.field_name)
            error_label_widget = getattr(self.ui, rule.error_label)
            
            field_value = FieldValueGetter.get_value(widget)
            
            error_messages = []
            for validator in rule.validators:
                if isinstance(validator, (SelectionValidator, SelectionEditValidator)) and isinstance(widget, QComboBox):
                    validator.combo_box = widget
                if not validator.validate(field_value):
                    error_messages.append(validator.error_message)

            if error_messages:
                self._set_error(error_label_widget, error_messages)
                #widget.setStyleSheet("border: 2px solid red;")
                return False, error_messages
            else:
                self._clear_error(error_label_widget)
                widget.setStyleSheet("")
                return True, []

        except AttributeError as e:
            logger.error(f"Erreur d'attribut pour le champ {rule.field_name}: {e}")
            return False, [str(e)]

    def connect_real_time_validation(self):
        """
        Connecte la validation en temps réel pour tous les champs configurés.
        """
        for rule in self.validation_rules:
            widget = getattr(self.ui, rule.field_name, None)
            if widget:
                self._connect_widget_validation(widget)
            else:
                logger.warning(f"Widget non trouvé pour le champ: {rule.field_name}")

    def _connect_widget_validation(self, widget):
        """
        Connecte le signal approprié pour la validation en temps réel en fonction du type de widget.
        """
        if isinstance(widget, QComboBox):
            widget.currentTextChanged.connect(self.validate)
        elif isinstance(widget, QLineEdit):
            widget.textChanged.connect(self.validate)
        elif isinstance(widget, QTextEdit):
            widget.textChanged.connect(self.validate)
        elif isinstance(widget, QDateEdit):
            widget.dateChanged.connect(self.validate)
        elif isinstance(widget, QTimeEdit):
            widget.timeChanged.connect(self.validate)
        elif isinstance(widget, QDateTimeEdit):
            widget.dateTimeChanged.connect(self.validate)
        elif isinstance(widget, QSpinBox) or isinstance(widget, QDoubleSpinBox):
            widget.valueChanged.connect(self.validate)
        elif isinstance(widget, QCheckBox):
            widget.stateChanged.connect(self.validate)
        else:
            logger.warning(f"Type de widget non pris en charge pour la validation: {type(widget)}")
   
