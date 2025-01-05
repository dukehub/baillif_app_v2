# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_act.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTimeEdit, QToolButton, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_form_act(object):
    def setupUi(self, form_act):
        if not form_act.objectName():
            form_act.setObjectName(u"form_act")
        form_act.resize(1057, 574)
        self.verticalLayout_3 = QVBoxLayout(form_act)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(form_act)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tb_save = QToolButton(self.frame_4)
        self.tb_save.setObjectName(u"tb_save")
        icon = QIcon()
        icon.addFile(u":/icons/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_save.setIcon(icon)
        self.tb_save.setIconSize(QSize(24, 24))
        self.tb_save.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_save.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_save)

        self.tb_close = QToolButton(self.frame_4)
        self.tb_close.setObjectName(u"tb_close")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/export.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_close.setIcon(icon1)
        self.tb_close.setIconSize(QSize(24, 24))
        self.tb_close.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_close.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cb_type_rapport = QComboBox(self.frame_4)
        self.cb_type_rapport.setObjectName(u"cb_type_rapport")

        self.horizontalLayout_3.addWidget(self.cb_type_rapport)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.groupBox = QGroupBox(form_act)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.error_client = QLabel(self.groupBox)
        self.error_client.setObjectName(u"error_client")

        self.horizontalLayout.addWidget(self.error_client)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cb_client = QComboBox(self.frame_2)
        self.cb_client.setObjectName(u"cb_client")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_client.sizePolicy().hasHeightForWidth())
        self.cb_client.setSizePolicy(sizePolicy)
        self.cb_client.setEditable(True)

        self.horizontalLayout_2.addWidget(self.cb_client)

        self.pb_add_client = QPushButton(self.frame_2)
        self.pb_add_client.setObjectName(u"pb_add_client")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/plus_math.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add_client.setIcon(icon2)
        self.pb_add_client.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pb_add_client)


        self.horizontalLayout.addWidget(self.frame_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.chb_same = QCheckBox(self.groupBox)
        self.chb_same.setObjectName(u"chb_same")

        self.horizontalLayout_4.addWidget(self.chb_same)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.frame_6 = QFrame(form_act)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gb_demandeur_info = QGroupBox(self.frame_6)
        self.gb_demandeur_info.setObjectName(u"gb_demandeur_info")
        self.gridLayout = QGridLayout(self.gb_demandeur_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.gb_demandeur_info)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.error_demandeur = QLabel(self.gb_demandeur_info)
        self.error_demandeur.setObjectName(u"error_demandeur")

        self.horizontalLayout_5.addWidget(self.error_demandeur)

        self.cb_demandeur = QComboBox(self.gb_demandeur_info)
        self.cb_demandeur.setObjectName(u"cb_demandeur")
        sizePolicy.setHeightForWidth(self.cb_demandeur.sizePolicy().hasHeightForWidth())
        self.cb_demandeur.setSizePolicy(sizePolicy)
        self.cb_demandeur.setLocale(QLocale(QLocale.Arabic, QLocale.Algeria))
        self.cb_demandeur.setEditable(True)

        self.horizontalLayout_5.addWidget(self.cb_demandeur)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gb_demandeur_info)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.error_adr_demandeur = QLabel(self.gb_demandeur_info)
        self.error_adr_demandeur.setObjectName(u"error_adr_demandeur")

        self.horizontalLayout_6.addWidget(self.error_adr_demandeur)

        self.le_address_demandeur = QLineEdit(self.gb_demandeur_info)
        self.le_address_demandeur.setObjectName(u"le_address_demandeur")

        self.horizontalLayout_6.addWidget(self.le_address_demandeur)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.gb_demandeur_info)

        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.error_defendeur = QLabel(self.groupBox_2)
        self.error_defendeur.setObjectName(u"error_defendeur")

        self.horizontalLayout_7.addWidget(self.error_defendeur)

        self.cb_defendeur = QComboBox(self.groupBox_2)
        self.cb_defendeur.setObjectName(u"cb_defendeur")
        sizePolicy.setHeightForWidth(self.cb_defendeur.sizePolicy().hasHeightForWidth())
        self.cb_defendeur.setSizePolicy(sizePolicy)
        self.cb_defendeur.setEditable(True)

        self.horizontalLayout_7.addWidget(self.cb_defendeur)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.error_adr_defendeur = QLabel(self.groupBox_2)
        self.error_adr_defendeur.setObjectName(u"error_adr_defendeur")

        self.horizontalLayout_8.addWidget(self.error_adr_defendeur)

        self.le_address_defendeur = QLineEdit(self.groupBox_2)
        self.le_address_defendeur.setObjectName(u"le_address_defendeur")

        self.horizontalLayout_8.addWidget(self.le_address_defendeur)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(form_act)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.gb_tribunal_registary = QGroupBox(self.frame_7)
        self.gb_tribunal_registary.setObjectName(u"gb_tribunal_registary")
        self.gridLayout_5 = QGridLayout(self.gb_tribunal_registary)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lbl_council_reg = QLabel(self.gb_tribunal_registary)
        self.lbl_council_reg.setObjectName(u"lbl_council_reg")

        self.gridLayout_5.addWidget(self.lbl_council_reg, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.error_council_reg = QLabel(self.gb_tribunal_registary)
        self.error_council_reg.setObjectName(u"error_council_reg")

        self.horizontalLayout_9.addWidget(self.error_council_reg)

        self.cb_council_registary = QComboBox(self.gb_tribunal_registary)
        self.cb_council_registary.setObjectName(u"cb_council_registary")
        sizePolicy.setHeightForWidth(self.cb_council_registary.sizePolicy().hasHeightForWidth())
        self.cb_council_registary.setSizePolicy(sizePolicy)
        self.cb_council_registary.setEditable(True)

        self.horizontalLayout_9.addWidget(self.cb_council_registary)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.lbl_tribunal_reg = QLabel(self.gb_tribunal_registary)
        self.lbl_tribunal_reg.setObjectName(u"lbl_tribunal_reg")

        self.gridLayout_5.addWidget(self.lbl_tribunal_reg, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.error_tribunal_reg = QLabel(self.gb_tribunal_registary)
        self.error_tribunal_reg.setObjectName(u"error_tribunal_reg")

        self.horizontalLayout_10.addWidget(self.error_tribunal_reg)

        self.cb_tribunal_registary = QComboBox(self.gb_tribunal_registary)
        self.cb_tribunal_registary.setObjectName(u"cb_tribunal_registary")
        sizePolicy.setHeightForWidth(self.cb_tribunal_registary.sizePolicy().hasHeightForWidth())
        self.cb_tribunal_registary.setSizePolicy(sizePolicy)
        self.cb_tribunal_registary.setEditable(True)

        self.horizontalLayout_10.addWidget(self.cb_tribunal_registary)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.label_15 = QLabel(self.gb_tribunal_registary)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 2, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.error_date_reg = QLabel(self.gb_tribunal_registary)
        self.error_date_reg.setObjectName(u"error_date_reg")

        self.horizontalLayout_11.addWidget(self.error_date_reg)

        self.de_registary = QDateEdit(self.gb_tribunal_registary)
        self.de_registary.setObjectName(u"de_registary")
        sizePolicy.setHeightForWidth(self.de_registary.sizePolicy().hasHeightForWidth())
        self.de_registary.setSizePolicy(sizePolicy)
        self.de_registary.setCalendarPopup(True)

        self.horizontalLayout_11.addWidget(self.de_registary)


        self.gridLayout_5.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.gb_tribunal_registary, 0, 2, 1, 1)

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gb_tribunal = QGroupBox(self.frame)
        self.gb_tribunal.setObjectName(u"gb_tribunal")
        self.gridLayout_4 = QGridLayout(self.gb_tribunal)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.gb_tribunal)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.error_tribunal = QLabel(self.gb_tribunal)
        self.error_tribunal.setObjectName(u"error_tribunal")

        self.horizontalLayout_16.addWidget(self.error_tribunal)

        self.cb_tribunal = QComboBox(self.gb_tribunal)
        self.cb_tribunal.setObjectName(u"cb_tribunal")
        sizePolicy.setHeightForWidth(self.cb_tribunal.sizePolicy().hasHeightForWidth())
        self.cb_tribunal.setSizePolicy(sizePolicy)
        self.cb_tribunal.setEditable(True)

        self.horizontalLayout_16.addWidget(self.cb_tribunal)


        self.gridLayout_4.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gb_tribunal)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.error_section = QLabel(self.gb_tribunal)
        self.error_section.setObjectName(u"error_section")

        self.horizontalLayout_17.addWidget(self.error_section)

        self.cb_section = QComboBox(self.gb_tribunal)
        self.cb_section.setObjectName(u"cb_section")
        sizePolicy.setHeightForWidth(self.cb_section.sizePolicy().hasHeightForWidth())
        self.cb_section.setSizePolicy(sizePolicy)
        self.cb_section.setEditable(True)

        self.horizontalLayout_17.addWidget(self.cb_section)


        self.gridLayout_4.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gb_tribunal)

        self.gb_council = QGroupBox(self.frame)
        self.gb_council.setObjectName(u"gb_council")
        self.gridLayout_7 = QGridLayout(self.gb_council)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.gb_council)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.error_council = QLabel(self.gb_council)
        self.error_council.setObjectName(u"error_council")

        self.horizontalLayout_18.addWidget(self.error_council)

        self.cb_council = QComboBox(self.gb_council)
        self.cb_council.setObjectName(u"cb_council")
        sizePolicy.setHeightForWidth(self.cb_council.sizePolicy().hasHeightForWidth())
        self.cb_council.setSizePolicy(sizePolicy)
        self.cb_council.setEditable(True)

        self.horizontalLayout_18.addWidget(self.cb_council)


        self.gridLayout_7.addLayout(self.horizontalLayout_18, 0, 1, 1, 1)

        self.label_16 = QLabel(self.gb_council)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 1, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.error_room = QLabel(self.gb_council)
        self.error_room.setObjectName(u"error_room")

        self.horizontalLayout_19.addWidget(self.error_room)

        self.cb_room = QComboBox(self.gb_council)
        self.cb_room.setObjectName(u"cb_room")
        sizePolicy.setHeightForWidth(self.cb_room.sizePolicy().hasHeightForWidth())
        self.cb_room.setSizePolicy(sizePolicy)
        self.cb_room.setEditable(True)

        self.horizontalLayout_19.addWidget(self.cb_room)


        self.gridLayout_7.addLayout(self.horizontalLayout_19, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.gb_council)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_3.addWidget(self.label_44, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.error_date_audience = QLabel(self.groupBox_3)
        self.error_date_audience.setObjectName(u"error_date_audience")

        self.horizontalLayout_12.addWidget(self.error_date_audience)

        self.de_audience = QDateEdit(self.groupBox_3)
        self.de_audience.setObjectName(u"de_audience")
        sizePolicy.setHeightForWidth(self.de_audience.sizePolicy().hasHeightForWidth())
        self.de_audience.setSizePolicy(sizePolicy)
        self.de_audience.setCalendarPopup(True)

        self.horizontalLayout_12.addWidget(self.de_audience)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_3.addWidget(self.label_43, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.error_case = QLabel(self.groupBox_3)
        self.error_case.setObjectName(u"error_case")

        self.horizontalLayout_13.addWidget(self.error_case)

        self.le_case = QLineEdit(self.groupBox_3)
        self.le_case.setObjectName(u"le_case")

        self.horizontalLayout_13.addWidget(self.le_case)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 1, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_3)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_3.addWidget(self.label_42, 2, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.error_hall = QLabel(self.groupBox_3)
        self.error_hall.setObjectName(u"error_hall")

        self.horizontalLayout_14.addWidget(self.error_hall)

        self.le_hall = QLineEdit(self.groupBox_3)
        self.le_hall.setObjectName(u"le_hall")
        sizePolicy.setHeightForWidth(self.le_hall.sizePolicy().hasHeightForWidth())
        self.le_hall.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.le_hall)


        self.gridLayout_3.addLayout(self.horizontalLayout_14, 2, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_3)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_3.addWidget(self.label_41, 3, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.error_hour = QLabel(self.groupBox_3)
        self.error_hour.setObjectName(u"error_hour")

        self.horizontalLayout_15.addWidget(self.error_hour)

        self.te_audience = QTimeEdit(self.groupBox_3)
        self.te_audience.setObjectName(u"te_audience")
        sizePolicy.setHeightForWidth(self.te_audience.sizePolicy().hasHeightForWidth())
        self.te_audience.setSizePolicy(sizePolicy)
        self.te_audience.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.te_audience.setProperty(u"showGroupSeparator", False)
        self.te_audience.setCurrentSection(QDateTimeEdit.Section.MinuteSection)
        self.te_audience.setCalendarPopup(True)

        self.horizontalLayout_15.addWidget(self.te_audience)


        self.gridLayout_3.addLayout(self.horizontalLayout_15, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.cb_type_rapport, self.cb_client)
        QWidget.setTabOrder(self.cb_client, self.chb_same)
        QWidget.setTabOrder(self.chb_same, self.cb_demandeur)
        QWidget.setTabOrder(self.cb_demandeur, self.le_address_demandeur)
        QWidget.setTabOrder(self.le_address_demandeur, self.cb_defendeur)
        QWidget.setTabOrder(self.cb_defendeur, self.le_address_defendeur)
        QWidget.setTabOrder(self.le_address_defendeur, self.cb_tribunal)
        QWidget.setTabOrder(self.cb_tribunal, self.cb_section)
        QWidget.setTabOrder(self.cb_section, self.cb_council)
        QWidget.setTabOrder(self.cb_council, self.cb_room)
        QWidget.setTabOrder(self.cb_room, self.de_audience)
        QWidget.setTabOrder(self.de_audience, self.le_case)
        QWidget.setTabOrder(self.le_case, self.le_hall)
        QWidget.setTabOrder(self.le_hall, self.te_audience)
        QWidget.setTabOrder(self.te_audience, self.cb_council_registary)
        QWidget.setTabOrder(self.cb_council_registary, self.cb_tribunal_registary)
        QWidget.setTabOrder(self.cb_tribunal_registary, self.de_registary)
        QWidget.setTabOrder(self.de_registary, self.pb_add_client)
        QWidget.setTabOrder(self.pb_add_client, self.tb_save)
        QWidget.setTabOrder(self.tb_save, self.tb_close)

        self.retranslateUi(form_act)

        QMetaObject.connectSlotsByName(form_act)
    # setupUi

    def retranslateUi(self, form_act):
        form_act.setWindowTitle(QCoreApplication.translate("form_act", u"\u0645\u062d\u0636\u0631 \u062c\u062f\u064a\u062f", None))
        self.tb_save.setText(QCoreApplication.translate("form_act", u"\u062d\u0641\u0638", None))
        self.tb_close.setText(QCoreApplication.translate("form_act", u"\u0625\u0644\u063a\u0627\u0621", None))
        self.label_4.setText(QCoreApplication.translate("form_act", u"\u0645\u062d\u0636\u0631 \u062a\u0643\u0644\u064a\u0641 \u062a\u0633\u0644\u064a\u0645", None))
        self.groupBox.setTitle(QCoreApplication.translate("form_act", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_9.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.error_client.setText("")
        self.cb_client.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062a\u062d\u062f\u064a\u062f \u0623\u0648 \u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644 \u062c\u062f\u064a\u062f", None))
        self.pb_add_client.setText("")
        self.label_6.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0639\u0645\u0646\u0644 \u0646\u0641\u0633\u0647 \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.chb_same.setText(QCoreApplication.translate("form_act", u" \u0646\u0641\u0633\u0647", None))
        self.gb_demandeur_info.setTitle(QCoreApplication.translate("form_act", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.label_2.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.error_demandeur.setText("")
        self.cb_demandeur.setPlaceholderText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_3.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.error_adr_demandeur.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("form_act", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u0628\u0644\u063a \u0644\u0647", None))
        self.label_8.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.error_defendeur.setText("")
        self.cb_defendeur.setPlaceholderText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_7.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.error_adr_defendeur.setText("")
        self.gb_tribunal_registary.setTitle(QCoreApplication.translate("form_act", u"\u0627\u0644\u0645\u0633\u062c\u0644 \u0628\u0623\u0645\u0627\u064a\u0629 \u0636\u0628\u0637", None))
        self.lbl_council_reg.setText(QCoreApplication.translate("form_act", u"\u0645\u062c\u0644\u0633", None))
        self.error_council_reg.setText("")
        self.cb_council_registary.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u0645\u062c\u0644\u0633 ...", None))
        self.lbl_tribunal_reg.setText(QCoreApplication.translate("form_act", u"\u0645\u062d\u0643\u0645\u0629", None))
        self.error_tribunal_reg.setText("")
        self.cb_tribunal_registary.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u0645\u062d\u0643\u0645\u0629 ...", None))
        self.label_15.setText(QCoreApplication.translate("form_act", u"\u0628\u062a\u0627\u0631\u064a\u062e", None))
        self.error_date_reg.setText("")
        self.de_registary.setDisplayFormat(QCoreApplication.translate("form_act", u"dd/MM/yyyy", None))
        self.gb_tribunal.setTitle(QCoreApplication.translate("form_act", u"\u0627\u0644\u0645\u062d\u0643\u0645\u0629", None))
        self.label_5.setText(QCoreApplication.translate("form_act", u"\u0645\u062d\u0643\u0645\u0629", None))
        self.error_tribunal.setText("")
        self.cb_tribunal.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u0645\u062d\u0643\u0645\u0629 ...", None))
        self.label_20.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0642\u0633\u0645", None))
        self.error_section.setText("")
        self.cb_section.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u0642\u0633\u0645 ...", None))
        self.gb_council.setTitle(QCoreApplication.translate("form_act", u"\u0627\u0644\u0645\u062c\u0644\u0633", None))
        self.label.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0645\u062c\u0644\u0633", None))
        self.error_council.setText("")
        self.cb_council.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u0645\u062c\u0644\u0633 ...", None))
        self.label_16.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u063a\u0631\u0641\u0629", None))
        self.error_room.setText("")
        self.cb_room.setPlaceholderText(QCoreApplication.translate("form_act", u"\u062d\u062f\u062f \u0627\u0644\u063a\u0631\u0641\u0629 ....", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("form_act", u"\u0627\u0644\u062c\u0644\u0633\u0629", None))
        self.label_44.setText(QCoreApplication.translate("form_act", u"\u0628\u0627\u0631\u064a\u062e \u0627\u0644\u062c\u0644\u0633\u0629", None))
        self.error_date_audience.setText("")
        self.de_audience.setDisplayFormat(QCoreApplication.translate("form_act", u"dd/MM/yyyy", None))
        self.label_43.setText(QCoreApplication.translate("form_act", u"\u0642\u0636\u064a\u0629 \u0631\u0642\u0645", None))
        self.error_case.setText("")
        self.label_42.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0642\u0627\u0639\u0629", None))
        self.error_hall.setText("")
        self.label_41.setText(QCoreApplication.translate("form_act", u"\u0627\u0644\u0633\u0627\u0639\u0629", None))
        self.error_hour.setText("")
        self.te_audience.setDisplayFormat(QCoreApplication.translate("form_act", u"mm:HH", None))
    # retranslateUi

