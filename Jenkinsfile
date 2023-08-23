pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'

                    sh '''
                        cd files
                        pip install -r requirements.txt
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
                     // Example: Run add operation with 5 and 3
//                     sh 'python SampleApplication.py multiply 4 2'  // Example: Run multiply operation with 4 and 2
//                     sh 'python -m unittest SampleApplication.py'
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
