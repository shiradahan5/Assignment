pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
                    // You can add build commands here if needed
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Python script...'
                    sh 'python hello.py'  // Run the Python script
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the application...'
                    // You can add deployment commands here
                }
            }
        }
    }
}
