# Bibliotecas
from datetime import datetime

import pandas as pd
import smtplib
import email.message
import time
from tkinter import *
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from ui_main import ui_MainWindow
import sys
import re
import requests
import urllib


'''
#Tk()


# Lendo apenas o periodo previamente definido
# (input(f"Digite a data inicial, mes, dia, ano: "))
# dataInicial = str()
# dataFinal = str(input(f"Digite a data final, mes, dia, ano: "))
# dataFinal = str()


dataInicial = str(data_Inicial.get())
dataFinal = str(data_Final.get())
'''

# Janela
janela = Tk()

# Função principal
def datasRel():
    # Continuação da Janela

    janela.geometry("500x200")


janela.title("Relatório Restaurantes Big John")

texto_orientacao = Label(janela, text="Digite as datas inicial e final para gerar o relatório")

texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

texto_orientacao2 = Label(janela, text="Digite a data inicial: ")
texto_orientacao2.grid(column=0, row=1, padx=10, pady=10)

# dataInicial = Entry(janela)
# dataInicial.grid(column=0, row=2, padx=10, pady=10)
campo_data_inicial = Entry(janela)
campo_data_inicial.grid(column=0, row=2, padx=10, pady=10)

texto_orientacao3 = Label(janela, text="Digite a data final: ")
texto_orientacao3.grid(column=2, row=1, padx=10, pady=10)

# dataFinal = Entry(janela)
# dataFinal.grid(column=2, row=2, padx=10, pady=10)
campo_data_final = Entry(janela)
campo_data_final.grid(column=2, row=2, padx=10, pady=10)

botao = Button(janela, text="Gerar Relatorio", command=datasRel)
botao.grid(column=0, row=8, padx=10, pady=10)

# Adicionando o valor das datas
data_Inicial = str(campo_data_inicial.get())
data_Final = str(campo_data_final.get())

janela.mainloop()

# Função principal
# def datasRel():

# importar base de dados
tabela_pedidos = pd.read_excel('lista-de-pedidos.xlsx')

# Visualizar a base de dados
# pd.set_option('display.max_columns', None)
# print(tabela_pedidos)

# Filtro para selecionar a data
TabelaFitradaPorData = tabela_pedidos[
    (tabela_pedidos['DATA'] >= f'{dataInicial}') & (tabela_pedidos['DATA'] <= f'{dataFinal}')]
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


# janela.mainloop()


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

# janela.mainloop()
'''
# Janela
janela = Tk()
janela.geometry("500x200")
janela.title("Relatório Restaurantes Big John")
'''
'''
#Iniciando a contagem de tempo para realização da tarefa
    #inicio = time.time()

    #dataInicial = campo_data_inicial.get()
    #dataFinal = campo_data_final.get()
    #dataInicial = str(campo_data_inicial.get())
    #dataFinal = str(campo_data_final.get())

# Continuação da Janela
texto_orientacao = Label(janela, text="Digite as datas inicial e final para gerar o relatório")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

texto_orientacao2 = Label(janela, text="Digite a data inicial: ")
texto_orientacao2.grid(column=0, row=1, padx=10, pady=10)

dataInicial = Entry(janela)
dataInicial.grid(column=0, row=2, padx=10, pady=10)
# campo_data_inicial = Entry(janela)
# campo_data_inicial.grid(column=0, row=2, padx=10, pady=10)

texto_orientacao3 = Label(janela, text="Digite a data final: ")
texto_orientacao3.grid(column=2, row=1, padx=10, pady=10)

dataFinal = Entry(janela)
dataFinal.grid(column=2, row=2, padx=10, pady=10)
# campo_data_final = Entry(janela)
# campo_data_final.grid(column=2, row=2, padx=10, pady=10)

botao = Button(janela, text="Gerar Relatorio", command=datasRel)
botao.grid(column=0, row=8, padx=10, pady=10)

    #texto_dataRelatorio = Label(janela, text='')
    #texto_dataRelatorio.grid(column=0, row=6, padx=10, pady=10)
'''
# janela.mainloop()

# print("Email enviado")
# texto_dataRelatorio["text"] = {dataInicial},{dataFinal}


# inicio = time.time()
# print('Tempo para chegar ao resultado: ', time.time() - inicio)
