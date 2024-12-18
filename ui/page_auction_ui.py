# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_auction.ui'
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

class Ui_page_auction(object):
    def setupUi(self, page_auction):
        if not page_auction.objectName():
            page_auction.setObjectName(u"page_auction")
        page_auction.resize(400, 300)
        self.label = QLabel(page_auction)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 120, 151, 71))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.retranslateUi(page_auction)

        QMetaObject.connectSlotsByName(page_auction)
    # setupUi

    def retranslateUi(self, page_auction):
        page_auction.setWindowTitle(QCoreApplication.translate("page_auction", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_auction", u"Auction", None))
    # retranslateUi

