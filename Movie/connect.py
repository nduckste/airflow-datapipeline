#import pandas as pd
from sqlalchemy import create_engine


def create_engine_mysql():
    #https://docs.sqlalchemy.org/en/13/core/engines.html
    #dialect + driver: // username: password @ host:port / database

    engine = create_engine('mysql://sa:password@ea-airflow-opsathon.c6yf9ed3gd4c.us-west-2.rds.amazonaws.com/airnick', echo=False)
    return engine

def create_engine_pgsql():
    #engine = create_engine(DB_CONN)
    #dialect + driver: // username: password @ host:port / database
    engine = create_engine('postgresql+psycopg2://postgres:pg@localhost/airflow', echo=False)
    return engine


def insert_to_db(engine, df, table_name):
    df.to_sql(table_name, con=engine, if_exists="append")



