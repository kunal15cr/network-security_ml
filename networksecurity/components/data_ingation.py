import os, sys
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
    
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e