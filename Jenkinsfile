pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git 'https://github.com/kunaljoshi5967/payment-gateway.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("payment-gateway-image")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run('-p 8000:8000')
                }
            }
        }
    }
}
