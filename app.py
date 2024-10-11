import json
from chalice import Chalice
from chalicelib.services.email import enviar_email_de_teste 

app = Chalice(app_name='projeto-estudos-chalice-aws-jenkins')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/teste_enviar_email', methods=['POST'])
def teste_enviar_email():
    request = app.current_request
    corpo_json = json.loads(request.raw_body)  # Carrega o corpo como JSON
    assunto = corpo_json.get('assunto')
    corpo_email = corpo_email.get('corpo')
    destinatario = corpo_json.get('destinatario')
    enviar_email_de_teste(
        assunto=assunto,
        corpo=corpo_email,
        email_destinatario=destinatario
    )
    return 'teste'
