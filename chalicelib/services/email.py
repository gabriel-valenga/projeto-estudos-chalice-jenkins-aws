import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def teste_obter_parametro_senha_email():
    # Criar um cliente para o SSM
    ssm_client = boto3.client('ssm')

    # Nome do parâmetro
    parameter_name = 'SENHA_GMAIL_GABRIELVALENGATESTESAWS1'

    # Recuperar o parâmetro do Parameter Store
    try:
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        gmail_password = response['Parameter']['Value']
        
        # Exemplo de uso da senha (não imprima em produção!)
        print(f"Senha do Gmail recuperada com sucesso. {gmail_password}")
        
        # Aqui você pode usar a senha para enviar e-mails ou outras operações
        # Exemplo: enviar_email(gmail_password)
        
    except Exception as e:
        print(f"Erro ao recuperar o parâmetro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Processo concluído!'
    }


def enviar_email(remetente, senha, destinatario, assunto, corpo):
    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        # Conecta ao servidor SMTP do Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Ativa a criptografia
            server.login(remetente, senha)  # Faz login na conta
            server.send_message(msg)  # Envia a mensagem
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")


def enviar_email_de_teste(remetente, email_destinatario, assunto, corpo):
    try:
        # Criar um cliente para o SSM
        ssm_client = boto3.client('ssm')
        senha_email = (
            ssm_client.get_parameter(
                Name='SENHA_GMAIL_GABRIELVALENGATESTESAWS1',
                WithDecryption=True
            )
        )
        senha_email = senha_email['Parameter']['Value']
        enviar_email(
            remetente='gabrielvalengatestesaws1@gmail.com',
            senha=senha_email,
            email_destinatario=email_destinatario,
            assunto=assunto,
            corpo=corpo         
        )
    except Exception as e:
        print('Ocorreu erro ao enviar email de teste')
