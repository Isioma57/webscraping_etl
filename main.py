import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from extractors import extract
from transformers import transform
from loader import load_to_postgres

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


engine = create_engine(f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}')

books_df = extract()
print(books_df.head()) 
transformed_df = transform(books_df)
load_to_postgres(transformed_df, 'books', engine)
