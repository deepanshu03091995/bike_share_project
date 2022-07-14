from http.client import ImproperConnectionState
import os, sys
from sharing.logger import logging
from sharing.exception import SharingException
from sharing.config.configuration import Configuartion
from sharing.entity.config_entity import *
from sharing.entity.artifact_entity import *
from sharing.component.data_ingestion import DataIngestion
from sharing.component.data_validation import DataValidation
from sharing.component.data_transformation import DataTransformation
from sharing.component.model_trainer import ModelTrainer

class Pipeline:
    
    def __init__(self, config : Configuartion = Configuartion()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise SharingException(e,sys) from e 
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise SharingException(e,sys) from e
    
    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact):
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),data_ingestion_artifact=data_ingestion_artifact)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise SharingException(e,sys) from e 

    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact, 
                                  data_validation_artifact : DataValidationArtifact)-> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(data_transformation_config=self.config.get_data_transformation_config(),
                                                     data_ingestion_artifact=data_ingestion_artifact,
                                                     data_validation_artifact=data_validation_artifact)
            
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise SharingException(e,sys) from e
        

    def start_model_trainer(self, data_transformation_artifact : DataTransformationArtifact)-> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer( data_transformation_artifact= data_transformation_artifact,
                                         model_trainer_config = self.config.get_model_trainer_config())
            model_trainer.initiate_model_trainer()
            
        except Exception as e:
            raise SharingException(e,sys) from e

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                                                          data_validation_artifact=data_validation_artifact)
            
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)

        except Exception as e:
            raise SharingException(e,sys) from e