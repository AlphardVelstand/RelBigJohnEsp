# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UiFrameMain.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 392)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 361, 371))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(self.frame)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(10, 10, 341, 31))
        font = QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.titulo.setFont(font)
        self.titulo.setLayoutDirection(Qt.LeftToRight)
        self.btnGerarRel = QPushButton(self.frame)
        self.btnGerarRel.setObjectName(u"btnGerarRel")
        self.btnGerarRel.setGeometry(QRect(20, 220, 141, 41))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(13)
        self.btnGerarRel.setFont(font1)
        self.btnGerarRel.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.EnvRelEmailButton = QPushButton(self.frame)
        self.EnvRelEmailButton.setObjectName(u"EnvRelEmailButton")
        self.EnvRelEmailButton.setGeometry(QRect(190, 220, 151, 41))
        self.EnvRelEmailButton.setFont(font1)
        self.EnvRelEmailButton.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(130, 280, 91, 41))
        self.btn_sair.setFont(font1)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 161, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 340, 131, 20))
        self.lineEditDataIni = QLineEdit(self.frame)
        self.lineEditDataIni.setObjectName(u"lineEditDataIni")
        self.lineEditDataIni.setGeometry(QRect(130, 140, 221, 20))
        self.lineEditDataFin = QLineEdit(self.frame)
        self.lineEditDataFin.setObjectName(u"lineEditDataFin")
        self.lineEditDataFin.setGeometry(QRect(130, 180, 221, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 111, 16))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 111, 16))
        self.label_4.setFont(font3)
        self.btnSelArq = QPushButton(self.frame)
        self.btnSelArq.setObjectName(u"btnSelArq")
        self.btnSelArq.setGeometry(QRect(130, 90, 91, 31))
        font4 = QFont()
        font4.setFamily(u"MV Boli")
        font4.setPointSize(11)
        self.btnSelArq.setFont(font4)
        self.btnSelArq.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(209,209,209);\n"
"	border-radius: 15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(9,125,235);\n"
"	color: #fff;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titulo.setText(QCoreApplication.translate("Form", u"Gerador de Ralat\u00f3rios", None))
        self.btnGerarRel.setText(QCoreApplication.translate("Form", u"Gerar Relat\u00f3rio", None))
        self.EnvRelEmailButton.setText(QCoreApplication.translate("Form", u"Enviar por Email", None))
        self.btn_sair.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.label.setText(QCoreApplication.translate("Form", u"Selecione o arquivo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Desenvolvido por Alphard", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">DATA FINAL</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">DATA INICIAL</span></p></body></html>", None))
        self.btnSelArq.setText(QCoreApplication.translate("Form", u"Arquivo", None))
    # retranslateUi

