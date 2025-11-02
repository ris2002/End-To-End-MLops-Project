import logging
from abc import ABC,abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC):
    @abstractmethod
    def train(self,X_Train,Y_Train):
        '''
        Trains the model
        '''
class LinearRegressionModel(Model):
    def train(self,X_Train,Y_Train,**kwargs):
        '''
        Trains The model
        Args:
        X_Train:Training the data
        Y_Train:Training mopdles
        '''
        try:
             reg=LinearRegression(**kwargs)
             reg.fit(X_Train,Y_Train)
             logging.info("Model Training Completed")
             return reg
        except Exception as e:
            logging.error("Error in training models:{}".format(e))
            raise e

    


