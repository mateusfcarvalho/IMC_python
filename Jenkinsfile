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
                sh 'python3 IMC.py'
                sh '58'
                sh '1.78'
            }
        }
    }
}
