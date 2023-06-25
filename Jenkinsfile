pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/mateusfcarvalho/IMC_python.git' 
                sh 'apt-get update'
                sh 'apt-get install -y python3 python3-pip npm'
                sh 'npm install'
                sh 'pip3 install -r requirements.txt'
                sh 'docker build -t calculadora-imc .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run calculadora-imc'
            }
        }
    }
    
    post {
        always {
            sh 'apt-get clean'
        }
    }
}