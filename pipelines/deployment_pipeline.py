import numpy as np
import pandas as pd

from pydantic import BaseParameters

from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
import click
from steps.clean_data import clean_data
from steps.evaluate_model import evaluate_model
from steps.ingest_data import ingest_data
from steps.train_model import train_model

docker_settings = DockerSettings(required_integrations=[MLFLOW])


class DeploymentTriggerConfig(BaseParameters):
    min_accuracy: float = 0.92

@step
def deployment_trigger(accuracy: float, config: DeploymentTriggerConfig) -> bool:
       
    return accuracy >= config.min_accuracy


@pipeline(enable_cache=True, settings=docker_settings)
def continuous_deployment_pipeline(
   
    min_accuracy: float = 0.92,
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
   
    df = ingest_data( )
    X_train, X_test, y_train, y_test = clean_data(df)
    
    model = train_model(X_train, y_train)
    
    r2_score, mse = evaluate_model(model, X_test, y_test)

    deploy_decision = deployment_trigger(r2_score)

   
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deploy_decision,
        workers=workers,
        timeout=timeout,
    )

