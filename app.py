from src.Predictive_credit_line_adjustment_system.logger import logging
from src.Predictive_credit_line_adjustment_system.exception import CustomException
import sys
from src.Predictive_credit_line_adjustment_system.components.data_ingestion import Dataingestion
from src.Predictive_credit_line_adjustment_system.components.data_ingestion import DataIngestionConfig



if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion= Dataingestion()
        data_ingestion.initiate_data_ingestion()


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)