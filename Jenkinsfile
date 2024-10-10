pipeline{
    agent any
    options {
        timeout(time:30, unit: 'SECONDS')
    }

    stages{
        stage('SAST'){
        }
        stage('SonarQube'){
        }
           stage('InstallDeps'){
            steps{
                sh 'sudo apt install python3.12-venv'
            }
        }
        stage('PythonUnitTest'){
            steps{
                withPythonEnv('python3'){
                sh 'pip install pytest'
                sh 'python3 -m pytest tests'
                }
            }
        }
    }
}
