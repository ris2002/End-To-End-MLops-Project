import logging
from zenml import step
import pandas as pd
from src.data_cleaning import DataPreproccess, DataDivideStrategy, DataCleaning
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_data(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "Y_train"],
    Annotated[pd.Series, "Y_test"]
]:
    """
    Cleans the data and splits into training and testing sets.

    Returns:
        X_train, X_test, Y_train, Y_test
    """
    try:
        logging.info("Starting data cleaning and division...")

        # Preprocessing
        process_strategy = DataPreproccess()
        data_cleaner = DataCleaning(df, process_strategy)
        processed_data = data_cleaner.handle_data()

        # Splitting
        divide_strategy = DataDivideStrategy()
        X_train, X_test, Y_train, Y_test = divide_strategy.handle_data(processed_data)

        logging.info("Data cleaning and division successful")

        # ✅ RETURN the values
        return X_train, X_test, Y_train, Y_test

    except Exception as e:
        logging.error(f"Error while cleaning data: {e}")
        raise e
