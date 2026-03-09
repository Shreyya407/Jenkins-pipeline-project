pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

    }
}