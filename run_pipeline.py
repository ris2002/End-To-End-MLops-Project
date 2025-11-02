from pipelines.training_pipeline import training_pipeline
from zenml.client import Client
import os
if __name__ =="__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    workspace=os.getenv('WORKSPACE',os.getcwd())
    data_path=os.path.join(workspace,'datasets','olist_customers_dataset.csv')
    training_pipeline(data_path=data_path)
