from zenml import step
import pandas as pd
import mlflow
import logging
from src.evaluation import R2, MSE
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated
from zenml.client import Client 
experiment_tracker=Client().active_stack.experiment_tracker.name
@step(experiment_tracker=experiment_tracker )
def evaluate_model(
    model: RegressorMixin, 
    X_Test: pd.DataFrame, 
    Y_Test: pd.DataFrame
) -> Tuple[
    Annotated[float, "r2_score"], 
    Annotated[float, "mse"]
]:
    """ZenML step for evaluating a regression model using MSE and R2 metrics."""
    try:
        logging.info("Starting model evaluation...")

        # Generate predictions
        prediction = model.predict(X_Test)

        # Calculate MSE
        mse_class = MSE()
        mse = mse_class.calculate_scores(Y_Test, prediction)
        mlflow.log_metric("mse",mse)
        logging.info(f"Model Mean Squared Error (MSE): {mse}")

        # Calculate R2
        r2_class = R2()
        r2 = r2_class.calculate_scores(Y_Test, prediction)
        mlflow.log_metric("r2",r2)
        logging.info(f"Model R2 Score: {r2}")

        logging.info("Model evaluation completed successfully.")
        return r2, mse

    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        raise e
