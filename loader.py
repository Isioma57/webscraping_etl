import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging


def load_to_postgres(books_df: pd.DataFrame, table_name: str, engine):
    """
    Load the transformed DataFrame into a PostgreSQL table.

    Args:
    books_df (pd.DataFrame): The DataFrame to be loaded into the database.
    
    table_name (str): The name of the table in PostgreSQL where the data will be loaded.
    
    engine: The SQLAlchemy engine object for database connection.
    """
    logging.info("Starting data loading into PostgreSQL...")
    
    try:
        # Load the DataFrame into Postgres Table
        books_df.to_sql(table_name, engine, index=False, if_exists='replace')
        logging.info("Data loading completed successfully.")
    except Exception as e:
        logging.error(f"Failed to load data into PostgreSQL: {e}")
        