# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDialog,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(831, 688)
        SettingsDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(SettingsDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_settings = QFrame(self.frame_3)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setMinimumSize(QSize(150, 0))
        self.frame_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_settings.setAutoFillBackground(False)
        self.frame_settings.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_settings)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_bailiff_info = QPushButton(self.frame_settings)
        self.buttonGroup = QButtonGroup(SettingsDialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pb_bailiff_info)
        self.pb_bailiff_info.setObjectName(u"pb_bailiff_info")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_bailiff_info.sizePolicy().hasHeightForWidth())
        self.pb_bailiff_info.setSizePolicy(sizePolicy)
        self.pb_bailiff_info.setCheckable(True)
        self.pb_bailiff_info.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_bailiff_info)

        self.pb_propeties = QPushButton(self.frame_settings)
        self.buttonGroup.addButton(self.pb_propeties)
        self.pb_propeties.setObjectName(u"pb_propeties")
        sizePolicy.setHeightForWidth(self.pb_propeties.sizePolicy().hasHeightForWidth())
        self.pb_propeties.setSizePolicy(sizePolicy)
        self.pb_propeties.setIconSize(QSize(32, 32))
        self.pb_propeties.setCheckable(True)
        self.pb_propeties.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_propeties)

        self.pb_users = QPushButton(self.frame_settings)
        self.buttonGroup.addButton(self.pb_users)
        self.pb_users.setObjectName(u"pb_users")
        sizePolicy.setHeightForWidth(self.pb_users.sizePolicy().hasHeightForWidth())
        self.pb_users.setSizePolicy(sizePolicy)
        self.pb_users.setIconSize(QSize(32, 32))
        self.pb_users.setCheckable(True)
        self.pb_users.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_users)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_settings)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_bailiff = QWidget()
        self.page_bailiff.setObjectName(u"page_bailiff")
        self.gridLayout_2 = QGridLayout(self.page_bailiff)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.le_email = QLineEdit(self.page_bailiff)
        self.le_email.setObjectName(u"le_email")

        self.gridLayout_2.addWidget(self.le_email, 10, 1, 1, 1)

        self.label_12 = QLabel(self.page_bailiff)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.le_address = QLineEdit(self.page_bailiff)
        self.le_address.setObjectName(u"le_address")
        self.le_address.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.gridLayout_2.addWidget(self.le_address, 3, 1, 1, 3)

        self.le_phone = QLineEdit(self.page_bailiff)
        self.le_phone.setObjectName(u"le_phone")

        self.gridLayout_2.addWidget(self.le_phone, 8, 1, 1, 1)

        self.label_11 = QLabel(self.page_bailiff)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_8 = QLabel(self.page_bailiff)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_13 = QLabel(self.page_bailiff)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 10, 0, 1, 1)

        self.le_register_in = QLineEdit(self.page_bailiff)
        self.le_register_in.setObjectName(u"le_register_in")

        self.gridLayout_2.addWidget(self.le_register_in, 2, 1, 1, 3)

        self.le_mobile = QLineEdit(self.page_bailiff)
        self.le_mobile.setObjectName(u"le_mobile")

        self.gridLayout_2.addWidget(self.le_mobile, 8, 3, 1, 1)

        self.label_10 = QLabel(self.page_bailiff)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.le_name = QLineEdit(self.page_bailiff)
        self.le_name.setObjectName(u"le_name")

        self.gridLayout_2.addWidget(self.le_name, 1, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 11, 1, 1, 1)

        self.label_14 = QLabel(self.page_bailiff)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 8, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_bailiff)
        self.page_users = QWidget()
        self.page_users.setObjectName(u"page_users")
        self.stackedWidget.addWidget(self.page_users)
        self.page_options = QWidget()
        self.page_options.setObjectName(u"page_options")
        self.formLayout = QFormLayout(self.page_options)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.page_options)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_templates = QComboBox(self.page_options)
        self.cb_templates.setObjectName(u"cb_templates")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_templates)

        self.stackedWidget.addWidget(self.page_options)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pb_cancel = QPushButton(self.frame_2)
        self.pb_cancel.setObjectName(u"pb_cancel")

        self.horizontalLayout_2.addWidget(self.pb_cancel)

        self.pb_save = QPushButton(self.frame_2)
        self.pb_save.setObjectName(u"pb_save")

        self.horizontalLayout_2.addWidget(self.pb_save)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(SettingsDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0625\u0639\u062f\u0627\u062f\u0627\u062a", None))
        self.pb_bailiff_info.setText(QCoreApplication.translate("SettingsDialog", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u062d\u0636\u0631", None))
        self.pb_propeties.setText(QCoreApplication.translate("SettingsDialog", u"\u062e\u0635\u0627\u0626\u0635", None))
        self.pb_users.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u064a\u0646", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0647\u0627\u0628\u0641", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u0645\u0633\u062c\u0644 \u0628\u0640", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0646\u0645\u0648\u0630\u062c", None))
        self.pb_cancel.setText(QCoreApplication.translate("SettingsDialog", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.pb_save.setText(QCoreApplication.translate("SettingsDialog", u"\u062d\u0641\u0638", None))
    # retranslateUi

