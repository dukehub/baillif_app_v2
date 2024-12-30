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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QTabWidget, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
import ui.resources_rc

class Ui_page_clients(object):
    def setupUi(self, page_clients):
        if not page_clients.objectName():
            page_clients.setObjectName(u"page_clients")
        page_clients.resize(1433, 871)
        self.verticalLayout_2 = QVBoxLayout(page_clients)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(page_clients)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame_6 = QFrame(self.splitter)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_header = QWidget(self.frame_6)
        self.widget_header.setObjectName(u"widget_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_header.sizePolicy().hasHeightForWidth())
        self.widget_header.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.le_find = QLineEdit(self.widget_header)
        self.le_find.setObjectName(u"le_find")
        self.le_find.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.le_find)

        self.pb_add = QPushButton(self.widget_header)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setMinimumSize(QSize(150, 24))
        self.pb_add.setMaximumSize(QSize(300, 32))
        self.pb_add.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add.setIcon(icon)
        self.pb_add.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pb_add)


        self.verticalLayout_6.addWidget(self.widget_header)

        self.tableView_client = QTableView(self.frame_6)
        self.tableView_client.setObjectName(u"tableView_client")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView_client.sizePolicy().hasHeightForWidth())
        self.tableView_client.setSizePolicy(sizePolicy3)
        self.tableView_client.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_client.setAlternatingRowColors(True)
        self.tableView_client.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_client.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_client.setSortingEnabled(True)

        self.verticalLayout_6.addWidget(self.tableView_client)

        self.splitter.addWidget(self.frame_6)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tab_client = QWidget()
        self.tab_client.setObjectName(u"tab_client")
        self.verticalLayout_5 = QVBoxLayout(self.tab_client)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.tab_client)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setMinimumSize(QSize(720, 0))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.error_address = QLabel(self.frame_3)
        self.error_address.setObjectName(u"error_address")

        self.horizontalLayout_5.addWidget(self.error_address)

        self.le_address = QLineEdit(self.frame_3)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_5.addWidget(self.le_address)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.error_mobile = QLabel(self.frame_3)
        self.error_mobile.setObjectName(u"error_mobile")

        self.horizontalLayout_7.addWidget(self.error_mobile)

        self.le_mobile = QLineEdit(self.frame_3)
        self.le_mobile.setObjectName(u"le_mobile")

        self.horizontalLayout_7.addWidget(self.le_mobile)


        self.gridLayout.addLayout(self.horizontalLayout_7, 9, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.error_notes = QLabel(self.frame_3)
        self.error_notes.setObjectName(u"error_notes")
        sizePolicy5.setHeightForWidth(self.error_notes.sizePolicy().hasHeightForWidth())
        self.error_notes.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.error_notes)

        self.txe_notes = QTextEdit(self.frame_3)
        self.txe_notes.setObjectName(u"txe_notes")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txe_notes.sizePolicy().hasHeightForWidth())
        self.txe_notes.setSizePolicy(sizePolicy6)
        self.txe_notes.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txe_notes.setLineWrapMode(QTextEdit.LineWrapMode.FixedColumnWidth)

        self.horizontalLayout_9.addWidget(self.txe_notes)


        self.gridLayout.addLayout(self.horizontalLayout_9, 13, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.error_mail = QLabel(self.frame_3)
        self.error_mail.setObjectName(u"error_mail")

        self.horizontalLayout_3.addWidget(self.error_mail)

        self.le_mail = QLineEdit(self.frame_3)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setMaxLength(32767)

        self.horizontalLayout_3.addWidget(self.le_mail)


        self.gridLayout.addLayout(self.horizontalLayout_3, 11, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.error_phone = QLabel(self.frame_3)
        self.error_phone.setObjectName(u"error_phone")

        self.horizontalLayout_6.addWidget(self.error_phone)

        self.le_phone = QLineEdit(self.frame_3)
        self.le_phone.setObjectName(u"le_phone")

        self.horizontalLayout_6.addWidget(self.le_phone)


        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.error_full_name = QLabel(self.frame_3)
        self.error_full_name.setObjectName(u"error_full_name")

        self.horizontalLayout_4.addWidget(self.error_full_name)

        self.le_full_name = QLineEdit(self.frame_3)
        self.le_full_name.setObjectName(u"le_full_name")

        self.horizontalLayout_4.addWidget(self.le_full_name)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.error_legal_status = QLabel(self.frame_3)
        self.error_legal_status.setObjectName(u"error_legal_status")
        sizePolicy5.setHeightForWidth(self.error_legal_status.sizePolicy().hasHeightForWidth())
        self.error_legal_status.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.error_legal_status)

        self.cb_legal_status = QComboBox(self.frame_3)
        self.cb_legal_status.setObjectName(u"cb_legal_status")

        self.horizontalLayout_8.addWidget(self.cb_legal_status)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.tab_client)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.pb_edit = QPushButton(self.frame_2)
        self.pb_edit.setObjectName(u"pb_edit")

        self.horizontalLayout_13.addWidget(self.pb_edit)

        self.pb_delete = QPushButton(self.frame_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.horizontalLayout_13.addWidget(self.pb_delete)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_client, "")
        self.tab_dossiers = QWidget()
        self.tab_dossiers.setObjectName(u"tab_dossiers")
        self.verticalLayout_4 = QVBoxLayout(self.tab_dossiers)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(self.tab_dossiers)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_11.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_11.addWidget(self.pushButton_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.tab_dossiers)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.le_find_dossier = QLineEdit(self.tab_dossiers)
        self.le_find_dossier.setObjectName(u"le_find_dossier")
        self.le_find_dossier.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.le_find_dossier)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.frame_5 = QFrame(self.tab_dossiers)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.frame_5)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.spinBox = QSpinBox(self.frame_7)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_12.addWidget(self.spinBox)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_dossiers, "")
        self.splitter.addWidget(self.tabWidget)

        self.horizontalLayout.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.widget)

        QWidget.setTabOrder(self.pb_add, self.tableView_client)
        QWidget.setTabOrder(self.tableView_client, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.pb_edit)
        QWidget.setTabOrder(self.pb_edit, self.pb_delete)
        QWidget.setTabOrder(self.pb_delete, self.cb_legal_status)
        QWidget.setTabOrder(self.cb_legal_status, self.le_full_name)
        QWidget.setTabOrder(self.le_full_name, self.le_address)
        QWidget.setTabOrder(self.le_address, self.le_phone)
        QWidget.setTabOrder(self.le_phone, self.le_mobile)
        QWidget.setTabOrder(self.le_mobile, self.le_mail)
        QWidget.setTabOrder(self.le_mail, self.txe_notes)

        self.retranslateUi(page_clients)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_clients)
    # setupUi

    def retranslateUi(self, page_clients):
        page_clients.setWindowTitle(QCoreApplication.translate("page_clients", u"Form", None))
        self.le_find.setPlaceholderText("")
        self.pb_add.setText(QCoreApplication.translate("page_clients", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644", None))
        self.error_address.setText("")
        self.error_mobile.setText("")
        self.le_mobile.setInputMask(QCoreApplication.translate("page_clients", u"9999 99 99 99", None))
        self.le_mobile.setPlaceholderText(QCoreApplication.translate("page_clients", u"9999 99 99 99", None))
        self.error_notes.setText("")
        self.error_mail.setText("")
        self.le_mail.setText("")
        self.le_mail.setPlaceholderText(QCoreApplication.translate("page_clients", u"personne@mail.com", None))
        self.error_phone.setText("")
        self.le_phone.setInputMask(QCoreApplication.translate("page_clients", u"999 99 99 99", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("page_clients", u"xxx xx xx xx", None))
        self.error_full_name.setText("")
        self.le_full_name.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628 \u0623\u0648 \u0627\u0644\u0647\u064a\u0626\u0629 \u0627\u0644\u0645\u062e\u062a\u0635\u0629 \u060c\u060c\u060c", None))
        self.error_legal_status.setText("")
        self.cb_legal_status.setPlaceholderText(QCoreApplication.translate("page_clients", u"\u062a\u062d\u0640\u062f\u064a\u062f \u0627\u0644\u0635\u0641\u0629 \u060c\u060c\u060c", None))
        self.label_2.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0635\u0641\u0629", None))
        self.label_8.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_3.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_4.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.label_6.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.label_5.setText(QCoreApplication.translate("page_clients", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.label_7.setText(QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0623\u062e\u0631\u0649", None))
        self.pb_edit.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pb_delete.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_client), QCoreApplication.translate("page_clients", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.pushButton_5.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("page_clients", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("page_clients", u"\u0628\u062d\u062b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dossiers), QCoreApplication.translate("page_clients", u"\u0645\u062d\u0627\u0636\u0631 \u0627\u0644\u0639\u0645\u064a\u0644", None))
    # retranslateUi

