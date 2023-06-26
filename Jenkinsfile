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
                sh 'python3 IMC.py 70 1.75'

            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python3 test.py'

            }
        }

    }
}
