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
                bat'"C:\\Users\\gunjs\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
            }
        }

    }
}