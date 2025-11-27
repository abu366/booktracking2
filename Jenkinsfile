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
                bat 'docker build -t booktracker-web .'
            }
        }
        stage('Test') {
            steps {
                bat 'docker run --rm booktracker-web curl -f http://localhost:5000 || exit 1'
            }
        }
    }
}
