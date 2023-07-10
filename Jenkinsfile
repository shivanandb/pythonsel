pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Hello World'
                echo 'Testing the application....'
                git branch: 'main', url: 'https://github.com/shivanandb/pythonsel.git'
                bat 'python --version'
            }
        }
        stage('Run') {
                steps{
                    echo "Current workspace is $WORKSPACE"
        }
    }
}
}
