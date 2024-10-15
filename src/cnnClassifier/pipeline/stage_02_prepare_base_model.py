from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage PrepareBaseModelTrainingPipeline Started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage PrepareBaseModelTrainingPipeline Completed <<<<<<")
    except Exception as e:
        logger.error(f"Error in PrepareBaseModelTrainingPipeline: {str(e)}")