from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *


if __name__ == "__main__":

    ### Step 1. Data Ingestion
    data_ingestion =  DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ### Step 2. Data Preprocessing
    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ### Step 3. Model Training and Evaluating
    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)   
    trainer.run()       
