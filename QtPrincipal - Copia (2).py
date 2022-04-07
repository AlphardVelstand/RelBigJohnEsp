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
import re
import requests
import urllib
import os

#Clase principal
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerador de Reltórios Big John")
    #Metodo
    #def gerarReletorio(self):

    #chamando a função fechar janela ao clicar no botao
        self.btn_sair.clicked.connect(fecharJanela)
    #chamando arquivo base para gerar relatório
        self.btnSelArq.clicked.connect(abrirArquivo)
    #Gerando relatório
        self.btnGerarRel.clicked.connect(gerarRelatorio)

# Função abrir e ler arquivo em excell
def abrirArquivo(self):
    files = QFileDialog.getOpenFileNames()
    print(files)

#Função que gera o relatório
def gerarRelatorio(self):
    #Selecionando o QLineEdit e armazenadno o texto dele nas variaveis
    dataIni = window.lineEditDataIni.text()
    dataFin = window.lineEditDataFin.text()
    print(dataIni, dataFin)

    #Validando se os campos nao estao em branco
    if dataIni =='' or dataFin =='':
        msgErro = QMessageBox()
        msgErro.setIcon(QMessageBox.Information)
        msgErro.setWindowTitle("ERRO")
        msgErro.setText("Erro, campo data nao pode estar vazio")
        msgErro.exec_()

    else:
        gerarCorpoEmail()

def gerarCorpoEmail():
    # Filtro para selecionar a data
    TabelaFitradaPorData = tabela_pedidos[
        (tabela_pedidos['DATA'] >= f'{dataIn}') & (tabela_pedidos['DATA'] <= f'{dataFinal}')]
    # print(tabela_pedidos)

    # Selecionando por dia
    FaturamentoPorDia = TabelaFitradaPorData[['DATA PEDIDO', 'RESTAURANTE', 'TOTAL DO PARCEIRO']].groupby(
        'DATA PEDIDO').sum()
    # FaturamentoPorDia = tabela_pedidos[['DATA PEDIDO', 'RESTAURANTE', 'TOTAL DO PARCEIRO']].groupby('DATA PEDIDO').sum()
    # print('Faturamento por dia: ',FaturamentoPorDia)

    # Faturamento por restaurante
    faturamento = TabelaFitradaPorData[['RESTAURANTE', 'TOTAL DO PARCEIRO']].groupby('RESTAURANTE').sum()
    # print("Faturamento por restaurante: ",faturamento)

    # Quantidade de produtos vendidos para entrega ou retirada
    # tipo_entrega = tabela_pedidos[['RESTAURANTE','TIPO DE PEDIDO']].groupby('RESTAURANTE').sum()
    # print(tipo_entrega)

    # Total de entregas e valor
    total_entregas = TabelaFitradaPorData[['RESTAURANTE', 'TAXA DE ENTREGA']].groupby('RESTAURANTE').sum()
    # print("Total faturado nas entregas: ",total_entregas)

    # Total de incentivo IFOOD
    incentivo_iffod = TabelaFitradaPorData[['RESTAURANTE', 'INCENTIVO PROMOCIONAL DO IFOOD']].groupby(
        'RESTAURANTE').sum()
    # print("Total de Descontos oferecidos pelo IFood: ",incentivo_iffod)

    # Total de incentivo do restaurante
    incentivo_restaurante = TabelaFitradaPorData[['RESTAURANTE', 'INCENTIVO PROMOCIONAL DA LOJA']].groupby(
        'RESTAURANTE').sum()

    # print("Total de descontos oferecidos pelo restaurante: ",incentivo_restaurante)

    # Calculando o tempo de execuçao da tarefa e convertendo pra string
    inicio = time.time()
    time_str = str(inicio)
    print('Tempo da tarefa: ', time_str)

    #Enviando email no final
    enviar_email()


# Enviar email com relatório
def enviar_email():
    corpo_email = f'''
        <p>'Faturamento por dia:</p>
        <p>{FaturamentoPorDia.to_html()}</p>

        <p>Faturamento por restaurante:</p> 
        <p>{faturamento.to_html(formatters={'TOTAL DO PARCEIRO': 'R${:,.2f}'.format})}</p>

        <p>Total de entregas e valor: </p>
        <p>{total_entregas.to_html(formatters={'TAXA DE ENTREGA': 'R${:,.2f}'.format})}</p>

        <p>Total de incentivo IFOOD: </p>
        <p>{incentivo_iffod.to_html(formatters={'INCENTIVO PROMOCIONAL DO IFOOD': 'R${:,.2f}'.format})}</p>

        <p>Total de incentivo do restaurante: </p>
        <p>{incentivo_restaurante.to_html(formatters={'INCENTIVO PROMOCIONAL DA LOJA': 'R${:,.2f}'.format})}</p>

        <p>Tempo para execução da tarefa: {time_str}</p>

         '''


msg = email.message.Message()
msg['Subject'] = f'RELATORIO DE FATURAMENTO DOS RESTAURANTES PERIODO: {dataInicial} Ate: {dataFinal}'
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


#função fehar janela
def fecharJanela(self):
    sys.exit()

#chamando tela
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
