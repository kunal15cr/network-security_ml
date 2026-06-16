from datetime import datetime
import os

from networksecurity.constant import training_pipeline

class TrainingPipelineConfig:
    def __init__(self):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp
    


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR)
        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.FEATURE_STORE_DIR, training_pipeline.FEATURE_STORE_FILE_NAME)
        self.train_test_split_ratio: float = training_pipeline.TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipeline.COLLECTION_NAME
        self.database_name: str = training_pipeline.DATABASE_NAME