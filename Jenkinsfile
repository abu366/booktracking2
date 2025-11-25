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
        bat 'docker build -t booktracker .'
    }
}
stage('Test') {
    steps {
        bat 'python main.py'
    }
}

    }
}
