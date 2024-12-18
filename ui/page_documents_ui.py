# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_documents.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTabWidget, QTextEdit, QTimeEdit, QToolButton,
    QTreeView, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_page_documents(object):
    def setupUi(self, page_documents):
        if not page_documents.objectName():
            page_documents.setObjectName(u"page_documents")
        page_documents.resize(1291, 908)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_documents.sizePolicy().hasHeightForWidth())
        page_documents.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(page_documents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(page_documents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.tab)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.widget_left = QWidget(self.splitter)
        self.widget_left.setObjectName(u"widget_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy1)
        self.widget_left.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.widget_left)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.treeView_templates = QTreeView(self.widget_left)
        self.treeView_templates.setObjectName(u"treeView_templates")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.treeView_templates.sizePolicy().hasHeightForWidth())
        self.treeView_templates.setSizePolicy(sizePolicy2)
        self.treeView_templates.setMinimumSize(QSize(0, 0))
        self.treeView_templates.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeView_templates.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.treeView_templates)

        self.label_6 = QLabel(self.widget_left)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.document_list_view = QListView(self.widget_left)
        self.document_list_view.setObjectName(u"document_list_view")
        self.document_list_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.document_list_view.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.document_list_view)

        self.splitter.addWidget(self.widget_left)
        self.widget_right = QWidget(self.splitter)
        self.widget_right.setObjectName(u"widget_right")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_right.sizePolicy().hasHeightForWidth())
        self.widget_right.setSizePolicy(sizePolicy3)
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.widget_right)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolButton = QToolButton(self.frame_4)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame_4)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_3.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.frame_4)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_3.addWidget(self.toolButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.widget_right)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.frame_8)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.cb_client = QComboBox(self.frame_2)
        self.cb_client.setObjectName(u"cb_client")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cb_client.sizePolicy().hasHeightForWidth())
        self.cb_client.setSizePolicy(sizePolicy5)
        self.cb_client.setEditable(True)

        self.horizontalLayout_2.addWidget(self.cb_client)

        self.pb_add_client = QPushButton(self.frame_2)
        self.pb_add_client.setObjectName(u"pb_add_client")
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus_math.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_add_client.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pb_add_client)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon)

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/subtract.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.frame, 1, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit.setLineWrapColumnOrWidth(1)

        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_5, 0, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.gridLayout_2.addWidget(self.textEdit_2, 4, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.horizontalLayout.addWidget(self.frame_8)

        self.gb_council = QGroupBox(self.frame_6)
        self.gb_council.setObjectName(u"gb_council")
        self.gridLayout_16 = QGridLayout(self.gb_council)
        self.gridLayout_16.setSpacing(5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 20, 0, 5)
        self.frm_council_case = QFrame(self.gb_council)
        self.frm_council_case.setObjectName(u"frm_council_case")
        self.frm_council_case.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_case.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_11 = QFormLayout(self.frm_council_case)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setHorizontalSpacing(0)
        self.formLayout_11.setVerticalSpacing(0)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frm_council_case)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_11.setWidget(0, QFormLayout.SpanningRole, self.label_43)

        self.lineEdit_27 = QLineEdit(self.frm_council_case)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.formLayout_11.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_27)


        self.gridLayout_16.addWidget(self.frm_council_case, 13, 0, 1, 1)

        self.frm_council_hour = QFrame(self.gb_council)
        self.frm_council_hour.setObjectName(u"frm_council_hour")
        self.frm_council_hour.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_council_hour.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_13 = QFormLayout(self.frm_council_hour)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setHorizontalSpacing(0)
        self.formLayout_13.setVerticalSpacing(0)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frm_council_hour)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_13.setWidget(0, QFormLayout.SpanningRole, self.label_41)

        self.timeEdit = QTimeEdit(self.frm_council_hour)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy5.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy5)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.timeEdit.setProperty(u"showGroupSeparator", False)
        self.timeEdit.setCalendarPopup(True)

        self.formLayout_13.setWidget(1, QFormLayout.FieldRole, self.timeEdit)


        self.gridLayout_16.addWidget(self.frm_council_hour, 15, 0, 1, 1)

        self.frm_council_date = QFrame(self.gb_council)
        self.frm_council_date.setObjectName(u"frm_council_date")
        self.frm_council_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_date.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_8 = QFormLayout(self.frm_council_date)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setHorizontalSpacing(0)
        self.formLayout_8.setVerticalSpacing(0)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frm_council_date)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_8.setWidget(0, QFormLayout.SpanningRole, self.label_18)

        self.dateEdit = QDateEdit(self.frm_council_date)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy5.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy5)
        self.dateEdit.setCalendarPopup(True)

        self.formLayout_8.setWidget(1, QFormLayout.SpanningRole, self.dateEdit)


        self.gridLayout_16.addWidget(self.frm_council_date, 0, 0, 1, 1)

        self.frm_council = QFrame(self.gb_council)
        self.frm_council.setObjectName(u"frm_council")
        self.frm_council.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frm_council)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.frm_council)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)

        self.gridLayout_15.addWidget(self.comboBox, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frm_council)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon)

        self.gridLayout_15.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.label = QLabel(self.frm_council)
        self.label.setObjectName(u"label")

        self.gridLayout_15.addWidget(self.label, 0, 1, 1, 2)


        self.gridLayout_16.addWidget(self.frm_council, 2, 0, 1, 1)

        self.frm_council_table = QFrame(self.gb_council)
        self.frm_council_table.setObjectName(u"frm_council_table")
        self.frm_council_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_table.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frm_council_table)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frm_council_table)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_4)

        self.label_22 = QLabel(self.frm_council_table)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.label_22)


        self.gridLayout_16.addWidget(self.frm_council_table, 8, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_5, 11, 0, 1, 1)

        self.frm_council_hall = QFrame(self.gb_council)
        self.frm_council_hall.setObjectName(u"frm_council_hall")
        self.frm_council_hall.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_hall.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_12 = QFormLayout(self.frm_council_hall)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setHorizontalSpacing(0)
        self.formLayout_12.setVerticalSpacing(0)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frm_council_hall)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_12.setWidget(0, QFormLayout.SpanningRole, self.label_42)

        self.lineEdit_26 = QLineEdit(self.frm_council_hall)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        sizePolicy5.setHeightForWidth(self.lineEdit_26.sizePolicy().hasHeightForWidth())
        self.lineEdit_26.setSizePolicy(sizePolicy5)

        self.formLayout_12.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_26)


        self.gridLayout_16.addWidget(self.frm_council_hall, 14, 0, 1, 1)

        self.frm_council_session_date = QFrame(self.gb_council)
        self.frm_council_session_date.setObjectName(u"frm_council_session_date")
        self.frm_council_session_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_session_date.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_10 = QFormLayout(self.frm_council_session_date)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(0)
        self.formLayout_10.setVerticalSpacing(0)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frm_council_session_date)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_10.setWidget(0, QFormLayout.SpanningRole, self.label_44)

        self.dateEdit_9 = QDateEdit(self.frm_council_session_date)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        sizePolicy5.setHeightForWidth(self.dateEdit_9.sizePolicy().hasHeightForWidth())
        self.dateEdit_9.setSizePolicy(sizePolicy5)
        self.dateEdit_9.setCalendarPopup(True)

        self.formLayout_10.setWidget(1, QFormLayout.SpanningRole, self.dateEdit_9)


        self.gridLayout_16.addWidget(self.frm_council_session_date, 12, 0, 1, 1)

        self.frm_council_room = QFrame(self.gb_council)
        self.frm_council_room.setObjectName(u"frm_council_room")
        self.frm_council_room.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_room.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frm_council_room)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frm_council_room)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon)

        self.gridLayout_3.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frm_council_room)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_16 = QLabel(self.frm_council_room)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 1, 1, 2)


        self.gridLayout_16.addWidget(self.frm_council_room, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_2, 16, 0, 1, 1)

        self.frm_council_index = QFrame(self.gb_council)
        self.frm_council_index.setObjectName(u"frm_council_index")
        self.frm_council_index.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_council_index.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_9 = QFormLayout(self.frm_council_index)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(0)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frm_council_index)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_9.setWidget(0, QFormLayout.SpanningRole, self.label_23)

        self.lineEdit_5 = QLineEdit(self.frm_council_index)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_9.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_5)


        self.gridLayout_16.addWidget(self.frm_council_index, 5, 0, 1, 1)

        self.gb_council_registary = QGroupBox(self.gb_council)
        self.gb_council_registary.setObjectName(u"gb_council_registary")
        self.gridLayout_6 = QGridLayout(self.gb_council_registary)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 10, 0, 0)
        self.dateEdit_5 = QDateEdit(self.gb_council_registary)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setCalendarPopup(True)

        self.gridLayout_6.addWidget(self.dateEdit_5, 5, 0, 1, 2)

        self.pushButton_12 = QPushButton(self.gb_council_registary)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon)

        self.gridLayout_6.addWidget(self.pushButton_12, 1, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.gb_council_registary)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy5.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy5)

        self.gridLayout_6.addWidget(self.comboBox_4, 1, 0, 1, 1)

        self.label_28 = QLabel(self.gb_council_registary)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_6.addWidget(self.label_28, 4, 0, 1, 2)

        self.label_27 = QLabel(self.gb_council_registary)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 2)


        self.gridLayout_16.addWidget(self.gb_council_registary, 10, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_4, 9, 0, 1, 1)


        self.horizontalLayout.addWidget(self.gb_council)

        self.gb_tribunal = QGroupBox(self.frame_6)
        self.gb_tribunal.setObjectName(u"gb_tribunal")
        self.gridLayout_4 = QGridLayout(self.gb_tribunal)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 20, 0, 5)
        self.frm_tribunal_index = QFrame(self.gb_tribunal)
        self.frm_tribunal_index.setObjectName(u"frm_tribunal_index")
        self.frm_tribunal_index.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_tribunal_index.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frm_tribunal_index)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_8 = QLineEdit(self.frm_tribunal_index)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_25 = QLabel(self.frm_tribunal_index)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_25)


        self.gridLayout_4.addWidget(self.frm_tribunal_index, 5, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 10, 1, 1, 1)

        self.frm_tribunal_date = QFrame(self.gb_tribunal)
        self.frm_tribunal_date.setObjectName(u"frm_tribunal_date")
        self.frm_tribunal_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_date.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_7 = QFormLayout(self.frm_tribunal_date)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.formLayout_7.setHorizontalSpacing(0)
        self.formLayout_7.setVerticalSpacing(0)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frm_tribunal_date)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_7.setWidget(0, QFormLayout.SpanningRole, self.label_21)

        self.dateEdit_2 = QDateEdit(self.frm_tribunal_date)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        sizePolicy5.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy5)
        self.dateEdit_2.setCalendarPopup(True)

        self.formLayout_7.setWidget(1, QFormLayout.SpanningRole, self.dateEdit_2)


        self.gridLayout_4.addWidget(self.frm_tribunal_date, 0, 0, 1, 2)

        self.frm_tribunal_table = QFrame(self.gb_tribunal)
        self.frm_tribunal_table.setObjectName(u"frm_tribunal_table")
        self.frm_tribunal_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_table.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frm_tribunal_table)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frm_tribunal_table)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_4.setWidget(0, QFormLayout.SpanningRole, self.label_24)

        self.lineEdit_7 = QLineEdit(self.frm_tribunal_table)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_7)


        self.gridLayout_4.addWidget(self.frm_tribunal_table, 4, 0, 1, 2)

        self.frm_tribunal_room = QFrame(self.gb_tribunal)
        self.frm_tribunal_room.setObjectName(u"frm_tribunal_room")
        self.frm_tribunal_room.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_room.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_14 = QFormLayout(self.frm_tribunal_room)
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.formLayout_14.setHorizontalSpacing(0)
        self.formLayout_14.setVerticalSpacing(0)
        self.formLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frm_tribunal_room)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_14.setWidget(0, QFormLayout.SpanningRole, self.label_12)

        self.lineEdit_11 = QLineEdit(self.frm_tribunal_room)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_14.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_11)


        self.gridLayout_4.addWidget(self.frm_tribunal_room, 14, 0, 1, 2)

        self.frm_tribunal_number = QFrame(self.gb_tribunal)
        self.frm_tribunal_number.setObjectName(u"frm_tribunal_number")
        self.frm_tribunal_number.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_number.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frm_tribunal_number)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_9 = QLineEdit(self.frm_tribunal_number)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_10 = QLabel(self.frm_tribunal_number)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)


        self.gridLayout_4.addWidget(self.frm_tribunal_number, 7, 0, 1, 2)

        self.frm_tribunal_session_date = QFrame(self.gb_tribunal)
        self.frm_tribunal_session_date.setObjectName(u"frm_tribunal_session_date")
        self.frm_tribunal_session_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_session_date.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frm_tribunal_session_date)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setHorizontalSpacing(0)
        self.formLayout_5.setVerticalSpacing(0)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frm_tribunal_session_date)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFrameShape(QFrame.Shape.NoFrame)

        self.formLayout_5.setWidget(0, QFormLayout.SpanningRole, self.label_26)

        self.dateEdit_3 = QDateEdit(self.frm_tribunal_session_date)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        sizePolicy5.setHeightForWidth(self.dateEdit_3.sizePolicy().hasHeightForWidth())
        self.dateEdit_3.setSizePolicy(sizePolicy5)

        self.formLayout_5.setWidget(1, QFormLayout.SpanningRole, self.dateEdit_3)


        self.gridLayout_4.addWidget(self.frm_tribunal_session_date, 11, 0, 1, 2)

        self.frm_tribunal = QFrame(self.gb_tribunal)
        self.frm_tribunal.setObjectName(u"frm_tribunal")
        self.frm_tribunal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frm_tribunal)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frm_tribunal)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon)

        self.gridLayout_17.addWidget(self.pushButton_8, 3, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.frm_tribunal)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy5.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy5)

        self.gridLayout_17.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frm_tribunal)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_17.addWidget(self.label_5, 2, 1, 1, 2)


        self.gridLayout_4.addWidget(self.frm_tribunal, 2, 0, 1, 2)

        self.gb_tribunal_registary = QGroupBox(self.gb_tribunal)
        self.gb_tribunal_registary.setObjectName(u"gb_tribunal_registary")
        self.gridLayout_5 = QGridLayout(self.gb_tribunal_registary)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 20, 0, 0)
        self.comboBox_3 = QComboBox(self.gb_tribunal_registary)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy5.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy5)

        self.gridLayout_5.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.gb_tribunal_registary)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setIcon(icon)

        self.gridLayout_5.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.dateEdit_4 = QDateEdit(self.gb_tribunal_registary)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setCalendarPopup(True)

        self.gridLayout_5.addWidget(self.dateEdit_4, 3, 1, 1, 2)

        self.label_15 = QLabel(self.gb_tribunal_registary)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 2, 1, 1, 2)

        self.label_14 = QLabel(self.gb_tribunal_registary)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 1, 1, 2)


        self.gridLayout_4.addWidget(self.gb_tribunal_registary, 9, 1, 1, 1)

        self.frm_tribunal_section = QFrame(self.gb_tribunal)
        self.frm_tribunal_section.setObjectName(u"frm_tribunal_section")
        self.frm_tribunal_section.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_section.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frm_tribunal_section)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frm_tribunal_section)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_18.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frm_tribunal_section)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon)

        self.gridLayout_18.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.label_20 = QLabel(self.frm_tribunal_section)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_18.addWidget(self.label_20, 0, 1, 1, 2)


        self.gridLayout_4.addWidget(self.frm_tribunal_section, 3, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 16, 1, 1, 1)

        self.frm_tribunal_hour = QFrame(self.gb_tribunal)
        self.frm_tribunal_hour.setObjectName(u"frm_tribunal_hour")
        self.frm_tribunal_hour.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_hour.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_6 = QFormLayout(self.frm_tribunal_hour)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setHorizontalSpacing(0)
        self.formLayout_6.setVerticalSpacing(0)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frm_tribunal_hour)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_6.setWidget(0, QFormLayout.SpanningRole, self.label_11)

        self.timeEdit_2 = QTimeEdit(self.frm_tribunal_hour)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setCalendarPopup(True)

        self.formLayout_6.setWidget(1, QFormLayout.SpanningRole, self.timeEdit_2)


        self.gridLayout_4.addWidget(self.frm_tribunal_hour, 15, 0, 1, 2)

        self.frm_tribunal_case = QFrame(self.gb_tribunal)
        self.frm_tribunal_case.setObjectName(u"frm_tribunal_case")
        self.frm_tribunal_case.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_tribunal_case.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_15 = QFormLayout(self.frm_tribunal_case)
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.formLayout_15.setHorizontalSpacing(0)
        self.formLayout_15.setVerticalSpacing(0)
        self.formLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_12 = QLineEdit(self.frm_tribunal_case)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_15.setWidget(1, QFormLayout.SpanningRole, self.lineEdit_12)

        self.label_13 = QLabel(self.frm_tribunal_case)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_15.setWidget(0, QFormLayout.SpanningRole, self.label_13)


        self.gridLayout_4.addWidget(self.frm_tribunal_case, 13, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 8, 1, 1, 1)


        self.horizontalLayout.addWidget(self.gb_tribunal)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.groupBox_7 = QGroupBox(self.frame_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_3 = QTextEdit(self.groupBox_7)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy1.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy1)
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_5.addWidget(self.textEdit_3)


        self.verticalLayout_6.addWidget(self.groupBox_7)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.splitter.addWidget(self.widget_right)

        self.verticalLayout_3.addWidget(self.splitter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(page_documents)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_documents)
    # setupUi

    def retranslateUi(self, page_documents):
        page_documents.setWindowTitle(QCoreApplication.translate("page_documents", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("page_documents", u"\u062d\u062f\u062f \u0627\u0644\u0645\u062d\u0636\u0631", None))
        self.toolButton.setText(QCoreApplication.translate("page_documents", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("page_documents", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("page_documents", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("page_documents", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0637\u0627\u0644\u0628", None))
        self.cb_client.setPlaceholderText(QCoreApplication.translate("page_documents", u"\u062a\u062d\u062f\u064a\u062f \u0623\u0648 \u0625\u0636\u0627\u0641\u0629 \u0639\u0645\u064a\u0644 \u062c\u062f\u064a\u062f", None))
        self.pb_add_client.setText("")
        self.label_2.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_9.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0639\u0645\u064a\u0644", None))
        self.label_3.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("page_documents", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u0628\u0644\u063a \u0644\u0647", None))
        self.label_8.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0625\u0633\u0645 \u0648 \u0627\u0644\u0644\u0642\u0628", None))
        self.label_7.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.gb_council.setTitle(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0645\u062c\u0644\u0633", None))
        self.label_43.setText(QCoreApplication.translate("page_documents", u"\u0642\u0636\u064a\u0629 \u0631\u0642\u0645", None))
        self.label_41.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0633\u0627\u0639\u0629", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("page_documents", u"HH:mm", None))
        self.label_18.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.pushButton_9.setText("")
        self.label.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0645\u062c\u0644\u0633", None))
        self.label_22.setText(QCoreApplication.translate("page_documents", u"\u062c\u062f\u0648\u0644", None))
        self.label_42.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0642\u0627\u0639\u0629", None))
        self.label_44.setText(QCoreApplication.translate("page_documents", u"\u0628\u0627\u0631\u064a\u062e \u0627\u0644\u062c\u0644\u0633\u0629", None))
        self.pushButton_7.setText("")
        self.label_16.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u063a\u0631\u0641\u0629", None))
        self.label_23.setText(QCoreApplication.translate("page_documents", u"\u0641\u0647\u0631\u0633", None))
        self.gb_council_registary.setTitle(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0645\u0633\u062c\u0644 \u0628\u0623\u0645\u0627\u064a\u0629 \u0636\u0628\u0637", None))
        self.pushButton_12.setText("")
        self.label_28.setText(QCoreApplication.translate("page_documents", u"\u0628\u062a\u0627\u0631\u064a\u062e", None))
        self.label_27.setText(QCoreApplication.translate("page_documents", u"\u0645\u062c\u0644\u0633", None))
        self.gb_tribunal.setTitle(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0645\u062d\u0643\u0645\u0629", None))
        self.label_25.setText(QCoreApplication.translate("page_documents", u"\u0641\u0647\u0631\u0633", None))
        self.label_21.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u062a\u0627\u0631\u064a\u062e", None))
        self.label_24.setText(QCoreApplication.translate("page_documents", u"\u062c\u062f\u0648\u0644", None))
        self.label_12.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0642\u0627\u0639\u0629", None))
        self.label_10.setText(QCoreApplication.translate("page_documents", u"\u0631\u0642\u0645", None))
        self.label_26.setText(QCoreApplication.translate("page_documents", u"\u0628\u0627\u0631\u064a\u062e \u0627\u0644\u062c\u0644\u0633\u0629", None))
        self.pushButton_8.setText("")
        self.label_5.setText(QCoreApplication.translate("page_documents", u"\u0645\u062d\u0643\u0645\u0629", None))
        self.gb_tribunal_registary.setTitle(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0645\u0633\u062c\u0644 \u0628\u0623\u0645\u0627\u064a\u0629 \u0636\u0628\u0637", None))
        self.pushButton_11.setText("")
        self.label_15.setText(QCoreApplication.translate("page_documents", u"\u0628\u062a\u0627\u0631\u064a\u062e", None))
        self.label_14.setText(QCoreApplication.translate("page_documents", u"\u0645\u062d\u0643\u0645\u0629", None))
        self.pushButton_10.setText("")
        self.label_20.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0642\u0633\u0645", None))
        self.label_11.setText(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0633\u0627\u0639\u0629", None))
        self.label_13.setText(QCoreApplication.translate("page_documents", u"\u0642\u0636\u064a\u0629 \u0631\u0642\u0645", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("page_documents", u"\u0627\u0644\u0646\u0635", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("page_documents", u"\u0645\u062d\u0636\u0631 \u062c\u062f\u064a\u062f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("page_documents", u"\u0642\u0627\u0626\u0645\u0629 \u0627\u0644\u0645\u062d\u0627\u0636\u0631", None))
    # retranslateUi

