from PySide6.QtWidgets import QDialog
from ui.widgets.form_settings_ui import Ui_SettingsDialog
from models.models import Bailiff, Templates
from core import data_manager, state_manager
class FormSettings(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.data_manager = data_manager
       
        self.ui.setupUi(self)
        self.load_settings()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_bailiff)
        self.ui.tb_bailiff_info.setChecked(True)
        self.ui.tb_bailiff_info.clicked.connect(self.show_bailiff_info)
        self.ui.tb_users.clicked.connect(self.show_users)
        
       

        self.ui.pb_save.clicked.connect(self.save_settings)
        self.ui.pb_cancel.clicked.connect(self.cancel_settings)

        
    def show_bailiff_info(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_bailiff)
    def show_users(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_users)
    

    def save_settings(self):
        bailiff : Bailiff = self.data_manager.get_bailiff()
        if bailiff:
            bailiff.nom = self.ui.le_name.text()
            bailiff.register_in = self.ui.le_register_in.text()
            bailiff.address = self.ui.le_address.text()
            bailiff.phone = self.ui.le_phone.text()
            bailiff.mobile = self.ui.le_mobile.text()
            bailiff.email = self.ui.le_email.text()
            self.data_manager.update_bailiff(bailiff)
        else:
            bailiff = Bailiff(
                nom=self.ui.le_name.text(),
                register_in=self.ui.le_register_in.text(),
                address=self.ui.le_address.text(),
                phone=self.ui.le_phone.text(),
                mobile=self.ui.le_mobile.text(),
                email=self.ui.le_email.text(),
            )
            self.data_manager.add_bailiff(bailiff)
    def cancel_settings(self):
        self.close()


    def load_settings(self):
        builiff : Bailiff = self.data_manager.get_bailiff()
        if builiff:
            self.ui.le_name.setText(builiff.nom)
            self.ui.le_register_in.setText(builiff.register_in)
            self.ui.le_address.setText(builiff.address)
            self.ui.le_phone.setText(builiff.phone)
            self.ui.le_mobile.setText(builiff.mobile)
            self.ui.le_email.setText(builiff.email)
    
    
    def on_data_changed(self, data_type):
        if data_type == 'bailiffs':
            self.load_settings()