from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e