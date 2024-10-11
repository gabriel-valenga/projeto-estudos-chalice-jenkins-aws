import boto3
import os

def teste_obter_parametro_senha_email(event, context):
    # Criar um cliente para o SSM
    ssm_client = boto3.client('ssm')

    # Nome do parâmetro
    parameter_name = 'SENHA_GMAIL_GABRIELVALENGATESTESAWS1'

    # Recuperar o parâmetro do Parameter Store
    try:
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        gmail_password = response['Parameter']['Value']
        
        # Exemplo de uso da senha (não imprima em produção!)
        print("Senha do Gmail recuperada com sucesso.")
        
        # Aqui você pode usar a senha para enviar e-mails ou outras operações
        # Exemplo: enviar_email(gmail_password)
        
    except Exception as e:
        print(f"Erro ao recuperar o parâmetro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Processo concluído!'
    }
