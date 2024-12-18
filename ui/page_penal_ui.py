# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_penal.ui'
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

class Ui_page_penal(object):
    def setupUi(self, page_penal):
        if not page_penal.objectName():
            page_penal.setObjectName(u"page_penal")
        page_penal.resize(400, 300)
        self.label = QLabel(page_penal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 120, 151, 71))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.retranslateUi(page_penal)

        QMetaObject.connectSlotsByName(page_penal)
    # setupUi

    def retranslateUi(self, page_penal):
        page_penal.setWindowTitle(QCoreApplication.translate("page_penal", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_penal", u"Penal", None))
    # retranslateUi

