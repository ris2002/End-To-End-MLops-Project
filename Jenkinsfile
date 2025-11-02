pipeline{
    agent any
    stages{



 stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/your-repo-name.git'
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