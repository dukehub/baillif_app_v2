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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QTableView, QVBoxLayout,
    QWidget)
import ui.resources_rc

class Ui_page_clients(object):
    def setupUi(self, page_clients):
        if not page_clients.objectName():
            page_clients.setObjectName(u"page_clients")
        page_clients.resize(1166, 753)
        self.verticalLayout_3 = QVBoxLayout(page_clients)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(page_clients)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame_6 = QFrame(self.splitter)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_header = QWidget(self.frame_6)
        self.widget_header.setObjectName(u"widget_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_header.sizePolicy().hasHeightForWidth())
        self.widget_header.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.le_find_clients = QLineEdit(self.widget_header)
        self.le_find_clients.setObjectName(u"le_find_clients")
        self.le_find_clients.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_find_clients)


        self.verticalLayout_6.addWidget(self.widget_header)

        self.tableView_client = QTableView(self.frame_6)
        self.tableView_client.setObjectName(u"tableView_client")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView_client.sizePolicy().hasHeightForWidth())
        self.tableView_client.setSizePolicy(sizePolicy2)
        self.tableView_client.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_client.setAlternatingRowColors(True)
        self.tableView_client.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_client.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_client.setSortingEnabled(True)

        self.verticalLayout_6.addWidget(self.tableView_client)

        self.splitter.addWidget(self.frame_6)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pb_add = QPushButton(self.frame_2)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(150, 24))
        self.pb_add.setMaximumSize(QSize(300, 32))
        self.pb_add.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon)
        self.pb_add.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.pb_add)

        self.pb_edit = QPushButton(self.frame_2)
        self.pb_edit.setObjectName(u"pb_edit")

        self.horizontalLayout_13.addWidget(self.pb_edit)

        self.pb_delete = QPushButton(self.frame_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.horizontalLayout_13.addWidget(self.pb_delete)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.gb_infos = QGroupBox(self.frame)
        self.gb_infos.setObjectName(u"gb_infos")
        self.gb_infos.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gb_infos.sizePolicy().hasHeightForWidth())
        self.gb_infos.setSizePolicy(sizePolicy3)
        self.gb_infos.setMinimumSize(QSize(720, 0))
        self.gb_infos.setFlat(False)
        self.gridLayout = QGridLayout(self.gb_infos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_phone = QLabel(self.gb_infos)
        self.lbl_phone.setObjectName(u"lbl_phone")

        self.gridLayout.addWidget(self.lbl_phone, 7, 0, 1, 1)

        self.lbl_full_name = QLabel(self.gb_infos)
        self.lbl_full_name.setObjectName(u"lbl_full_name")

        self.gridLayout.addWidget(self.lbl_full_name, 0, 2, 1, 1)

        self.lbl_legal_status = QLabel(self.gb_infos)
        self.lbl_legal_status.setObjectName(u"lbl_legal_status")

        self.gridLayout.addWidget(self.lbl_legal_status, 0, 0, 1, 1)

        self.lbl_mobile = QLabel(self.gb_infos)
        self.lbl_mobile.setObjectName(u"lbl_mobile")

        self.gridLayout.addWidget(self.lbl_mobile, 8, 0, 1, 1)

        self.lbl_address = QLabel(self.gb_infos)
        self.lbl_address.setObjectName(u"lbl_address")
        self.lbl_address.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_address, 6, 0, 1, 3)

        self.lbl_email = QLabel(self.gb_infos)
        self.lbl_email.setObjectName(u"lbl_email")

        self.gridLayout.addWidget(self.lbl_email, 9, 0, 1, 1)

        self.lbl_notes = QLabel(self.gb_infos)
        self.lbl_notes.setObjectName(u"lbl_notes")

        self.gridLayout.addWidget(self.lbl_notes, 7, 1, 3, 2)


        self.verticalLayout_2.addWidget(self.gb_infos)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_find_dossiers = QLineEdit(self.groupBox)
        self.le_find_dossiers.setObjectName(u"le_find_dossiers")

        self.verticalLayout.addWidget(self.le_find_dossiers)

        self.tableView_dossiers = QTableView(self.groupBox)
        self.tableView_dossiers.setObjectName(u"tableView_dossiers")

        self.verticalLayout.addWidget(self.tableView_dossiers)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.spinBox = QSpinBox(self.frame_3)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.splitter.addWidget(self.frame)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(page_clients)

        QMetaObject.connectSlotsByName(page_clients)
    # setupUi

    def retranslateUi(self, page_clients):
        page_clients.setWindowTitle(QCoreApplication.translate("page_clients", u"Form", None))
        self.le_find_clients.setPlaceholderText("")
        self.pb_add.setText(QCoreApplication.translate("page_clients", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644", None))
        self.pb_edit.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pb_delete.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.gb_infos.setTitle(QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.lbl_phone.setText("")
        self.lbl_full_name.setText("")
        self.lbl_legal_status.setText("")
        self.lbl_mobile.setText("")
        self.lbl_address.setText("")
        self.lbl_email.setText("")
        self.lbl_notes.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("page_clients", u"\u0645\u062d\u0627\u0636\u0631 \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.pushButton.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
    # retranslateUi

