pipeline{
    agent any
    options {
        timeout(time:30, unit: 'SECONDS')
    }

    stages{
        stage('SAST'){
            steps{
                sh 'echo SAST'
            }
        }
        stage('SonarQube'){
            steps{
                sh 'echo Sonar'
            }
        }
        stage('PythonUnitTest'){
            steps{
                withPythonEnv('python3'){
                sh 'python3 -m pytest tests --junitxml=./xmlReport/output.xml'
                }
            }
        }
    }
    post{
        always {
            junit 'xmlReport/output.xml'    
        }
    }
}

