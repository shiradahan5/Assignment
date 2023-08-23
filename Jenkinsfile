pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building the application...'
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
                        python -m unittest testSampleApplication.py
                     '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the application...'
                    sh '''
                        cd files
                        python SampleApplication.py --operation add --a 5 --b 3
                        python SampleApplication.py --operation multiply --a 4 --b 2
                     '''

                }
            }
        }
    }
}
