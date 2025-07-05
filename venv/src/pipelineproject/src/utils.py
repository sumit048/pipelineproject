import os
import sys
import pickle
from sqlalchemy import create_engine
from dataclasses import dataclass
import pandas as pd
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging

@dataclass
class ConnectDBConfig():
    host = 'localhost'
    user = 'root'
    password = 'Sagnik123#'
    database = 'diamondproject'
    table_name = 'diamondprojectdata'
    dataset_path:str = os.path.join('dataset', 'gemstone.csv')


class ConnectDB():
    def __init__(self):
        self.connect_db_config = ConnectDBConfig()

    
    def retrieve_data(self):
        engine = create_engine(f'mysql+mysqlconnector://{self.connect_db_config.user}:{self.connect_db_config.password}@{self.connect_db_config.host}/{self.connect_db_config.database}')
        query = f'Select * from {self.connect_db_config.table_name}'
        df = pd.read_sql(query, engine)
        os.makedirs(os.path.dirname(self.connect_db_config.dataset_path), exist_ok=True)
        df.to_csv(self.connect_db_config.dataset_path, index=False)
        logging.info('Copy of dataset stored in dataset folder as a csv file')


def save_function(file_path, obj):
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "wb") as file_obj:
        pickle.dump(obj, file_obj)


def model_performance(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        
        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    


def load_obj(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        logging.info('Error in load_object function in utils')
        raise CustomException(e,sys)