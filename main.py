from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Prepare base model"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
        logger.error(f"Error in PrepareBaseModelTrainingPipeline: {str(e)}")