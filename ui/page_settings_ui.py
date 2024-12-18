# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_settings.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QWidget)

class Ui_page_settings(object):
    def setupUi(self, page_settings):
        if not page_settings.objectName():
            page_settings.setObjectName(u"page_settings")
        page_settings.resize(875, 835)
        self.horizontalLayout = QHBoxLayout(page_settings)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(page_settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_bailiff_info = QWidget()
        self.tab_bailiff_info.setObjectName(u"tab_bailiff_info")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_bailiff_info)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_bailiff = QFrame(self.tab_bailiff_info)
        self.frm_bailiff.setObjectName(u"frm_bailiff")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_bailiff.sizePolicy().hasHeightForWidth())
        self.frm_bailiff.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.frm_bailiff)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.gridLayout.setVerticalSpacing(15)
        self.label_3 = QLabel(self.frm_bailiff)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frm_bailiff)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frm_bailiff)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frm_bailiff)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frm_bailiff)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)

        self.label = QLabel(self.frm_bailiff)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frm_bailiff)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 2, 1, 1, 3)

        self.label_4 = QLabel(self.frm_bailiff)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.textEdit = QTextEdit(self.frm_bailiff)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 3)

        self.label_5 = QLabel(self.frm_bailiff)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 3)

        self.lineEdit_3 = QLineEdit(self.frm_bailiff)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frm_bailiff)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frm_bailiff)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frm_bailiff)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 6, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frm_bailiff)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.tabWidget.addTab(self.tab_bailiff_info, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(page_settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(page_settings)
    # setupUi

    def retranslateUi(self, page_settings):
        page_settings.setWindowTitle(QCoreApplication.translate("page_settings", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0647\u0627\u0628\u0641", None))
        self.label_2.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0644\u0642\u0628", None))
        self.label_7.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0645\u0633\u062c\u0644 \u0628\u0640", None))
        self.label.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0625\u0633\u0645", None))
        self.label_4.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0639\u0646\u0648\u0627\u0646", None))
        self.label_5.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a", None))
        self.label_6.setText(QCoreApplication.translate("page_settings", u"\u0627\u0644\u062c\u0648\u0627\u0644", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bailiff_info), QCoreApplication.translate("page_settings", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0645\u062d\u0636\u0631", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("page_settings", u"\u0625\u0639\u062f\u0627\u062f\u0627\u062a", None))
    # retranslateUi

