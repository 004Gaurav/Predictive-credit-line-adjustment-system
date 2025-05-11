import sys
import os
from src.Predictive_credit_line_adjustment_system.exception import CustomException
from src.Predictive_credit_line_adjustment_system.logger import logger
import pandas as pd
import logging
from dotenv import load_dotenv
import pymysql


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established,mydb")
        df=pd.read_sql_query('Select * from linepredict',mydb)
        print(df.head())

        return df
        
    except Exception as ex:
        raise CustomException(ex,sys)