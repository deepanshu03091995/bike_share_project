from sharing.exception import SharingException
import sys
from sharing.logger import logging
from typing import List
from sharing.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from sharing.entity.config_entity import ModelTrainerConfig
from sharing.util.util import load_numpy_array_data,save_object,load_object

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            logging.info(f"{'>>' * 30}Model trainer log started.{'<<' * 30} ")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise SharingException(e, sys) from e
        
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            pass
        except Exception as e:
            raise SharingException(e, sys) from e
        
    
