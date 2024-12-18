# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_clients.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_page_clients(object):
    def setupUi(self, page_clients):
        if not page_clients.objectName():
            page_clients.setObjectName(u"page_clients")
        page_clients.resize(962, 495)
        self.horizontalLayout = QHBoxLayout(page_clients)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_main = QWidget(page_clients)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_main)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.widget_header = QWidget(self.widget)
        self.widget_header.setObjectName(u"widget_header")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.le_find = QLineEdit(self.widget_header)
        self.le_find.setObjectName(u"le_find")
        self.le_find.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_find)

        self.pb_edit = QPushButton(self.widget_header)
        self.pb_edit.setObjectName(u"pb_edit")
        icon = QIcon()
        icon.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit.setIcon(icon)
        self.pb_edit.setIconSize(QSize(24, 24))
        self.pb_edit.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pb_edit)

        self.pb_delete = QPushButton(self.widget_header)
        self.pb_delete.setObjectName(u"pb_delete")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_delete.setIcon(icon1)
        self.pb_delete.setIconSize(QSize(24, 24))
        self.pb_delete.setAutoDefault(True)
        self.pb_delete.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pb_delete)

        self.pb_add = QPushButton(self.widget_header)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(150, 24))
        self.pb_add.setMaximumSize(QSize(300, 32))
        self.pb_add.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon2)
        self.pb_add.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pb_add)


        self.verticalLayout.addWidget(self.widget_header)

        self.tableView_client = QTableView(self.widget)
        self.tableView_client.setObjectName(u"tableView_client")
        self.tableView_client.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_client.setAlternatingRowColors(True)
        self.tableView_client.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_client.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_client.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableView_client)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_main)


        self.retranslateUi(page_clients)

        QMetaObject.connectSlotsByName(page_clients)
    # setupUi

    def retranslateUi(self, page_clients):
        page_clients.setWindowTitle(QCoreApplication.translate("page_clients", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_clients", u"\u0628\u062d\u062b", None))
        self.le_find.setPlaceholderText("")
        self.pb_edit.setText("")
        self.pb_delete.setText("")
        self.pb_add.setText(QCoreApplication.translate("page_clients", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644", None))
    # retranslateUi

