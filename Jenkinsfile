pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/akjoshi12/Group-E-Deployment-of-AI---Model-Deployment-and-CI-CD-With-Jenkins-and-Github.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python tests/test_model.py'
            }
        }
    }
    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed. Check logs.'
        }
    }
}