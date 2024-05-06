import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_data_api():
    msg = MIMEMultipart()
    msg['From'] = 'matheusbodin321@gmail.com'
    msg['To'] = 'eobodin@icloud.com'
    msg['Subject'] = 'Test andre'
    body = 'test 1'
    msg.attach(MIMEText(body, 'plain'))

    #output_file2 = "..\\dados\\olhao_data.csv"

    path = '..\\dados'
    all_files = os.listdir(path)
    #csv_files = [filename for filename in all_files if filename.endswith('.csv')]

    for file in all_files:
        if file.endswith('.csv'):
            file_path = os.path.join(path, file)
            with open(file_path, 'rb') as file:
                file_data = file.read()
                msg.attach(MIMEApplication(file_data, Name=file_path))


    smtp_server = 'smtp.gmail.com'  # Servidor SMTP do Gmail
    smtp_port = 587  # Porta para conexão TLS
    smtp_username = 'matheusbodin321@gmail.com'
    smtp_password = 'geol enbf tvia gwvl'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Inicie a conexão TLS
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
