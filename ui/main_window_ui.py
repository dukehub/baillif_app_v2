# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import ui.resources_rc
import ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 860)
        MainWindow.setStyleSheet(u"#frame_header {\n"
"	background-color: #e5e7eb\n"
"}\n"
"#frame_header QLabel {\n"
"	color: #fff;\n"
"	background-color: transparent;\n"
"}\n"
"#frame_header QPushButton{\n"
"border: none;\n"
"width: 50px;\n"
"height: 40px;\n"
"}\n"
"#lbl_icon {\n"
"min-width: 30px;\n"
"min-height: 30px;\n"
"max-width: 30px;\n"
"max-height: 30px;\n"
"background-color: #fff;\n"
"border-radius: 15px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"#frame_main{\n"
"\n"
"	background-color: rgb(216, 216, 216);\n"
"}\n"
"#pb_maximize:hover, #pb_minimize:hover, #pb_menu:hover {\n"
"	background-color: rgb(216, 216, 216);\n"
"}\n"
"#pb_close:hover {\n"
"	background-color: #c42b1c;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy)
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_main)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(240, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 238, 835))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 100))
        self.label.setMaximumSize(QSize(120, 100))
        self.label.setPixmap(QPixmap(u":/icons/icons/bailiff_logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_full_menu = QWidget(self.scrollAreaWidgetContents)
        self.widget_full_menu.setObjectName(u"widget_full_menu")
        sizePolicy1.setHeightForWidth(self.widget_full_menu.sizePolicy().hasHeightForWidth())
        self.widget_full_menu.setSizePolicy(sizePolicy1)
        self.widget_full_menu.setStyleSheet(u"text-align: left;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_full_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_home = QPushButton(self.widget_full_menu)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pb_home)
        self.pb_home.setObjectName(u"pb_home")
        font1 = QFont()
        font1.setPointSize(12)
        self.pb_home.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/dashboard_layout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_home.setIcon(icon)
        self.pb_home.setIconSize(QSize(24, 24))
        self.pb_home.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_home)

        self.pb_clients_show = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_clients_show)
        self.pb_clients_show.setObjectName(u"pb_clients_show")
        self.pb_clients_show.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_clients_show.setIcon(icon1)
        self.pb_clients_show.setIconSize(QSize(24, 24))
        self.pb_clients_show.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_clients_show)

        self.pb_repports_show = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_repports_show)
        self.pb_repports_show.setObjectName(u"pb_repports_show")
        self.pb_repports_show.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/task.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_repports_show.setIcon(icon2)
        self.pb_repports_show.setIconSize(QSize(24, 24))
        self.pb_repports_show.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_repports_show)

        self.pb_administration = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_administration)
        self.pb_administration.setObjectName(u"pb_administration")
        self.pb_administration.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/business_building.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_administration.setIcon(icon3)
        self.pb_administration.setIconSize(QSize(24, 24))
        self.pb_administration.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_administration)

        self.pb_civil = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_civil)
        self.pb_civil.setObjectName(u"pb_civil")
        self.pb_civil.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/meeting_room.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_civil.setIcon(icon4)
        self.pb_civil.setIconSize(QSize(24, 24))
        self.pb_civil.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_civil)

        self.pb_penal = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_penal)
        self.pb_penal.setObjectName(u"pb_penal")
        self.pb_penal.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/law.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_penal.setIcon(icon5)
        self.pb_penal.setIconSize(QSize(24, 24))
        self.pb_penal.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_penal)

        self.pb_acts = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_acts)
        self.pb_acts.setObjectName(u"pb_acts")
        self.pb_acts.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/contract.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_acts.setIcon(icon6)
        self.pb_acts.setIconSize(QSize(24, 24))
        self.pb_acts.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_acts)

        self.pb_execution = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_execution)
        self.pb_execution.setObjectName(u"pb_execution")
        self.pb_execution.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/police.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_execution.setIcon(icon7)
        self.pb_execution.setIconSize(QSize(24, 24))
        self.pb_execution.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_execution)

        self.pb_auction = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_auction)
        self.pb_auction.setObjectName(u"pb_auction")
        self.pb_auction.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/auctionist.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_auction.setIcon(icon8)
        self.pb_auction.setIconSize(QSize(24, 24))
        self.pb_auction.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_auction)

        self.pb_archives = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_archives)
        self.pb_archives.setObjectName(u"pb_archives")
        self.pb_archives.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/binders.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_archives.setIcon(icon9)
        self.pb_archives.setIconSize(QSize(24, 24))
        self.pb_archives.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_archives)

        self.verticalSpacer = QSpacerItem(20, 373, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pb_control = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_control)
        self.pb_control.setObjectName(u"pb_control")
        self.pb_control.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_control.setIcon(icon10)
        self.pb_control.setIconSize(QSize(24, 24))
        self.pb_control.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_control)

        self.pb_exit = QPushButton(self.widget_full_menu)
        self.buttonGroup.addButton(self.pb_exit)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_exit.setIcon(icon11)
        self.pb_exit.setIconSize(QSize(24, 24))
        self.pb_exit.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pb_exit)


        self.verticalLayout_4.addWidget(self.widget_full_menu)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.widget = QWidget(self.frame_main)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(6)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pb_menu = QPushButton(self.widget_2)
        self.pb_menu.setObjectName(u"pb_menu")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/squared_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_menu.setIcon(icon12)
        self.pb_menu.setIconSize(QSize(20, 20))
        self.pb_menu.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pb_menu)

        self.lbl_page_title = QLabel(self.widget_2)
        self.lbl_page_title.setObjectName(u"lbl_page_title")
        self.lbl_page_title.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lbl_page_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pb_settings = QPushButton(self.widget_2)
        self.pb_settings.setObjectName(u"pb_settings")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/gears.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_settings.setIcon(icon13)
        self.pb_settings.setIconSize(QSize(20, 20))
        self.pb_settings.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pb_settings)

        self.pb_notification = QPushButton(self.widget_2)
        self.pb_notification.setObjectName(u"pb_notification")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/notification.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_notification.setIcon(icon14)
        self.pb_notification.setIconSize(QSize(20, 20))
        self.pb_notification.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pb_notification)

        self.pb_infos = QPushButton(self.widget_2)
        self.pb_infos.setObjectName(u"pb_infos")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_infos.setIcon(icon15)
        self.pb_infos.setIconSize(QSize(20, 20))
        self.pb_infos.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pb_infos)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.widget)


        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.pb_menu.toggled.connect(self.scrollArea.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bailiff App", None))
        self.label.setText("")
        self.pb_home.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629", None))
        self.pb_clients_show.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u0645\u0644\u0627\u0621", None))
        self.pb_repports_show.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062d\u0636\u0631 \u062a\u0643\u0644\u064a\u0641", None))
        self.pb_administration.setText(QCoreApplication.translate("MainWindow", u"\u0625\u062f\u0627\u0631\u064a", None))
        self.pb_civil.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062f\u0646\u064a", None))
        self.pb_penal.setText(QCoreApplication.translate("MainWindow", u"\u062c\u0640\u0632\u0627\u0626\u064a", None))
        self.pb_acts.setText(QCoreApplication.translate("MainWindow", u"\u0639\u0642\u0648\u062f \u063a\u064a\u0631 \u0642\u0636\u0627\u0626\u064a\u0629", None))
        self.pb_execution.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062a\u064a\u0641\u064a\u0630", None))
        self.pb_auction.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0640\u0640\u0632\u0627\u062f", None))
        self.pb_archives.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0623\u0631\u0634\u064a\u0641", None))
        self.pb_control.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0625\u0639\u062f\u0627\u062f\u0627\u062a", None))
        self.pb_exit.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062e\u0631\u0648\u062c", None))
        self.pb_menu.setText("")
        self.lbl_page_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pb_settings.setText("")
        self.pb_notification.setText("")
        self.pb_infos.setText("")
    # retranslateUi

