def enviar_email():
    corpo_email = f'''
    <p>Faturamento por restaurante:</p> 
    <p>{faturamento.to_html(formatters={'TOTAL DO PARCEIRO': 'R${:,.2f}'.format})}</p>

    <p>Total de entregas e valor: </p>
    <p>{total_entregas.to_html(formatters={'TAXA DE ENTREGA': 'R${:,.2f}'.format})}</p>

    <p>Total de incentivo IFOOD: </p>
    <p>{incentivo_iffod.to_html(formatters={'INCENTIVO PROMOCIONAL DO IFOOD': 'R${:,.2f}'.format})}</p>

    <p>Total de incentivo do restaurante: </p>
    <p>{incentivo_restaurante.to_html(formatters={'INCENTIVO PROMOCIONAL DA LOJA': 'R${:,.2f}'.format})}</p>
    '''
    msg = email.message.Message()
    msg['Subject'] = 'RELATORIO DE FATURAMENTO DOS RESTAURANTES'
    msg['From'] = 'emonitor@transportadoraroma.com.br'
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