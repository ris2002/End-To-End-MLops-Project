import pandas as pd
from zenml import step
import logging
class IngestData:
    '''Class for inngesting data'''
    def __init__(self,datapath:str):
        self.datapath=datapath
    def getData(self):
        '''Converting data from the given path to a pandas DataFrame'''
        print("Ingestinng data from {self.datapath}")  
        return pd.read_csv(self.datapath)
@step #n ZenML, @step is a decorator that tells ZenML:This function (or class) is a step in my ML pipeline

def ingest_data(data_path:str)->pd.DataFrame:
    ''''
    Ingesting data from the given path.
    Args-datapath
    O/p-pandas dataframe 
    '''
    try:
        ingest_data=IngestData(data_path)
        df=ingest_data.getData()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: e")
        raise e

'''Here, the decorator @step:
Wraps the function ingest_data
Registers it with ZenML as a pipeline step
Allows ZenML to track its inputs, outputs, logs, and artifacts
'''
'''When you run your pipeline:
ZenML calls the function (step).
It stores outputs (like DataFrames) as artifacts in your artifact store (local, S3, GCP, etc.).
It logs metadata so the run is reproducible.
You can later inspect each step’s inputs/outputs in the ZenML Dashboard'''