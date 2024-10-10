pipeline {
    agent any
    options {
        timeout(time: 50, unit: 'MINUTES') // ajuste conforme necessário
    }
    environment {
        AWS_DEFAULT_REGION = 'us-east-2' // Substitua pela sua região AWS
    }
    stages {
        stage('Env Check') {
            steps {
                sh 'env' // Imprime todas as variáveis de ambiente
                sh 'which python3' // Verifica o caminho do Python 3 no ambiente Jenkins
            }
        }
        stage('Debug AWS Parameter Store') {
            steps {
                script {
                    // Usando AWS CLI para testar a recuperação do parâmetro
                    sh """
                    aws ssm get-parameter --name ${SENHA_GMAIL_GABRIELVALENGATESTESAWS1} --with-decryption --query "Parameter.Value" --output text
                    """
                }
            }
        }
       
        stage('Setup') {
            steps {
                sh '/usr/bin/python3 --version' // Usando o caminho absoluto para Python
            }
        }
        stage('Clone Repository') {
            steps {
                // Clona o repositório do projeto Chalice
                git 'https://github.com/gabriel-valenga/projeto-estudos-chalice-jenkins-aws.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instala as dependências no ambiente virtual do Python
                sh '/usr/bin/python3 -m venv venv'
                sh './venv/bin/pip install -r ./requirements.txt'
            }
        }
        
        stage('Deploy to AWS') {
            steps {
                // Executa o deploy do Chalice na AWS
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credenciais']]) {
                    sh 'pwd'  // Verifique o diretório atual
                    sh 'ls -la'  // Verifique se o diretório .chalice/ está presente
                    dir('/var/jenkins_home/workspace/pipeline-projeto-estudos-chalice-jenkins-aws') {
                        sh 'pwd'  // Verifique o diretório atual
                        sh 'ls -la'  // Verifique se o diretório .chalice/ está presente
                        // Executa o comando de deploy do Chalice
                        sh './venv/bin/chalice deploy'
                    }

                }
            }
        }
    }
}
