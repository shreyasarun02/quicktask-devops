pipeline {
    agent any

    environment {
        IMAGE_NAME = "quicktask-app"
        CONTAINER_NAME = "quicktask-container"
        PORT = "5000"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/shreyasarun02/quicktask-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Stopping existing container if running..."
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'

                echo "Running new container..."
                sh 'docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Please check the logs above."
        }
    }
}





