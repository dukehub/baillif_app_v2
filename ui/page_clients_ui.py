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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_page_clients(object):
    def setupUi(self, page_clients):
        if not page_clients.objectName():
            page_clients.setObjectName(u"page_clients")
        page_clients.resize(1121, 682)
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
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_header = QWidget(self.widget)
        self.widget_header.setObjectName(u"widget_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_header.sizePolicy().hasHeightForWidth())
        self.widget_header.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.le_find = QLineEdit(self.widget_header)
        self.le_find.setObjectName(u"le_find")
        self.le_find.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_find)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget_header)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView_client = QTableView(self.widget1)
        self.tableView_client.setObjectName(u"tableView_client")
        self.tableView_client.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_client.setAlternatingRowColors(True)
        self.tableView_client.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_client.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_client.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableView_client)

        self.frame = QFrame(self.widget1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        self.splitter.addWidget(self.widget1)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_client = QWidget()
        self.tab_client.setObjectName(u"tab_client")
        self.verticalLayout_4 = QVBoxLayout(self.tab_client)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.tab_client)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pb_add = QPushButton(self.frame_3)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(150, 24))
        self.pb_add.setMaximumSize(QSize(300, 32))
        self.pb_add.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon)
        self.pb_add.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.pb_add)

        self.pb_save = QPushButton(self.frame_3)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_save.setIcon(icon1)
        self.pb_save.setIconSize(QSize(24, 24))
        self.pb_save.setAutoDefault(True)
        self.pb_save.setFlat(False)

        self.horizontalLayout_11.addWidget(self.pb_save)

        self.pb_edit = QPushButton(self.frame_3)
        self.pb_edit.setObjectName(u"pb_edit")
        self.pb_edit.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_edit.setIcon(icon2)
        self.pb_edit.setIconSize(QSize(24, 24))
        self.pb_edit.setFlat(False)

        self.horizontalLayout_11.addWidget(self.pb_edit)

        self.pb_delete = QPushButton(self.frame_3)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_delete.setIcon(icon3)
        self.pb_delete.setIconSize(QSize(24, 24))
        self.pb_delete.setAutoDefault(True)
        self.pb_delete.setFlat(False)

        self.horizontalLayout_11.addWidget(self.pb_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.groupBox_2 = QGroupBox(self.tab_client)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(720, 0))
        self.groupBox_2.setMaximumSize(QSize(720, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.error_mobile = QLabel(self.groupBox_2)
        self.error_mobile.setObjectName(u"error_mobile")

        self.horizontalLayout_7.addWidget(self.error_mobile)

        self.le_mobile = QLineEdit(self.groupBox_2)
        self.le_mobile.setObjectName(u"le_mobile")

        self.horizontalLayout_7.addWidget(self.le_mobile)


        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.error_legal_status = QLabel(self.groupBox_2)
        self.error_legal_status.setObjectName(u"error_legal_status")

        self.horizontalLayout_4.addWidget(self.error_legal_status)

        self.cb_legal_status = QComboBox(self.groupBox_2)
        self.cb_legal_status.setObjectName(u"cb_legal_status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cb_legal_status.sizePolicy().hasHeightForWidth())
        self.cb_legal_status.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.cb_legal_status)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 2)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.error_full_name = QLabel(self.groupBox_2)
        self.error_full_name.setObjectName(u"error_full_name")

        self.horizontalLayout_5.addWidget(self.error_full_name)

        self.le_full_name = QLineEdit(self.groupBox_2)
        self.le_full_name.setObjectName(u"le_full_name")

        self.horizontalLayout_5.addWidget(self.le_full_name)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 2)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.error_phone = QLabel(self.groupBox_2)
        self.error_phone.setObjectName(u"error_phone")

        self.horizontalLayout_8.addWidget(self.error_phone)

        self.le_phone = QLineEdit(self.groupBox_2)
        self.le_phone.setObjectName(u"le_phone")

        self.horizontalLayout_8.addWidget(self.le_phone)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.error_mail = QLabel(self.groupBox_2)
        self.error_mail.setObjectName(u"error_mail")

        self.horizontalLayout_9.addWidget(self.error_mail)

        self.le_mail = QLineEdit(self.groupBox_2)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setMaxLength(32767)

        self.horizontalLayout_9.addWidget(self.le_mail)


        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 3, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.error_address = QLabel(self.groupBox_2)
        self.error_address.setObjectName(u"error_address")

        self.horizontalLayout_6.addWidget(self.error_address)

        self.le_address = QLineEdit(self.groupBox_2)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_6.addWidget(self.le_address)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.txe_notes = QTextEdit(self.groupBox_2)
        self.txe_notes.setObjectName(u"txe_notes")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txe_notes.sizePolicy().hasHeightForWidth())
        self.txe_notes.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.txe_notes)


        self.gridLayout.addLayout(self.horizontalLayout_10, 7, 1, 1, 3)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_client, "")
        self.tab_dossiers = QWidget()
        self.tab_dossiers.setObjectName(u"tab_dossiers")
        self.tabWidget.addTab(self.tab_dossiers, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout_3.addWidget(self.splitter)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_main)


        self.retranslateUi(page_clients)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_clients)
    # setupUi

    def retranslateUi(self, page_clients):
        page_clients.setWindowTitle(QCoreApplication.translate("page_clients", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_clients", u"\u0628\u062d\u062b", None))
        self.le_find.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pb_add.setText(QCoreApplication.translate("page_clients", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644", None))
        self.pb_save.setText("")
        self.pb_edit.setText("")
        self.pb_delete.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_11.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.error_mobile.setText("")
        self.le_mobile.setInputMask(QCoreApplication.translate("page_clients", u"9999 99 99 99", None))
        self.le_mobile.setPlaceholderText(QCoreApplication.translate("page_clients", u"9999 99 99 99", None))
        self.error_legal_status.setText("")
        self.cb_legal_status.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u062a\u062d\u0640\u062f\u064a\u062f \u0627\u0644\u0635\u0641\u0629 \u060c\u060c\u060c", None))
        self.label_9.setText(QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0623\u062e\u0631\u0649", None))
        self.error_full_name.setText("")
        self.le_full_name.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628 \u0623\u0648 \u0627\u0644\u0647\u064a\u0626\u0629 \u0627\u0644\u0645\u062e\u062a\u0635\u0629 \u060c\u060c\u060c", None))
        self.label_12.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0635\u0641\u0629", None))
        self.label_10.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.label_15.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_14.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.error_phone.setText("")
        self.le_phone.setInputMask(QCoreApplication.translate("page_clients", u"999 99 99 99", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("page_clients", u"xxx xx xx xx", None))
        self.label_13.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.error_mail.setText("")
        self.le_mail.setText("")
        self.le_mail.setPlaceholderText(QCoreApplication.translate("page_clients", u"personne@mail.com", None))
        self.error_address.setText("")
        self.label_8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_client), QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dossiers), QCoreApplication.translate("page_clients", u"\u0645\u062d\u0627\u0636\u0631 \u0627\u0644\u0639\u0645\u064a\u0644", None))
    # retranslateUi

