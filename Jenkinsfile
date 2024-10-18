pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Use the built-in Jenkins Git plugin to clone the repo
                git branch: 'main', url: 'https://github.com/akjoshi12/Group-E-Deployment-of-AI---Model-Deployment-and-CI-CD-With-Jenkins-and-Github.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install required dependencies from requirements.txt
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run your test script
                sh 'python3 tests/test_model.py'
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
