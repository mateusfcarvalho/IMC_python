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
                sh 'python3 IMC.py'
                sh '50'
                sh '1.60'
            }
        }

    }
}
