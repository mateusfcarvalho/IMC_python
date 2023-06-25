pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                h 'python3 --version'
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
