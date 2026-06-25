from networksecurity.entity.artifac_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.entity.entity_config import DataValidationConfig
from networksecurity.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import os, sys

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self._schema_columns = [
                list(column_def.keys())[0].strip()
                for column_def in self._schema_config.get("columns", [])
                if isinstance(column_def, dict) and column_def
            ]
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e   
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def data_set_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, threshold=0.05) -> bool:
        try:
           status = True
           report = {}
           for column in base_df.columns:
               d1 = base_df[column]
               d2 = current_df[column]
               is_same_dist = ks_2samp(d1, d2)
               if threshold <= is_same_dist.pvalue:
                   is_found = False
               else:
                    is_found = True
                    status = False
                    report.update({column: {"p_value": float(is_same_dist.pvalue), 
                                        "drift_status": is_found}})  
                
               drift_report_file_path = self.data_validation_config.drift_report_file_path 

               os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
               write_yaml_file(drift_report_file_path, report)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            expected_columns = self._schema_columns
            logging.info(f"Expected columns: {expected_columns}")
            logging.info(f"Dataframe columns: {list(dataframe.columns)}")

            if len(dataframe.columns) != len(expected_columns):
                logging.warning(
                    f"Column count mismatch: expected {len(expected_columns)}, got {len(dataframe.columns)}"
                )
                return False

            missing_columns = [column for column in expected_columns if column not in dataframe.columns]
            if missing_columns:
                logging.warning(f"Missing required columns: {missing_columns}")
                return False

            return True
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
           
           #read _data
            train_df = DataValidation.read_data(train_file_path)
            test_df = DataValidation.read_data(test_file_path)


            # validate data
            status = self.validate_number_of_columns(dataframe=train_df)
            if not status:
                raise NetworkSecurityException(f"Train data does not have required number of columns", sys)
            
            status = self.validate_number_of_columns(dataframe=test_df)
            if not status:
                raise NetworkSecurityException(f"Test data does not have required number of columns", sys)
            
            # check data drift
            self.data_set_drift(base_df=train_df, current_df=test_df, threshold=self.data_validation_config.drift_threshold)
            directory_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(directory_path, exist_ok=True)

            train_df.to_csv(path_or_buf=self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_df.to_csv(path_or_buf=self.data_validation_config.valid_test_file_path, index=False, header=True)
            
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
            )
            logging.info(f"Data Validation Artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        

