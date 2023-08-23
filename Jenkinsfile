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
                    sh 'python SampleApplication.py add 5 3'  // Example: Run add operation with 5 and 3
                    sh 'python SampleApplication.py multiply 4 2'  // Example: Run multiply operation with 4 and 2
                    sh 'python -m unittest SampleApplication.py'
//                     sh 'python hello.py'  // Run the Python script
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
