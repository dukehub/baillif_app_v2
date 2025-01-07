# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_client.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)
import ui.resources_rc

class Ui_form_client(object):
    def setupUi(self, form_client):
        if not form_client.objectName():
            form_client.setObjectName(u"form_client")
        form_client.resize(870, 267)
        icon = QIcon()
        icon.addFile(u":/icons/icons/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        form_client.setWindowIcon(icon)
        self.gridLayout = QGridLayout(form_client)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(form_client)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.error_legal_status = QLabel(form_client)
        self.error_legal_status.setObjectName(u"error_legal_status")

        self.horizontalLayout_5.addWidget(self.error_legal_status)

        self.cb_legal_status = QComboBox(form_client)
        self.cb_legal_status.setObjectName(u"cb_legal_status")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_legal_status.sizePolicy().hasHeightForWidth())
        self.cb_legal_status.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.cb_legal_status)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.label_2 = QLabel(form_client)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.error_full_name = QLabel(form_client)
        self.error_full_name.setObjectName(u"error_full_name")

        self.horizontalLayout_2.addWidget(self.error_full_name)

        self.le_full_name = QLineEdit(form_client)
        self.le_full_name.setObjectName(u"le_full_name")

        self.horizontalLayout_2.addWidget(self.le_full_name)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.label_3 = QLabel(form_client)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(form_client)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.error_phone = QLabel(form_client)
        self.error_phone.setObjectName(u"error_phone")

        self.horizontalLayout_7.addWidget(self.error_phone)

        self.le_phone = QLineEdit(form_client)
        self.le_phone.setObjectName(u"le_phone")

        self.horizontalLayout_7.addWidget(self.le_phone)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.label_5 = QLabel(form_client)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.error_mail = QLabel(form_client)
        self.error_mail.setObjectName(u"error_mail")

        self.horizontalLayout_4.addWidget(self.error_mail)

        self.le_mail = QLineEdit(form_client)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setMaxLength(32767)

        self.horizontalLayout_4.addWidget(self.le_mail)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 3, 1, 1)

        self.label_6 = QLabel(form_client)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(form_client)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.error_notes = QLabel(form_client)
        self.error_notes.setObjectName(u"error_notes")

        self.horizontalLayout_8.addWidget(self.error_notes)

        self.txe_notes = QTextEdit(form_client)
        self.txe_notes.setObjectName(u"txe_notes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txe_notes.sizePolicy().hasHeightForWidth())
        self.txe_notes.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.txe_notes)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.frame = QFrame(form_client)
        self.frame.setObjectName(u"frame")
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

        self.horizontalLayout.addWidget(self.pb_save)


        self.gridLayout.addWidget(self.frame, 5, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.error_address = QLabel(form_client)
        self.error_address.setObjectName(u"error_address")

        self.horizontalLayout_3.addWidget(self.error_address)

        self.le_address = QLineEdit(form_client)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_3.addWidget(self.le_address)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.error_mobile = QLabel(form_client)
        self.error_mobile.setObjectName(u"error_mobile")

        self.horizontalLayout_6.addWidget(self.error_mobile)

        self.le_mobile = QLineEdit(form_client)
        self.le_mobile.setObjectName(u"le_mobile")

        self.horizontalLayout_6.addWidget(self.le_mobile)


        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        QWidget.setTabOrder(self.cb_legal_status, self.le_full_name)
        QWidget.setTabOrder(self.le_full_name, self.le_address)
        QWidget.setTabOrder(self.le_address, self.le_phone)
        QWidget.setTabOrder(self.le_phone, self.le_mail)
        QWidget.setTabOrder(self.le_mail, self.le_mobile)
        QWidget.setTabOrder(self.le_mobile, self.txe_notes)
        QWidget.setTabOrder(self.txe_notes, self.pb_cancel)
        QWidget.setTabOrder(self.pb_cancel, self.pb_save)

        self.retranslateUi(form_client)

        QMetaObject.connectSlotsByName(form_client)
    # setupUi

    def retranslateUi(self, form_client):
        form_client.setWindowTitle(QCoreApplication.translate("form_client", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644 \u062c\u062f\u064a\u062f", None))
        self.label.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0635\u0641\u0629", None))
        self.error_legal_status.setText("")
        self.cb_legal_status.setPlaceholderText(QCoreApplication.translate("form_client", u"\u062a\u062d\u0640\u062f\u064a\u062f \u0627\u0644\u0635\u0641\u0629 \u060c\u060c\u060c", None))
        self.label_2.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.error_full_name.setText("")
        self.le_full_name.setPlaceholderText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628 \u0623\u0648 \u0627\u0644\u0647\u064a\u0626\u0629 \u0627\u0644\u0645\u062e\u062a\u0635\u0629 \u060c\u060c\u060c", None))
        self.label_3.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_4.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.error_phone.setText("")
        self.le_phone.setInputMask(QCoreApplication.translate("form_client", u"999 99 99 99", None))
        self.label_5.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.error_mail.setText("")
        self.le_mail.setText("")
        self.le_mail.setPlaceholderText(QCoreApplication.translate("form_client", u"personne@mail.com", None))
        self.label_6.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.label_7.setText(QCoreApplication.translate("form_client", u"\u0645\u0644\u062d\u0648\u0638\u0627\u062a", None))
        self.error_notes.setText("")
        self.pb_cancel.setText(QCoreApplication.translate("form_client", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.pb_save.setText(QCoreApplication.translate("form_client", u"\u062d\u0641\u0638", None))
        self.error_address.setText("")
        self.error_mobile.setText("")
        self.le_mobile.setInputMask(QCoreApplication.translate("form_client", u"9999 99 99 99", None))
    # retranslateUi

