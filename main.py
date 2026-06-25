import sys
import os
from networksecurity.components.data_ingation import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.entity_config import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig



    
if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Starting data ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
        logging.info("Starting data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e