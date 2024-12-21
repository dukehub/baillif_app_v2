from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

class Ui_PageClients(QWidget):
    def setupUi(self, PageClients):
        # Layout principal
        self.main_layout = QVBoxLayout(PageClients)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Barre de recherche et filtres
        self.search_frame = QFrame()
        self.search_layout = QHBoxLayout(self.search_frame)
        
        self.le_search = QLineEdit()
        self.le_search.setPlaceholderText("البحث عن عميل...")
        
        self.cb_filter_type = QComboBox()
        self.cb_filter_type.addItem("كل الأنواع")
        
        self.pb_add_client = QPushButton()
        self.pb_add_client.setIcon(QIcon(":/icons/icons/add_white.svg"))
        self.pb_add_client.setText("إضافة عميل")
        
        self.search_layout.addWidget(self.le_search)
        self.search_layout.addWidget(self.cb_filter_type)
        self.search_layout.addWidget(self.pb_add_client)
        
        # Table des clients
        self.table_clients = QTableWidget()
        self.table_clients.setColumnCount(7)
        headers = ["الاسم", "النوع", "العنوان", "البريد الإلكتروني", 
                  "الهاتف", "عدد الملفات", "العمليات"]
        self.table_clients.setHorizontalHeaderLabels(headers)
        self.table_clients.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Ajout des widgets au layout principal
        self.main_layout.addWidget(self.search_frame)
        self.main_layout.addWidget(self.table_clients) 