pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run') {
            steps {
                sh 'python3 IMC.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
               sh 'python3 teste.py'
            }
        }

       
    }
}
