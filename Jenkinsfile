pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/mateusfcarvalho/IMC_python.git'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python -m unittest discover -s IMC_python -p "test_*.py"'
            }
        }

        stage('Run') {
            steps {
                sh 'python IMC_python/calculadora_imc.py'
            }
        }
    }
}
