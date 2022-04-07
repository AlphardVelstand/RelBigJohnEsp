# Bibliotecas
from datetime import datetime

import pandas as pd
from pandas import read_excel
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
import datetime
from datetime import datetime
import time
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
global dataIniStrtoData
global dataFinStrtoData

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
    global tabela_pedidoos
    global tabela_pedidos
    global FaturamentoPorDia
    global faturamento, total_entregas, incentivo_iffod, incentivo_restaurante
    global TabelaFitradaPorData
    global dataIniStrtoData
    global dataFinStrtoData
    #global dataIni = dataIniStrtoData
    #global dataFin
    #tabela_pedidos = pd.read_excel('lista-de-pedidos.xlsx')
    #tabela_pedidoos = QFileDialog.setReadOnly()

    #tabela_pedidoos = QFileDialog.getOpenFileNames()
    tabela_pedidos = pd.read_excel = QFileDialog.getOpenFileNames()
    #Capturando a data e Convertendo para D/M/A
    hoje = datetime.today()
    print(hoje)
    printHoje = hoje.strftime("%d/%m/%Y %H:%M:%S")
    print(printHoje)

    #tabela_pedidos = pandas.read_excel(f'{tabela_pedidoos}')

    #tabela_pedidos = pd.read_excel(r'{tabela_pedidos}', engine='openpyxl')
    #tabela_pedidos = pd.ExcelFile(tabela_pedidos)
    #tabela_pedidos = pd.ExcelFile(f'{tabela_pedidoos}')
    print(tabela_pedidos)

    #gerarCorpoEmail

def gerarCorpoEmail():
    global tabela_pedidoos, tabela_pedidos, FaturamentoPorDia
    global faturamento, total_entregas, incentivo_iffod, incentivo_restaurante
    global TabelaFitradaPorData, dataIni, dataFin
    #tabela_pedidos = pd.read_excel(f'{tabela_pedidoos}')
    #print(type(tabela_pedidos))

    print(dataIni, dataFin)

    # Filtro para selecionar a data
    TabelaFitradaPorData = tabela_pedidos[
        (tabela_pedidos['DATA'] >= f'{dataIni}') & (tabela_pedidos['DATA'] <= f'{dataFin}')]

    # Selecionando por dia
    FaturamentoPorDia = TabelaFitradaPorData[['DATA PEDIDO', 'RESTAURANTE', 'TOTAL DO PARCEIRO']].groupby(
        'DATA PEDIDO').sum()
    print("Relatorio gerado")

#Função que gera o relatório
def gerarRelatorio(self):
    global tabela_pedidoos
    global tabela_pedidos
    global FaturamentoPorDia
    global faturamento, total_entregas, incentivo_iffod, incentivo_restaurante
    global TabelaFitradaPorData
    global dataIni
    global dataFin
    global dataIniStrtoData
    global dataFinStrtoData
    #Selecionando o QLineEdit e armazenadno o texto dele nas variaveis
    dataIniStrtoData = window.lineEditDataIni.text()
    dataFinStrtoData = window.lineEditDataFin.text()

    dataIni = datetime.strptime(f"{dataIniStrtoData}", '%d-%m-%Y')
    dataFin = datetime.strptime(f"{dataFinStrtoData}", '%d-%m-%Y')
    #print(type(dataIni, dataFin))

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
    global tabela_pedidoos
    global tabela_pedidos
    global FaturamentoPorDia
    global faturamento, total_entregas, incentivo_iffod, incentivo_restaurante
    global TabelaFitradaPorData
    global dataIni
    global dataFin

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
