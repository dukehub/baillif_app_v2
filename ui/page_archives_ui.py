# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_archives.ui'
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
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSplitter, QToolButton,
    QTreeView, QVBoxLayout, QWidget)
import ui.resources_rc

class Ui_page_archives(object):
    def setupUi(self, page_archives):
        if not page_archives.objectName():
            page_archives.setObjectName(u"page_archives")
        page_archives.resize(907, 735)
        self.verticalLayout_2 = QVBoxLayout(page_archives)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(page_archives)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_add_box = QToolButton(self.frame)
        self.tb_add_box.setObjectName(u"tb_add_box")
        icon = QIcon()
        icon.addFile(u":/icons/icons/binder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_add_box.setIcon(icon)
        self.tb_add_box.setIconSize(QSize(24, 24))
        self.tb_add_box.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_add_box.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.tb_add_box)

        self.tb_add_archive = QToolButton(self.frame)
        self.tb_add_archive.setObjectName(u"tb_add_archive")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/create_archive.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_add_archive.setIcon(icon1)
        self.tb_add_archive.setIconSize(QSize(24, 24))
        self.tb_add_archive.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_add_archive.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.tb_add_archive)

        self.tb_delete_archive = QToolButton(self.frame)
        self.tb_delete_archive.setObjectName(u"tb_delete_archive")
        self.tb_delete_archive.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/delete_archive.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_delete_archive.setIcon(icon2)
        self.tb_delete_archive.setIconSize(QSize(24, 24))
        self.tb_delete_archive.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_delete_archive.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.tb_delete_archive)

        self.tb_print = QToolButton(self.frame)
        self.tb_print.setObjectName(u"tb_print")
        self.tb_print.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tb_print.setIcon(icon3)
        self.tb_print.setIconSize(QSize(24, 24))
        self.tb_print.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.tb_print.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.tb_print)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(page_archives)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(450, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.le_filter = QLineEdit(self.frame_2)
        self.le_filter.setObjectName(u"le_filter")
        self.le_filter.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.le_filter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tree_view_pdf = QTreeView(self.frame_2)
        self.tree_view_pdf.setObjectName(u"tree_view_pdf")
        self.tree_view_pdf.setLineWidth(1)
        self.tree_view_pdf.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tree_view_pdf.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_view_pdf.setAlternatingRowColors(True)
        self.tree_view_pdf.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tree_view_pdf.setIconSize(QSize(24, 24))
        self.tree_view_pdf.setIndentation(20)
        self.tree_view_pdf.setAnimated(True)
        self.tree_view_pdf.setWordWrap(True)

        self.verticalLayout.addWidget(self.tree_view_pdf)

        self.splitter.addWidget(self.frame_2)
        self.pdf_viewer = QPdfView(self.splitter)
        self.pdf_viewer.setObjectName(u"pdf_viewer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pdf_viewer.sizePolicy().hasHeightForWidth())
        self.pdf_viewer.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.pdf_viewer)

        self.horizontalLayout_2.addWidget(self.splitter)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.retranslateUi(page_archives)

        QMetaObject.connectSlotsByName(page_archives)
    # setupUi

    def retranslateUi(self, page_archives):
        page_archives.setWindowTitle(QCoreApplication.translate("page_archives", u"Form", None))
        self.tb_add_box.setText(QCoreApplication.translate("page_archives", u"\u0625\u0636\u0627\u0641\u0629 \u0639\u0644\u0628\u0629", None))
        self.tb_add_archive.setText(QCoreApplication.translate("page_archives", u"\u0623\u0631\u0634\u064a\u0641 \u062c\u062f\u064a\u062f", None))
        self.tb_delete_archive.setText(QCoreApplication.translate("page_archives", u"\u062d\u0630\u0641 \u0627\u0644\u0623\u0631\u0634\u064a\u0641", None))
        self.tb_print.setText(QCoreApplication.translate("page_archives", u"\u0637\u0628\u0627\u0639\u0629", None))
        self.label.setText(QCoreApplication.translate("page_archives", u"\u0628\u062d\u062b", None))
        self.le_filter.setPlaceholderText(QCoreApplication.translate("page_archives", u"\u0628\u062d\u062b...", None))
    # retranslateUi

