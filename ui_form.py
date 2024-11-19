# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(725, 618)
        self.exitBtn = QPushButton(Widget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(20, 560, 75, 24))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 111, 16))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 121, 16))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 131, 16))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 350, 71, 16))
        self.derivationTxt = QTextBrowser(Widget)
        self.derivationTxt.setObjectName(u"derivationTxt")
        self.derivationTxt.setGeometry(QRect(20, 140, 241, 391))
        self.derivationTxt.setStyleSheet(u"font: 10pt \"MS UI Gothic\";\n"
"font: 700 10pt \"Monospac821 BT\";")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 241, 22))
        self.okBtn = QPushButton(Widget)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(20, 70, 75, 24))
        self.clearBtn = QPushButton(Widget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(120, 560, 75, 24))
        self.syntaxTree = QTextBrowser(Widget)
        self.syntaxTree.setObjectName(u"syntaxTree")
        self.syntaxTree.setGeometry(QRect(310, 30, 401, 311))
        self.syntaxTree.setStyleSheet(u"font: 10pt \"MS UI Gothic\";\n"
"font: 700 10pt \"Monospac821 BT\";")
        self.astTree = QTextBrowser(Widget)
        self.astTree.setObjectName(u"astTree")
        self.astTree.setGeometry(QRect(310, 370, 401, 221))
        self.astTree.setStyleSheet(u"font: 10pt \"MS UI Gothic\";\n"
"font: 700 10pt \"Monospac821 BT\";")

        self.retranslateUi(Widget)
        self.exitBtn.clicked.connect(Widget.close)
        self.clearBtn.clicked.connect(self.derivationTxt.clear)
        self.clearBtn.clicked.connect(self.lineEdit.clear)
        self.clearBtn.clicked.connect(self.astTree.clear)
        self.clearBtn.clicked.connect(self.syntaxTree.clear)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Practice3", None))
        self.exitBtn.setText(QCoreApplication.translate("Widget", u"Exit", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Enter an Expression", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Syntax Tree", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Derivation Process", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"AST Tree", None))
        self.okBtn.setText(QCoreApplication.translate("Widget", u"Ok", None))
        self.clearBtn.setText(QCoreApplication.translate("Widget", u"Clear", None))
    # retranslateUi

