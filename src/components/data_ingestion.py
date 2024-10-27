import os
import sys
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging



@dataclass
class DataIngestionConfig:
    """
    define path to save train, test and raw data
    """
    raw_data_path:str = os.path.join('artefact','raw_data.csv')
    train_data_path:str = os.path.join('artefact','train_data.csv')
    test_data_path:str = os.path.join('artefact','test_data.csv')
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        a = print(os.getcwd())
        logging.info('data ingestion started')
        logging.info(a)
        try:
            file_path = os.path.join('model development', 'train.csv')
            df = pd.read_csv(file_path)
            logging.info('dataset is loaded')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('spliting data initiated')
            train_data, test_data = train_test_split(df, test_size=.2,random_state=1)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=False)
            logging.info('data ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            

        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()