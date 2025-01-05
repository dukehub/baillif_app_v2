from PySide6.QtWidgets import QDialog, QLineEdit, QLabel, QDialogButtonBox, QVBoxLayout
from core import data_manager
from core.validators import ValidatorManager, NotEmptyValidator
from models.models import ArchiveBox


class FormBox(QDialog):
    def __init__(self):
        super().__init__()
        self.data_manager = data_manager
        self.le_num_box = QLineEdit()
        self.error_num_box = QLabel()
        self.le_num_box.setPlaceholderText("رقم العلبة")
        self.le_description = QLineEdit()
        self.le_description.setPlaceholderText("الوصف")
        # QDialogButtonBox pour les boutons OK et Annuler
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        ok_button = self.button_box.button(QDialogButtonBox.Ok)
        cancel_button = self.button_box.button(QDialogButtonBox.Cancel)
        ok_button.setText("موافق")
        cancel_button.setText("إلغاء")
        layout = QVBoxLayout()
        layout.addWidget(self.le_num_box)
        layout.addWidget(self.error_num_box)
        layout.addWidget(self.le_description)
        layout.addWidget(self.button_box)
        self.setLayout(layout)
        ok_button.setDisabled(True)
        self.button_box.accepted.connect(self.accept)  # OK
        self.button_box.rejected.connect(self.reject)  # Annuler
        self.validator_manager = ValidatorManager(self)
        self.validator_manager.add_validation_rule("le_num_box", "error_num_box", [NotEmptyValidator()])
        self.setWindowTitle("إضافة علبة جديدة")
        self.le_num_box.textChanged.connect(lambda: self.validator_manager._validate_field("le_num_box"))
        self.validator_manager.validationStateChanged.connect(lambda valid: ok_button.setEnabled(valid))

    def accept(self):
        if self.validator_manager.validate():
            box = ArchiveBox()
            box.name = self.le_num_box.text().strip()
            box.description = self.le_description.text().strip()
            data_manager.add_archive_box(box)

    def reject(self):
        super().reject()
          
            