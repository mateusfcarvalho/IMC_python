pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                git 'https://github.com/mateusfcarvalho/IMC_python.git'
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
