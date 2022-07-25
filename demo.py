from distutils.command.config import config
from sharing.config.configuration import *
from sharing.component.data_ingestion import DataIngestion
from sharing.component.data_validation import DataValidation
from sharing.entity.config_entity import DataValidationConfig
from sharing.entity.artifact_entity import DataIngestionArtifact
from sharing.pipeline.pipeline import Pipeline
from sharing.component.data_transformation import DataTransformation
import logging


def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        #config = Configuartion().get_model_evaluation_config()
        #print(config)
        #ingested = DataIngestion(data_ingestion_config=DataIngestionConfig)
        #ingested.download_sharing_data()
        #schema_file = r"D:\GIT\bike_share_project\config\schema.yaml"
        #file_pth = r"D:\GIT\bike_share_project\sharing\artifact\data_ingestion\2022-07-24-06-55-53\ingested_data\train\hours.csv"
        #validate = DataValidation(data_ingestion_artifact=DataIngestionConfig,data_validation_config=DataValidationConfig)
        #validate.validate_dataset_schema(schema_file_path = schema_file, file_path =file_pth)        
        #DataTransformation.load_data(file_path=file_pth,schema_file_path=schema_file)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()