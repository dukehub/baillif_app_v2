# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_page_dashboard(object):
    def setupUi(self, page_dashboard):
        if not page_dashboard.objectName():
            page_dashboard.setObjectName(u"page_dashboard")
        page_dashboard.resize(642, 451)
        self.label = QLabel(page_dashboard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 200, 151, 71))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.retranslateUi(page_dashboard)

        QMetaObject.connectSlotsByName(page_dashboard)
    # setupUi

    def retranslateUi(self, page_dashboard):
        page_dashboard.setWindowTitle(QCoreApplication.translate("page_dashboard", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_dashboard", u"Dashboard", None))
    # retranslateUi

