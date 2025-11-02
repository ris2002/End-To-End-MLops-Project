from zenml import step
import pandas as pd
import logging
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig
import mlflow
from zenml.client import Client
experiment_tracker=Client().active_stack.experiment_tracker.name

@step(experiment_tracker=experiment_tracker)
def train_model(
    X_Train: pd.DataFrame,
    X_Test: pd.DataFrame,
    Y_Train: pd.DataFrame,
    Y_Test: pd.DataFrame,
    config: ModelNameConfig
) -> RegressorMixin:
    """ZenML step to train a regression model."""
    try:
        # Instantiate model based on config
        if config.model_type == "LinearRegression":
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
        else:
            raise ValueError(f"Unsupported model: {config.model_type}")

        # Train model
        trained_model = model.train(X_Train, Y_Train)
        logging.info(f"Model {config.model_type} trained successfully.")

        return trained_model

    except Exception as e:
        logging.error(f"Error in training model: {e}")
        raise e
