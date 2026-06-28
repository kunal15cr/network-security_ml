import os
import sys

from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging

from networksecurity.entity.artifac_entity import DataTransformationArtifact,ModelTrainerArtifact
from networksecurity.entity.entity_config import ModelTrainerConfig

from networksecurity.utils.main_utils.utils import save_object, load_object, save_numpy_array_data, load_numpy_array_data

from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score

class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path
            
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train,y_train,x_test,y_test = train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def train_model(self,x,y):
        try:
            pass
           
        except Exception as e:
            raise NetworkSecurityException(e, sys)