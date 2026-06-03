pipeline {
    agent {label 'dev'}

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t srikanthreddy1234/sample-app:v1 .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push srikanthreddy1234/sample-app:v1
                '''
            }
        }

        stage('Deploy To Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                '''
            }
        }
    }
}