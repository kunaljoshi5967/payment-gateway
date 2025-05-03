pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/kunaljoshi5967/payment-gateway.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t payment-gateway .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name payment-gateway payment-gateway'
            }
        }
    }
}
