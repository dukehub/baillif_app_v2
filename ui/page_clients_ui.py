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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QTableView, QVBoxLayout,
    QWidget)
import ui.resources_rc

class Ui_page_clients(object):
    def setupUi(self, page_clients):
        if not page_clients.objectName():
            page_clients.setObjectName(u"page_clients")
        page_clients.resize(1061, 663)
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
        self.tableView_client.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView_client.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_client.setAlternatingRowColors(True)
        self.tableView_client.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_client.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_client.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tableView_client.setSortingEnabled(True)
        self.tableView_client.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_client.horizontalHeader().setMinimumSectionSize(100)
        self.tableView_client.horizontalHeader().setDefaultSectionSize(120)
        self.tableView_client.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableView_client.horizontalHeader().setStretchLastSection(True)
        self.tableView_client.verticalHeader().setCascadingSectionResizes(True)
        self.tableView_client.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableView_client.verticalHeader().setStretchLastSection(False)

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
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.pb_add = QPushButton(self.frame_2)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(150, 0))
        self.pb_add.setMaximumSize(QSize(16777215, 16777215))
        self.pb_add.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon)
        self.pb_add.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.pb_add)

        self.pb_edit = QPushButton(self.frame_2)
        self.pb_edit.setObjectName(u"pb_edit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit.setIcon(icon1)

        self.horizontalLayout_13.addWidget(self.pb_edit)

        self.pb_delete = QPushButton(self.frame_2)
        self.pb_delete.setObjectName(u"pb_delete")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_delete.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.pb_delete)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_find_dossiers = QLineEdit(self.groupBox)
        self.le_find_dossiers.setObjectName(u"le_find_dossiers")
        self.le_find_dossiers.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_find_dossiers)

        self.tableView_dossiers = QTableView(self.groupBox)
        self.tableView_dossiers.setObjectName(u"tableView_dossiers")
        self.tableView_dossiers.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView_dossiers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_dossiers.setAlternatingRowColors(True)
        self.tableView_dossiers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_dossiers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_dossiers.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tableView_dossiers.setSortingEnabled(True)
        self.tableView_dossiers.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_dossiers.horizontalHeader().setHighlightSections(True)
        self.tableView_dossiers.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableView_dossiers.horizontalHeader().setStretchLastSection(False)
        self.tableView_dossiers.verticalHeader().setCascadingSectionResizes(True)
        self.tableView_dossiers.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableView_dossiers.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableView_dossiers)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.gb_infos = QGroupBox(self.frame_4)
        self.gb_infos.setObjectName(u"gb_infos")
        self.gb_infos.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gb_infos.sizePolicy().hasHeightForWidth())
        self.gb_infos.setSizePolicy(sizePolicy3)
        self.gb_infos.setMinimumSize(QSize(300, 0))
        self.gb_infos.setMaximumSize(QSize(300, 16777215))
        self.gb_infos.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.gb_infos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.gb_infos)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_4.addWidget(self.label)

        self.lbl_legal_status = QLabel(self.gb_infos)
        self.lbl_legal_status.setObjectName(u"lbl_legal_status")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_legal_status.setFont(font1)
        self.lbl_legal_status.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.lbl_legal_status)

        self.label_3 = QLabel(self.gb_infos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_4.addWidget(self.label_3)

        self.lbl_full_name = QLabel(self.gb_infos)
        self.lbl_full_name.setObjectName(u"lbl_full_name")
        self.lbl_full_name.setFont(font1)
        self.lbl_full_name.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.lbl_full_name)

        self.label_2 = QLabel(self.gb_infos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_4.addWidget(self.label_2)

        self.lbl_address = QLabel(self.gb_infos)
        self.lbl_address.setObjectName(u"lbl_address")
        self.lbl_address.setFont(font1)
        self.lbl_address.setFrameShape(QFrame.Shape.Box)
        self.lbl_address.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lbl_address)

        self.label_4 = QLabel(self.gb_infos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.lbl_phone = QLabel(self.gb_infos)
        self.lbl_phone.setObjectName(u"lbl_phone")
        self.lbl_phone.setFont(font1)
        self.lbl_phone.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.lbl_phone)

        self.label_5 = QLabel(self.gb_infos)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lbl_mobile = QLabel(self.gb_infos)
        self.lbl_mobile.setObjectName(u"lbl_mobile")
        self.lbl_mobile.setFont(font1)
        self.lbl_mobile.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.lbl_mobile)

        self.label_6 = QLabel(self.gb_infos)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.lbl_email = QLabel(self.gb_infos)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setFont(font1)
        self.lbl_email.setFrameShape(QFrame.Shape.Box)

        self.verticalLayout_4.addWidget(self.lbl_email)

        self.label_7 = QLabel(self.gb_infos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_4.addWidget(self.label_7)

        self.lbl_notes = QLabel(self.gb_infos)
        self.lbl_notes.setObjectName(u"lbl_notes")
        self.lbl_notes.setFont(font1)
        self.lbl_notes.setFrameShape(QFrame.Shape.Box)
        self.lbl_notes.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lbl_notes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.gb_infos)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.splitter.addWidget(self.frame)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(page_clients)

        QMetaObject.connectSlotsByName(page_clients)
    # setupUi

    def retranslateUi(self, page_clients):
        page_clients.setWindowTitle(QCoreApplication.translate("page_clients", u"Form", None))
        self.le_find_clients.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u0628\u062d\u062b...", None))
        self.pb_add.setText(QCoreApplication.translate("page_clients", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644", None))
        self.pb_edit.setText("")
        self.pb_delete.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("page_clients", u"\u0645\u062d\u0627\u0636\u0631 \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.le_find_dossiers.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u0628\u062d\u062b...", None))
        self.pushButton.setText(QCoreApplication.translate("page_clients", u"<<", None))
        self.pushButton_2.setText(QCoreApplication.translate("page_clients", u">>", None))
        self.gb_infos.setTitle(QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0635\u0641\u0629", None))
        self.lbl_legal_status.setText("")
        self.label_3.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.lbl_full_name.setText("")
        self.label_2.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.lbl_address.setText("")
        self.label_4.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.lbl_phone.setText("")
        self.label_5.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.lbl_mobile.setText("")
        self.label_6.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.lbl_email.setText("")
        self.label_7.setText(QCoreApplication.translate("page_clients", u"\u0645\u0644\u0627\u062d\u0638\u0627\u062a", None))
        self.lbl_notes.setText("")
    # retranslateUi

