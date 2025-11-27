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
        stage('Run') {
            steps {
                // Stop existing container if running (ignore errors)
                bat '''
                docker rm -f booktracker-container || exit 0
                '''

                // Run container in detached mode
                bat 'docker run -d --name booktracker-container -p 5000:5000 booktracker-web'
            }
        }
    }
    post {
        always {
            echo "You can access the app at http://localhost:5000/"
            // Optionally keep container running; if you want to stop container on job finish, uncomment below
            // bat 'docker stop booktracker-container'
            // bat 'docker rm booktracker-container'
        }
    }
}
