pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/YOUR_USERNAME/book-tracker.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t booktracker .'
            }
        }
        stage('Test') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
