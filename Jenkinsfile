pipeline{
    agent any
    stages{



stage('Checkout') {
            steps {
                git branch:'master',url:'git@github.com:ris2002/End-To-End-MLops-Project.git'
            }
        }




        stage('Setup'){
           steps{
               sh 'python3 -m venv venv'
               sh '. venv/bin/activate && pip install -r requirements.txt'
           }
        }
        stage('Run Pipelinne'){
            steps{
                sh 'python run_pipeline.py'
            }
        }
    }
}