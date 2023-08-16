pipeline {
    agent any

    stages {
        stage('Checkout repo') {
            steps {
                git branch: 'master',
                credentialsId: 'github',
                url: 'https://github.com/RoyyGoren/WOG.git'
            }
        }

        stage('docker compose build') {
            steps {
                script {
                    bat "docker-compose build"
                }
            }
        }

        stage('docker compose') {
            steps {
                script {
                    bat "docker-compose up -d"
                }
            }
        }
        stage('selenium test') {
            steps {
                script {
                    bat "python e2e.py"
                }
            }
        }
    }
}
