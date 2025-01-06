from PySide6.QtWidgets import QWidget, QDialog, QMessageBox, QHeaderView
from ui.page_archives_ui import Ui_page_archives
from core import data_manager
from services.print_manager import PrintManager
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Qt, QPoint, QUrl
from models.ArchiveTreeModel import ArchiveTreeModel
from controllers.widgets.FormArchive import FormArchive
from controllers.widgets.formes import FormBox
from helpers.config import archive_dir
import os, sys
from PySide6.QtCore import Slot

class PageArchives(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_page_archives()
        self.ui.setupUi(self)
        self.data_manager = data_manager
        self.print_manager = PrintManager(self)
   
        self.dossier = None
        self.m_document = QPdfDocument(self)
        self.ui.pdf_viewer.setDocument(self.m_document)
        
        self.ui.tb_add_archive.clicked.connect(self.add_archive)
        self.ui.tb_add_box.clicked.connect(self.add_box)
        self.archive_model = ArchiveTreeModel(self.data_manager)
        self.ui.tree_view_pdf.setModel(self.archive_model)

        self.ui.pdf_viewer.setPageMode(QPdfView.PageMode.MultiPage)
       
  
       
        self.ui.tree_view_pdf.setWordWrap(True)
        self.ui.tree_view_pdf.setUniformRowHeights(True)
        self.ui.tree_view_pdf.setTextElideMode(Qt.ElideNone)
        self.ui.tree_view_pdf.header().setStretchLastSection(True)
        self.ui.tree_view_pdf.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tree_view_pdf.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        
        
        self.ui.tree_view_pdf.selectionModel().selectionChanged.connect(self.update_pdf_view)
        self.ui.tb_print.clicked.connect(self.print)
        self.ui.tb_delete_archive.clicked.connect(self.delete_archive)
        self.ui.le_filter.textChanged.connect(self.filter_archives)
    def add_archive(self):
        """
        Affiche une bo te de dialogue pour l'ajout d'un archive.
        """
    
        dlg = FormArchive()
        dlg.exec()
            
 
    def add_box(self):
        """
        Affiche une bo te de dialogue pour l'ajout d'une box.
        """
        dlg = FormBox()
        dlg.exec()

    def delete_archive(self):
        
        self.dossier.path_file = None
        self.dossier.archive_box_id = None
        self.dossier.date_accus = None
        self.dossier.archive_status = False
        self.dossier.valid_status = False
        self.dossier.num_archive = None
        self.dossier.honoraires = None
        self.dossier.uplaod_at = None    
        self.data_manager.update_dossier(self.dossier)


    def update_pdf_view(self, selected):
        indexes = selected.indexes()
        
        if indexes:
            selected_item = indexes[1]
           
            if self.archive_model.get_hidden_data(selected_item,"full_data"):
                self.dossier = self.archive_model.get_hidden_data(selected_item,"full_data")
                
                path = os.path.join(archive_dir,self.dossier.path_file)
                
                self.open(QUrl.fromLocalFile(path))
                self.ui.tb_delete_archive.setEnabled(True)
                self.ui.tb_print.setEnabled(True)
            else:
                self.ui.tb_delete_archive.setEnabled(False)
                self.ui.tb_print.setEnabled(False)

    def open(self, doc_location):
        if doc_location.isLocalFile():
            self.m_document.load(doc_location.toLocalFile())

            document_title = self.m_document.metaData(QPdfDocument.MetaDataField.Title)

            self.page_selected(0)
            self.ui.tb_print.setEnabled(True)
        else:
            message = self.tr(f"{doc_location} n'est pas un fichier valid.")
            print(message, file=sys.stderr)
            QMessageBox.critical(self, self.tr("Echec d'ouverture"), message)
    @Slot(int)
    def page_selected(self, page):
        nav = self.ui.pdf_viewer.pageNavigator()
        nav.jump(page, QPoint(), nav.currentZoom())
    
    def print(self):
        path = os.path.join(archive_dir,self.dossier.path_file)
        self.print_manager.print_with_dialog( path)
    
    def filter_archives(self):
        """Filtre les archives selon le texte de recherche"""
        search_text = self.ui.le_filter.text()
        self.archive_model.filter_archives(search_text, self.ui.tree_view_pdf)
