pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
               
            }
        }

        stage('Run') {
            steps {
                sh 'python3 IMC_python/calculadora_imc.py'
            }
        }
    }
}
