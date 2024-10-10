pipeline{
    agent any
    options {
        timeout(time:30, unit: 'SECONDS')
    }

    stages{
        stage('PythonUnitTest'){
            withPythonEnv('python3'){
            sh 'pip install pytest'
            sh 'python3 -m pytest tests'
            }
        }
    }
}
