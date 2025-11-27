pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                // Clone your GitHub repository
                git 'https://github.com/abu366/booktracking2.git'
            }
        }
        stage('Build') {
            steps {
                // Build the Docker image for your Flask app
                bat 'docker build -t booktracker-web .'
            }
        }
        stage('Test') {
            steps {
                // Run a simple Python version check inside the container to verify image works
                bat 'docker run --rm booktracker-web python --version'
                
                // Optionally, run additional non-interactive tests here
            }
        }
    }
}
