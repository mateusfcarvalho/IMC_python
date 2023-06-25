pipeline {
    agent {
        docker {
            image 'python:3.8'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/mateusfcarvalho/IMC_python.git'
                sh 'pip install -r requirements.txt'
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
            sh 'docker system prune -af'
        }
    }
}
