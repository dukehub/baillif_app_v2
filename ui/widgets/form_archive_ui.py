# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_archive.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import ( QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

from helpers.formats import NumberFormatLineEdit

class Ui_form_archhive(object):
    def setupUi(self, form_archhive):
        if not form_archhive.objectName():
            form_archhive.setObjectName(u"form_archhive")
        form_archhive.resize(925, 381)
        self.gridLayout_3 = QGridLayout(form_archhive)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(6)
        self.label_7 = QLabel(form_archhive)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(form_archhive)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.lbl_demandeur = QLabel(form_archhive)
        self.lbl_demandeur.setObjectName(u"lbl_demandeur")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_demandeur.sizePolicy().hasHeightForWidth())
        self.lbl_demandeur.setSizePolicy(sizePolicy)
        self.lbl_demandeur.setFrameShape(QFrame.Shape.Box)
        self.lbl_demandeur.setScaledContents(True)
        self.lbl_demandeur.setWordWrap(True)

        self.gridLayout_3.addWidget(self.lbl_demandeur, 1, 1, 1, 1)

        self.frame = QFrame(form_archhive)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_cancel = QPushButton(self.frame)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout.addWidget(self.pb_cancel)

        self.pb_save = QPushButton(self.frame)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setEnabled(False)

        self.horizontalLayout.addWidget(self.pb_save)


        self.gridLayout_3.addWidget(self.frame, 4, 0, 1, 2)

        self.gb_archive = QGroupBox(form_archhive)
        self.gb_archive.setObjectName(u"gb_archive")
        self.gb_archive.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gb_archive.sizePolicy().hasHeightForWidth())
        self.gb_archive.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.gb_archive)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.error_num_box = QLabel(self.gb_archive)
        self.error_num_box.setObjectName(u"error_num_box")

        self.gridLayout_2.addWidget(self.error_num_box, 0, 2, 1, 1)

        self.error_date_accus = QLabel(self.gb_archive)
        self.error_date_accus.setObjectName(u"error_date_accus")

        self.gridLayout_2.addWidget(self.error_date_accus, 3, 2, 1, 1)

        self.error_num_archive = QLabel(self.gb_archive)
        self.error_num_archive.setObjectName(u"error_num_archive")

        self.gridLayout_2.addWidget(self.error_num_archive, 2, 2, 1, 1)

        self.le_num_archive = QLineEdit(self.gb_archive)
        self.le_num_archive.setObjectName(u"le_num_archive")

        self.gridLayout_2.addWidget(self.le_num_archive, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gb_archive)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.date_accus = QDateEdit(self.gb_archive)
        self.date_accus.setObjectName(u"date_accus")
        self.date_accus.setProperty(u"showGroupSeparator", False)
        self.date_accus.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.date_accus, 3, 1, 1, 1)

        self.label_5 = QLabel(self.gb_archive)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.cb_num_box = QComboBox(self.gb_archive)
        self.cb_num_box.setObjectName(u"cb_num_box")
        self.cb_num_box.setEditable(True)

        self.gridLayout_2.addWidget(self.cb_num_box, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gb_archive)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.pb_upload = QPushButton(self.gb_archive)
        self.pb_upload.setObjectName(u"pb_upload")

        self.gridLayout_2.addWidget(self.pb_upload, 0, 3, 1, 1)

        self.le_file_name = QLineEdit(self.gb_archive)
        self.le_file_name.setObjectName(u"le_file_name")
        self.le_file_name.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_file_name, 0, 4, 1, 1)

        self.label_4 = QLabel(self.gb_archive)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 3, 1, 1)

        self.le_honoraires = NumberFormatLineEdit(self.gb_archive)
        self.le_honoraires.setObjectName(u"le_honoraires")

        self.gridLayout_2.addWidget(self.le_honoraires, 3, 4, 1, 1)

        self.error_file_name = QLabel(self.gb_archive)
        self.error_file_name.setObjectName(u"error_file_name")

        self.gridLayout_2.addWidget(self.error_file_name, 0, 5, 1, 1)

        self.error_honoraires = QLabel(self.gb_archive)
        self.error_honoraires.setObjectName(u"error_honoraires")

        self.gridLayout_2.addWidget(self.error_honoraires, 3, 5, 1, 1)


        self.gridLayout_3.addWidget(self.gb_archive, 3, 0, 1, 2)

        self.lbl_defendeur = QLabel(form_archhive)
        self.lbl_defendeur.setObjectName(u"lbl_defendeur")
        self.lbl_defendeur.setFrameShape(QFrame.Shape.Box)
        self.lbl_defendeur.setScaledContents(True)
        self.lbl_defendeur.setWordWrap(True)

        self.gridLayout_3.addWidget(self.lbl_defendeur, 2, 1, 1, 1)

        self.label = QLabel(form_archhive)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.cb_num_doc = QComboBox(form_archhive)
        self.cb_num_doc.setObjectName(u"cb_num_doc")
        sizePolicy2.setHeightForWidth(self.cb_num_doc.sizePolicy().hasHeightForWidth())
        self.cb_num_doc.setSizePolicy(sizePolicy2)
        self.cb_num_doc.setEditable(True)

        self.gridLayout_3.addWidget(self.cb_num_doc, 0, 1, 1, 1)

        self.error_num_doc = QLabel(form_archhive)
        self.error_num_doc.setObjectName(u"error_num_doc")

        self.gridLayout_3.addWidget(self.error_num_doc, 0, 2, 1, 1)

        QWidget.setTabOrder(self.cb_num_doc, self.cb_num_box)
        QWidget.setTabOrder(self.cb_num_box, self.le_num_archive)
        QWidget.setTabOrder(self.le_num_archive, self.date_accus)

        self.retranslateUi(form_archhive)

        QMetaObject.connectSlotsByName(form_archhive)
    # setupUi

    def retranslateUi(self, form_archhive):
        form_archhive.setWindowTitle(QCoreApplication.translate("form_archhive", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("form_archhive", u"\u0627\u0644\u0645\u0637\u0644\u0648\u0628", None))
        self.label_6.setText(QCoreApplication.translate("form_archhive", u"\u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.lbl_demandeur.setText("")
        self.pb_cancel.setText(QCoreApplication.translate("form_archhive", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.pb_save.setText(QCoreApplication.translate("form_archhive", u"\u0645\u0648\u0627\u0641\u0642", None))
        self.gb_archive.setTitle(QCoreApplication.translate("form_archhive", u"\u0627\u0644\u0623\u0631\u0634\u064a\u0641", None))
        self.error_num_box.setText("")
        self.error_date_accus.setText("")
        self.error_num_archive.setText("")
        self.label_2.setText(QCoreApplication.translate("form_archhive", u"\u0639\u0644\u0628\u0629 \u0627\u0644\u0623\u0631\u0634\u064a\u0641", None))
        self.date_accus.setDisplayFormat(QCoreApplication.translate("form_archhive", u"dd/MM/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("form_archhive", u"\u0631\u0642\u0645 \u0627\u0644\u0623\u0631\u0634\u064a\u0641", None))
        self.label_3.setText(QCoreApplication.translate("form_archhive", u"\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u062a\u0628\u0644\u064a\u063a", None))
        self.pb_upload.setText(QCoreApplication.translate("form_archhive", u"\u062a\u062d\u0645\u064a\u0644 \u0627\u0644\u0645\u062c\u0636\u0631", None))
        self.label_4.setText(QCoreApplication.translate("form_archhive", u"\u0627\u0644\u0623\u062a\u0639\u0627\u0628", None))
        self.error_file_name.setText("")
        self.error_honoraires.setText("")
        self.lbl_defendeur.setText("")
        self.label.setText(QCoreApplication.translate("form_archhive", u"\u0631\u0642\u0645 \u0627\u0644\u0645\u062d\u0636\u0631", None))
        self.cb_num_doc.setPlaceholderText(QCoreApplication.translate("form_archhive", u"\u0623\u062f\u062e\u0644 \u0631\u0642\u0645 \u0627\u0644\u0645\u062d\u0636\u0631", None))
        self.error_num_doc.setText("")
    # retranslateUi

