pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/abu366/booktracking2.git'
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
