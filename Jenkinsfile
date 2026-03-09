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
                sh 'python3 app.py'
            }
        }

    }
}