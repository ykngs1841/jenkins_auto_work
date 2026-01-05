pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build step running'
                echo 'Hello Jenkins CI!'
            }
        }
    }
}
