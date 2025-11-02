import numpy as np
from abc import ABC, abstractmethod
import logging
from sklearn.metrics import mean_squared_error, r2_score


class Evaluation(ABC):
    """Abstract class defining strategy for evaluating models."""

    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """Calculates the score for the models."""
        pass


class MSE(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error calculating MSE: {}".format(e))
            raise e


class R2(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("Calculating R2")
            r2 = r2_score(y_true, y_pred)
            logging.info("R2: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error calculating R2: {}".format(e))
            raise e
