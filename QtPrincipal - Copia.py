# Bibliotecas
from datetime import datetime

import pandas as pd
import smtplib
import email.message
import time
from tkinter import *
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox, QtW)
from ui_main import Ui_Form
import sys
import re
import requests
import urllib
import os

#Clase principal
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerador de reltórios Big John")
    #Metodo
    #def gerarReletorio(self):

    #Função abrir e ler arquivo em excell
    def abrirArquivo():
        arquivo = QtW

    #chamando a função fechar janela
        self.btn_sair.clicked.connect(fecharJanela)


#função fehar janela
def fecharJanela(self):
    sys.exit()

#chamando tela
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
