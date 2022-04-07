# Bibliotecas
from datetime import datetime
import pandas as pd
import smtplib
import email.message
import time
from tkinter import *
from PySide2.QtWidgets import *#Responsavel por chamar a caixa de dialogo para selecionar o arquivo
from tkinter import messagebox, filedialog
from tkinter import filedialog as dlg
#from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtGui import QIcon
from ui_main import Ui_Form
import sys
import pandas as pd
import re
import requests
import urllib
import os

global tabela_pedidoos
global tabela_pedidos
global FaturamentoPorDia
global faturamento, total_entregas, incentivo_iffod, incentivo_restaurante
global TabelaFitradaPorData
global dataIni
global dataFin

#Clase principal
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerador de Reltórios Big John")

    #chamando a função fechar janela ao clicar no botao
        self.btn_sair.clicked.connect(fecharJanela)
    #chamando arquivo base para gerar relatório
        self.btnSelArq.clicked.connect(abrirArquivo)
    #Gerando relatório
        self.btnGerarRel.clicked.connect(gerarRelatorio)
    #Enviando Email com relatorio
        self.EnvRelEmailButton.clicked.connect(enviar_email)

# Função abrir e ler arquivo em excell
def abrirArquivo(self):
    tabela_pedidoos = QFileDialog.getOpenFileNames()
    #window.listWidgetVisu.addItem(tabela_pedidoos)
    #QString tabela_pedidos.read.toString
    #tabela_pedidos = pd.read_excel(f'{tabela_pedidoos}')
    #tabela_pedidos = QFileDialog.getOpenFileNames()
    print(tabela_pedidoos)

    #gerarCorpoEmail

def gerarCorpoEmail():
    tabela_pedidos = pd.read_excel(f'{tabela_pedidoos}')
    #print(type(tabela_pedidos))

    # Filtro para selecionar a data
    TabelaFitradaPorData = tabela_pedidos[
        (tabela_pedidos['DATA'] >= f'{dataIni}') & (tabela_pedidos['DATA'] <= f'{dataFin}')]


    # Selecionando por dia
    FaturamentoPorDia = TabelaFitradaPorData[['DATA PEDIDO', 'RESTAURANTE', 'TOTAL DO PARCEIRO']].groupby(
        'DATA PEDIDO').sum()
    print(FaturamentoPorDia)

#Função que gera o relatório
def gerarRelatorio(self):
    #Selecionando o QLineEdit e armazenadno o texto dele nas variaveis
    dataIni = window.lineEditDataIni.text()
    dataFin = window.lineEditDataFin.text()
    #tabela_pedidos = pd.read_excel(f'{tabela_pedidoos}')
    print(dataIni," atè ", dataFin)
    #gerarCorpoEmail()

    #Validando se os campos nao estao em branco
    if dataIni =='' or dataFin =='':
        msgErro = QMessageBox()
        msgErro.setIcon(QMessageBox.Information)
        msgErro.setWindowTitle("ERRO")
        msgErro.setText("Erro, campo data nao pode estar vazio")
        msgErro.exec_()

    else:
        gerarCorpoEmail()

# Enviar email com relatório
def enviar_email():
    corpo_email = f'''
        <p>'Faturamento por dia:</p>
        <p>{FaturamentoPorDia.to_html()}</p>
 
         '''

    msg = email.message.Message()
    #msg['subject'] = 'teste'
    msg['Subject'] = f'RELATORIO DE FATURAMENTO DOS RESTAURANTES PERIODO: {dataIni} Ate: {dataFin}'
    msg['From'] = 'emonitor@transportadoraroma.com.br'
    # msg['To'] = 'john.big.jota@hotmail.com'  # Destinatario
    msg['To'] = 'jhonathan.silva@gruporomatransportes.com.br'  # Destinatario
    password = 'roma2012'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    enviar_email()
    print("Email enviado")

#função fehar janela
def fecharJanela(self):
    sys.exit()

#chamando tela
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
