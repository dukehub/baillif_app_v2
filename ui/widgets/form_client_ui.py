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
        form_client.resize(836, 297)
        icon = QIcon()
        icon.addFile(u":/icons/icons/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        form_client.setWindowIcon(icon)
        self.gridLayout = QGridLayout(form_client)
        self.gridLayout.setObjectName(u"gridLayout")
        self.error_status = QLabel(form_client)
        self.error_status.setObjectName(u"error_status")

        self.gridLayout.addWidget(self.error_status, 1, 1, 1, 1)

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


        self.gridLayout.addWidget(self.frame, 17, 0, 1, 6)

        self.error_address = QLabel(form_client)
        self.error_address.setObjectName(u"error_address")

        self.gridLayout.addWidget(self.error_address, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(form_client)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 4)

        self.error_name = QLabel(form_client)
        self.error_name.setObjectName(u"error_name")

        self.gridLayout.addWidget(self.error_name, 1, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 5, 1, 1)

        self.error_phone = QLabel(form_client)
        self.error_phone.setObjectName(u"error_phone")

        self.gridLayout.addWidget(self.error_phone, 6, 1, 1, 1)

        self.le_full_name = QLineEdit(form_client)
        self.le_full_name.setObjectName(u"le_full_name")

        self.gridLayout.addWidget(self.le_full_name, 1, 5, 1, 1)

        self.le_phone = QLineEdit(form_client)
        self.le_phone.setObjectName(u"le_phone")

        self.gridLayout.addWidget(self.le_phone, 6, 2, 1, 1)

        self.cb_legal_status = QComboBox(form_client)
        self.cb_legal_status.setObjectName(u"cb_legal_status")

        self.gridLayout.addWidget(self.cb_legal_status, 1, 2, 1, 1)

        self.label_2 = QLabel(form_client)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.label = QLabel(form_client)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(form_client)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(form_client)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.le_mail = QLineEdit(form_client)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setMaxLength(32767)

        self.gridLayout.addWidget(self.le_mail, 7, 5, 1, 1)

        self.label_5 = QLabel(form_client)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 3, 1, 1)

        self.error_mail = QLabel(form_client)
        self.error_mail.setObjectName(u"error_mail")

        self.gridLayout.addWidget(self.error_mail, 7, 4, 1, 1)

        self.label_6 = QLabel(form_client)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.le_mobile = QLineEdit(form_client)
        self.le_mobile.setObjectName(u"le_mobile")

        self.gridLayout.addWidget(self.le_mobile, 7, 2, 1, 1)

        self.error_mobile = QLabel(form_client)
        self.error_mobile.setObjectName(u"error_mobile")

        self.gridLayout.addWidget(self.error_mobile, 7, 1, 1, 1)

        self.txe_notes = QTextEdit(form_client)
        self.txe_notes.setObjectName(u"txe_notes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txe_notes.sizePolicy().hasHeightForWidth())
        self.txe_notes.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.txe_notes, 12, 2, 1, 4)

        self.label_7 = QLabel(form_client)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)


        self.retranslateUi(form_client)

        QMetaObject.connectSlotsByName(form_client)
    # setupUi

    def retranslateUi(self, form_client):
        form_client.setWindowTitle(QCoreApplication.translate("form_client", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644 \u062c\u062f\u064a\u062f", None))
        self.error_status.setText("")
        self.pb_cancel.setText(QCoreApplication.translate("form_client", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.pb_save.setText(QCoreApplication.translate("form_client", u"\u062d\u0641\u0638", None))
        self.error_address.setText("")
        self.error_name.setText("")
        self.error_phone.setText("")
        self.le_full_name.setPlaceholderText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628 \u0623\u0648 \u0627\u0644\u0647\u064a\u0626\u0629 \u0627\u0644\u0645\u062e\u062a\u0635\u0629 \u060c\u060c\u060c", None))
        self.le_phone.setInputMask(QCoreApplication.translate("form_client", u"999 99 99 99", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("form_client", u"xxx xx xx xx", None))
        self.cb_legal_status.setPlaceholderText(QCoreApplication.translate("form_client", u"\u062a\u062d\u0640\u062f\u064a\u062f \u0627\u0644\u0635\u0641\u0629 \u060c\u060c\u060c", None))
        self.label_2.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0635\u0641\u0629", None))
        self.label_3.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_4.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0647\u0627\u062a\u0641", None))
        self.le_mail.setText("")
        self.le_mail.setPlaceholderText(QCoreApplication.translate("form_client", u"personne@mail.com", None))
        self.label_5.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.error_mail.setText("")
        self.label_6.setText(QCoreApplication.translate("form_client", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.le_mobile.setInputMask(QCoreApplication.translate("form_client", u"9999 99 99 99", None))
        self.le_mobile.setPlaceholderText(QCoreApplication.translate("form_client", u"9999 99 99 99", None))
        self.error_mobile.setText("")
        self.label_7.setText(QCoreApplication.translate("form_client", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0623\u062e\u0631\u0649", None))
    # retranslateUi

