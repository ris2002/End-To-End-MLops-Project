My Understanding of ZenML and MLOps (Improved
Summary)
Background
Before starting this project, I had no prior knowledge of MLOps.
I am currently taking the MLOps course by Duke University, and this is a practice project I
followed from YouTube to apply what I’m learning. This file contains the things I didn't know
prior.
What I Learned About ZenML
ZenML is an open-source MLOps framework that helps you build, organize, and deploy
machine learning pipelines — both locally and on the cloud.
It acts as a unifying layer that connects all parts of an ML project (data processing, model
training, experiment tracking, deployment, etc.) into one reproducible and production-ready
workflow.
You can think of ZenML like LangChain (which simplifies building LLM applications):
ZenML simplifies building ML pipelines and deploying end-to-end ML workflows.
Without ZenML, we often use multiple separate tools:
● GitHub Actions → CI/CD
● Docker → Containerization
● MLflow → Experiment tracking
● AWS / GCP / Azure → Deployment
ZenML combines all these pieces into a single managed pipeline called a stack, so you don’t
have to manually connect everything.
Project Structure and Blueprint
Before coding, I learned the importance of first creating a blueprint for the project — similar to
designing a building before construction.
This means:
● Defining folder structures
● Planning the functions and pipeline steps
● Running a dummy version of the code once to verify the flow works
Data Cleaning Module (data_cleaning.py)
In this file, I created four classes following an object-oriented and abstract design pattern.
1. DataStrategy (Abstract Class)
● Defines a common interface for data-handling strategies.
● Has an abstract method handle_data() that all subclasses must implement.
2. DataPreprocess (Subclass)
● Implements handle_data() to clean and preprocess data.
● Tasks include dropping unnecessary columns, filling missing values, and keeping only
numeric features.
3. DataDivideStrategy (Subclass)
● Implements handle_data() to split data into train and test sets.
4. DataCleaning (Controller Class)
● Takes a dataset and a chosen strategy (either DataPreprocess or
DataDivideStrategy).
● Delegates the processing task to the strategy passed into it.
● Ensures flexible and reusable data processing.
This structure uses the Strategy Design Pattern — allowing easy swapping of different
data-processing strategies.
Configuration File (config.py)
The config.py file is used to define configuration parameters for the pipeline using ZenML’s
BaseParameters class.
Example:
from zenml.steps import BaseParameters
class ModelNameConfig(BaseParameters):
model_name: str = "Linear Regression"
This allows you to easily pass custom settings (like model name, learning rate, etc.) to ZenML
steps.
Model Training (train_model.py)
I created a training script using Linear Regression and followed the same abstract class
pattern — keeping the project modular and scalable.
What I Learned About MLFlow
MLFlow is an experiment tracker.The advantage of using MLFlow over over standard printing of
accuracies is it saves the results of previous experiments so it would be easier to compare the
differences and the terminal would look cleaner. It also saves and versions trained models, so
you can load and reuse them later. It saves also theParameters → e.g., learning rate, number of
epochsMetrics → e.g., accuracy, lossArtifacts → e.g., the trained model file, plots, or data
Run info → start/end time, user, environment details but not hte whole code of the model
What I Learned About ZenML + MLflow Integration
ZenML integrates seamlessly with MLflow for experiment tracking.
Here are the key steps and commands I used to set it up:
Step 1: Install MLflow integration
zenml integration install mlflow -y
Step 2: Register an MLflow experiment tracker
zenml experiment-tracker register mlflow_tracker \
--flavor=mlflow \
--tracking_uri="file:./mlruns"
Step 3: Create and activate a ZenML stack
Since the default stack cannot be modified, I created a new one:
zenml stack register local_stack \
-o default \
-a default \
-e mlflow_tracker
zenml stack set local_stack
Step 4: Verify
zenml stack describe local_stack
Result:
A new stack (local_stack) was created that uses:
● Default orchestrator
● Default artifact store
● MLflow experiment tracker
Now, whenever I run a ZenML pipeline (e.g., python run_pipeline.py), all runs, metrics,
and artifacts are automatically tracked in MLflow.
What I learnt for deployment
For deployment part zeml uses the the function MLflowModelDeployer to deploy the model
either in cloud or locally. So it deploys the models which are logged using ML Flow if the
accuracy is greater or equal to min_accuracy defined. What it does it uses docker to
containerize the model and deploys either to cloud or locally.
Summary
Concept Description
ZenML Framework for building, managing, and deploying ML pipelines
MLflow Integrated experiment tracker within ZenML stack
Pipeline
Blueprint
Predefined structure and dummy runs to ensure correctness before real
data
Abstract Classes Ensure modular, reusable data processing logic
Stacks Combine orchestrator, artifact store, and tracker into one environment
