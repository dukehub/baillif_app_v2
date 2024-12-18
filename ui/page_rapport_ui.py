# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_rapport.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QTableView, QToolButton,
    QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_page_rapports(object):
    def setupUi(self, page_rapports):
        if not page_rapports.objectName():
            page_rapports.setObjectName(u"page_rapports")
        page_rapports.resize(1248, 837)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_rapports.sizePolicy().hasHeightForWidth())
        page_rapports.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(page_rapports)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(page_rapports)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tb_new = QToolButton(self.frame_4)
        self.tb_new.setObjectName(u"tb_new")
        icon = QIcon()
        icon.addFile(u":/icons/icons/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_new.setIcon(icon)
        self.tb_new.setIconSize(QSize(24, 24))
        self.tb_new.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_new.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_new)

        self.tb_edit = QToolButton(self.frame_4)
        self.tb_edit.setObjectName(u"tb_edit")
        self.tb_edit.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_text_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_edit.setIcon(icon1)
        self.tb_edit.setIconSize(QSize(24, 24))
        self.tb_edit.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_edit.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_edit)

        self.tb_delete = QToolButton(self.frame_4)
        self.tb_delete.setObjectName(u"tb_delete")
        self.tb_delete.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_delete.setIcon(icon2)
        self.tb_delete.setIconSize(QSize(24, 24))
        self.tb_delete.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_delete.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_delete)

        self.tb_preview = QToolButton(self.frame_4)
        self.tb_preview.setObjectName(u"tb_preview")
        self.tb_preview.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/view.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_preview.setIcon(icon3)
        self.tb_preview.setIconSize(QSize(24, 24))
        self.tb_preview.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_preview.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_preview)

        self.tb_print = QToolButton(self.frame_4)
        self.tb_print.setObjectName(u"tb_print")
        self.tb_print.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_print.setIcon(icon4)
        self.tb_print.setIconSize(QSize(24, 24))
        self.tb_print.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_print.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.tb_print)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_7 = QFrame(page_rapports)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_7)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.le_filter = QLineEdit(self.frame_8)
        self.le_filter.setObjectName(u"le_filter")

        self.horizontalLayout_5.addWidget(self.le_filter)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.tableView_dossiers = QTableView(self.widget)
        self.tableView_dossiers.setObjectName(u"tableView_dossiers")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView_dossiers.sizePolicy().hasHeightForWidth())
        self.tableView_dossiers.setSizePolicy(sizePolicy3)
        self.tableView_dossiers.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tableView_dossiers.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView_dossiers.setAlternatingRowColors(True)
        self.tableView_dossiers.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView_dossiers.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView_dossiers.setSortingEnabled(True)

        self.verticalLayout_4.addWidget(self.tableView_dossiers)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_5.addWidget(self.frame_7)

        QWidget.setTabOrder(self.tb_new, self.tb_edit)
        QWidget.setTabOrder(self.tb_edit, self.tb_preview)
        QWidget.setTabOrder(self.tb_preview, self.tableView_dossiers)

        self.retranslateUi(page_rapports)

        QMetaObject.connectSlotsByName(page_rapports)
    # setupUi

    def retranslateUi(self, page_rapports):
        page_rapports.setWindowTitle(QCoreApplication.translate("page_rapports", u"Form", None))
        self.tb_new.setText(QCoreApplication.translate("page_rapports", u"\u062c\u062f\u064a\u062f", None))
        self.tb_edit.setText(QCoreApplication.translate("page_rapports", u"\u062a\u0639\u062f\u064a\u0644", None))
        self.tb_delete.setText(QCoreApplication.translate("page_rapports", u"\u062d\u0630\u0641", None))
        self.tb_preview.setText(QCoreApplication.translate("page_rapports", u"\u062a\u062f\u0642\u064a\u0642", None))
        self.tb_print.setText(QCoreApplication.translate("page_rapports", u"\u0637\u0628\u0627\u0639\u0629", None))
        self.label_6.setText(QCoreApplication.translate("page_rapports", u"\u0628\u062d\u062b", None))
    # retranslateUi

