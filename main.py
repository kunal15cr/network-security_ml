import sys
import os
from networksecurity.components.data_ingation import DataIngestion
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.entity_config import TrainingPipelineConfig, DataIngestionConfig


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Starting data ingestion")
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e