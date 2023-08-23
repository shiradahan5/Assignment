pipeline {
    agent any
//     agent {
//         docker { image 'python:3' }
//     }

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
//                     sh 'pip --version'
//                     sh '''
//                         cd files
//                         pip install -r requirements.txt
//                     '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Python script...'
                     sh '''
                        cd files
                        python SampleApplication.py add 5 3
                        python SampleApplication.py multiply 4 2
                        python -m unittest SampleApplication.py
                     '''
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
