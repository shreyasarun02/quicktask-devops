pipeline {
    agent any

    environment {
        IMAGE_NAME = "quicktask-app"
        CONTAINER_NAME = "quicktask-container"
        PORT = "5000"
        DOCKERHUB_USERNAME = "shreyas9980"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repository..."
                git branch: 'main', url: 'https://github.com/shreyasarun02/quicktask-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                echo "Logging into DockerHub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo "Tagging and pushing image to DockerHub..."
                sh 'docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG'
                sh 'docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Stopping existing container if running..."
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $




