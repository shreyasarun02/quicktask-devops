pipeline {
    agent any

    environment {
        IMAGE_NAME = "quicktask-app"
        CONTAINER_NAME = "quicktask-container"
        PORT = "5000"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker tag $IMAGE_NAME $DOCKER_USERNAME/quicktask:latest
                        docker push $DOCKER_USERNAME/quicktask:latest
                    '''
                }
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/shreyasarun02/quicktask-devops.git'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Stopping existing container if running..."
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                
                echo "Running container..."
                sh 'docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs above."
        }
    }
}

