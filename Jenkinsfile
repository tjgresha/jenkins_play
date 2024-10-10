pipeline{
    agent python
    options {
        timeout(time:30, unit: 'SECONDS')
    }

    stages{
        stage('InstallDeps'){
            steps{
                sh 'apt install python3.12-venv'
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
