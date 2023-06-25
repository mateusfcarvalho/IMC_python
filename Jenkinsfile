pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh 'apt-get update'
                sh 'apt-get install -y python3'
                sh 'python3 --version'
            }
        }

        stage('Build') {
            steps {
                git 'https://github.com/mateusfcarvalho/IMC_python.git'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
                archiveArtifacts "teste.py"
            }
        }

        stage('Run') {
            steps {
                sh 'python3 IMC_python/calculadora_imc.py'
            }
        }
    }
}
