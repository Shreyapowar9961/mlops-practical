
@'
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '"C:/Users/DS_USER/AppData/Local/Programs/Python/Python311/python.exe" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-hello:1.0 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm mlops-hello:1.0'
            }
        }
    }
}
'@ | Set-Content -Encoding ascii Jenkinsfile
