from PySide6.QtWidgets import QWidget
from ui.page_rapport_ui import Ui_page_rapports
from controllers.widgets.FormAct import FormAct
from core import data_manager, state_manager



class PageRapports(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_rapports()
        self.ui.setupUi(self)
        
        self.setup_signals()
        
    
    def setup_signals(self):
        self.ui.tb_new.clicked.connect(self.on_new_rapport_clicked)
        
    def on_new_rapport_clicked(self):
        dlg = FormAct()
        dlg.exec_()
        