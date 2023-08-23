pipeline {
    agent any
//     agent {
//         node {
//             label 'docker-agent-python'
//             }
//       }

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
//                     sh 'pip --version'
//                         pip install -r requirements.txt
                    sh '''
                        cd files
                        python3 -m pip install -r requirements.txt
                    '''
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
