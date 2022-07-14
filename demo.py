from distutils.command.config import config
from sharing.config.configuration import *
from sharing.component.data_ingestion import DataIngestion
from sharing.component.data_validation import DataValidation
from sharing.entity.config_entity import DataValidationConfig
from sharing.entity.artifact_entity import DataIngestionArtifact
from sharing.pipeline.pipeline import Pipeline
import logging

def main():
    try:
        #pipe = Pipeline()
        #pipe.run_pipeline()
        config = Configuartion().get_data_transformation_config()
        print(config)
        #ingested = DataIngestion(data_ingestion_config=DataIngestionConfig)
        #ingested.download_sharing_data()
    
        
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()