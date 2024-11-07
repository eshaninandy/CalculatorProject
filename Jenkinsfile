pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                // Run unit tests
                sh 'python -m unittest discover'
            }
        }
    }
}
