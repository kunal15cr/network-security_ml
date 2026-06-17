import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List

from sklearn.model_selection import train_test_split
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# configaration for data ingestion
from networksecurity.entity.entity_config import DataIngestionConfig




class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def export_data_as_dataframe(self) -> pd.DataFrame:
        try:
            CSV_URL = (
                    f"https://docs.google.com/spreadsheets/d/"
                    f"{self.data_ingestion_config.sheet_id}/export?format=csv"
                )
            return pd.read_csv(CSV_URL)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_data_as_dataframe()
            dataframe = self.export_data_to_feature_store(dataframe)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def export_data_to_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e