from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox
from PySide6.QtCore import QDate
from ui.page_rapport_ui import Ui_page_rapports
from controllers.widgets.FormAct import FormAct
from models.models import Bailiff
from models.DossiersTableModel import DossiersTableModel
from core import data_manager
from helpers.config import templates_dir
from helpers import generators
from services.print_manager import PrintManager
import tempfile, os, time, threading
from datetime import datetime
from io import BytesIO



class PageRapports(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_rapports()
        self.ui.setupUi(self)
        self.print_manager = PrintManager()
        
        self.dossiers_model = DossiersTableModel()
        self.ui.tableView_dossiers.setModel(self.dossiers_model)
       
        self.ui.tableView_dossiers.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableView_dossiers.horizontalHeader().setStretchLastSection(True)
        self.ui.le_filter.textChanged.connect(self.dossiers_model.filter_dossier)
        self.setup_signals()
        
    
    def setup_signals(self):
        self.ui.tb_new.clicked.connect(self.on_new_rapport_clicked)
        self.ui.tableView_dossiers.selectionModel().selectionChanged.connect(lambda: self.enable_buttons(self.ui.tableView_dossiers.selectionModel().hasSelection()))   
        self.ui.tableView_dossiers.doubleClicked.connect(self.open_act)
        self.ui.tb_edit.clicked.connect(self.open_act)
        self.ui.tb_preview.clicked.connect(self.preview_dossier)
        self.ui.tb_print.clicked.connect(self.print_dossier)
        self.ui.tb_delete.clicked.connect(self.delete_dossier)
        
    def on_new_rapport_clicked(self):
        dlg = FormAct()
        dlg.exec_()
    def enable_buttons(self, enable):
        self.ui.tb_delete.setEnabled(enable)
        self.ui.tb_edit.setEnabled(enable)
        self.ui.tb_preview.setEnabled(enable)
        self.ui.tb_print.setEnabled(enable)
    def load_dossier(self, selected):
         if selected.indexes():
            index = selected.indexes()[0]
            self.dossier = self.dossiers_model._dossiers[index.row()]
            self.set_form_dossier(self.dossier)
    
    def on_data_changed(self, data_type):
        
        if data_type == 'dossiers':
            self.dossiers_model.refresh()
                     

    def add_new_act(self):
        dlg = FormAct(dossier=None)
        dlg.exec_()

    def open_act(self):
        index = self.ui.tableView_dossiers.selectionModel().currentIndex()
        if not index.isValid():
            print("Aucun dossier selectionne")
            return
        selected_dossier = self.dossiers_model._dossiers[index.row()]
        dlg = FormAct(dossier=selected_dossier)
        dlg.exec()
            
        
    def export_dossier(self):
        index = self.ui.tableView_dossiers.selectionModel().currentIndex()
        if not index.isValid():
            print("Aucun dossier selectionne")
            return
        selected_dossier = self.dossiers_model._dossiers[index.row()]
        bailiff : Bailiff = data_manager.get_bailiff()
       

        dossier = data_manager.get_dossier_att_by_id(selected_dossier.id)
        template = os.path.join(templates_dir,dossier.document_path)
        
        
        fields = data_manager.get_fields_by_dossier_id(selected_dossier.id)    
        fields_map = {field.field_name: field.field_value for field in fields}
        law = f"القائم في حق {dossier.demandeur_nom} الساكن بـ {dossier.demandeur_adresse}...... مدعي"
        client_adresse= f"العنوان {dossier.client_adresse}...... مدعى عليه"
        defendeur = f"{dossier.defendeur_nom} الساكن بـ {dossier.defendeur_adresse}...... مدعى عليه"
        date_audience = datetime.strptime(fields_map.get("date_audience", ""), '%Y-%m-%d').strftime('%d-%m-%Y')
        date_registary = datetime.strptime(fields_map.get("date_registary", ""), '%Y-%m-%d').strftime('%d-%m-%Y')
       
        context = {
            "title": "محضـر تكليف بالحضـور للجلسة",
            "year": generators.generate_year(QDate.currentDate().year()),
            "bailiff_name": bailiff.nom,
            "bailiff_address": bailiff.address,
            "bailiff_register_in": bailiff.register_in,
            "bailiff_phone": bailiff.phone,
            "client": dossier.client_nom,
            "law": law if dossier.client_nom != dossier.demandeur_nom else client_adresse,
            "defendeur": defendeur,
            "tribunal": fields_map.get("tribunal", ""),      
            "section": fields_map.get("section", ""),
            "council": fields_map.get("council", ""),
            "room": fields_map.get("room", ""),
            "date_audience": date_audience,
            "hour_audience": fields_map.get("hour_audience", ""),
            "case_number": fields_map.get("case_number", ""),
            "code": dossier.code,
            "hall": fields_map.get("hall", ""),
            "mission": "كلفنا",
            
            
        }
        context_2 = context.copy()
        context_2["title"] =  "محضـر تسليم تكليف بالحضـور للجلسة"
        context_2["mission"] = "بلغنا و سلمنا لـ"
        context_2["signature"] = "إمضاء أو بصمة المستلم"
        context_2["registary_reg"] = ":حيث كنـا مخاطبين مع"
        context_2["registary"] = "نسخـة من التكليف بالحضور مرفقا بنسخة من عريضة المؤشر عليها مـن طرف امانة ضبط"
        context_2["tribunal_registary"] = f'محكمة {fields_map.get("tribunal_registary", "")}'
        context_2["council_registary"] = f'مجلس {fields_map.get("council_registary", "")}'
        context_2["date_registary"] = date_registary
        contexts = [context, context_2]
        output_stream = BytesIO()
        output_stream = generators.generate_document(template, contexts,output_stream)
        
       
        return output_stream

    def print_dossier(self):
        """
            Prépare un fichier temporaire et lance l'impression avec une boîte de dialogue.
        """
        # Exporter le dossier (génération du contenu DOCX dans un flux binaire)
        fileIO = self.export_dossier()

        if not fileIO:
            print("Erreur : Impossible d'exporter le dossier.")
            return

        # Créer un fichier temporaire pour stocker le contenu du document
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
            tmp_file.write(fileIO.getvalue())  # Écrire le contenu du fichier dans le fichier temporaire
            temp_file_path = tmp_file.name  # Chemin du fichier temporaire
        
        try:
            # Utiliser le gestionnaire d'impression pour imprimer le fichier
            self.print_manager.print_with_dialog(temp_file_path)
        finally:
            # Nettoyer : Supprimer le fichier temporaire après utilisation
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
        
        

    def preview_dossier(self):
        fileIO = self.export_dossier()
        if not fileIO:
            print("Erreur : Impossible d'exporter le dossier.")
            return

        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
            tmp_file.write(fileIO.getvalue())
            temp_file_path = tmp_file.name

        def delete_file_later(path, delay=10):
            time.sleep(delay)  # Attendre avant de supprimer
            if os.path.exists(path):
                os.remove(path)
                print(f"Fichier temporaire supprimé automatiquement : {path}")

        try:
            os.startfile(temp_file_path)  # Ouvre le fichier avec l'application par défaut
            threading.Thread(target=delete_file_later, args=(temp_file_path,), daemon=True).start()
        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier : {e}")


    def delete_dossier(self):
        index = self.ui.tableView_dossiers.selectionModel().currentIndex()
        if index.isValid():
            selected_dossier_id = self.dossiers_model._dossiers[index.row()].id
            reply = QMessageBox.question(self, "تأكيد", "هل تريد حذف هذا الملف؟", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                data_manager.delete_dossier(selected_dossier_id)
            else:
                print("Deletion cancelled")
        else:
            print("Aucun dossier sélectionné")

        
        
   
        
    

    def next_page(self):
        if self.dossiers_model.current_page < self.dossiers_model.total_pages() - 1:
            self.dossiers_model.setPage(self.dossiers_model.current_page + 1)

    def previous_page(self):
        if self.dossiers_model.current_page > 0:
            self.dossiers_model.setPage(self.dossiers_model.current_page - 1)
        