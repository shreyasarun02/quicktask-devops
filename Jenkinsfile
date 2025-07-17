pipeline {
    agent any

    environment {
        IMAGE_NAME = "quicktask-app"
        CONTAINER_NAME = "quicktask-container"
        PORT = "5000"
        DOCKER_TAG = "shreyas9980/quicktask:latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/shreyasarun02/quicktask-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🔨 Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKE


