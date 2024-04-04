import sys
from Xray.components.Dataingestion import DataIngestion
from Xray.components.Data_transformation import DataTransformation
from Xray.components.model_traning import ModelTrainer
from Xray.components.model_evaluation import ModelEvaluation
from Xray.components.model_push import ModelPusher
from Xray.exception import XRayException
from Xray.logger import logging
from Xray.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
    )

from Xray.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_Config=DataIngestionConfig()
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_Data_ingestion method of Training Pipelines Class")
        try:
            logging.info("GEtting the data from s3 bucket")
            data_ingestion=DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the train set and test set from s3")
            
            logging.info("Exited the start_data_ingestion method from training pipline class")
            return data_ingestion_artifact
        except Exception as e:
            raise XRayException(e,sys)
if __name__=='__main__':
    train_pipeline=TrainPipeline()
    train_pipeline.start_data_ingestion