import logging
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from typing import Union
from sklearn.model_selection import train_test_split

class DataStrategy(ABC):
    """Abstract class for data strategies"""
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass

class DataPreproccess(DataStrategy):
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        try:
            # Drop unneeded columns
            data = data.drop(
                [
                    "order_approved_at",
                    "order_delivered_customer_date",
                    "order_estimated_delivery_date",
                    "order_purchase_timestamp",
                    "order_delivered_carrier_date",
                ], axis=1
            )
            # Fill missing values
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            data["review_comment_message"].fillna("No review", inplace=True)

            # Keep only numeric columns and drop some
            data = data.select_dtypes(include=[np.number])
            col_to_drop = ["customer_zip_code_prefix", "order_item_id"]
            data = data.drop(col_to_drop, axis=1)
            return data
        except Exception as e:
            logging.error(f"Error while cleaning the data: {e}")
            raise e

class DataDivideStrategy(DataStrategy):
    """Class for dividing data into train and test sets"""
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        try:
            X = data.drop(["review_score"], axis=1)
            Y = data["review_score"]
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
            return X_train, X_test, Y_train, Y_test
        except Exception as e:
            logging.error(f"Error while dividing data: {e}")
            raise e

class DataCleaning:
    """Class for cleaning data which processes the data and optionally divides it."""
    def __init__(self, data: pd.DataFrame, data_strategy: DataStrategy):
        self.data = data
        self.data_strategy = data_strategy  # fixed typo

    def handle_data(self):
        try:
            return self.data_strategy.handle_data(self.data)
        except Exception as e:
            logging.error(f"Error while cleaning the data: {e}")
            raise e
