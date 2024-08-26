import pandas as pd
import logging


def transform(books_df: pd.DataFrame)-> pd.DataFrame:
    logging.info("Starting Data Transformation...")
    
    # Remove leading and trailing whitespace from column names
    books_df.columns = books_df.columns.str.strip()
    
    # Convert 'price' column to numeric values (removing currency symbols)
    books_df['price'] = books_df['price'].replace('[/£]', '', regex=True).astype(float)
    
    # Normalize 'availability' by removing extra whitespace
    books_df['availability'] = books_df['availability'].str.strip()
    
    # Map star ratings to numeric values
    ratings_mapping = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    books_df['rating'] = books_df['rating'].map(ratings_mapping)
    
    logging.info("Data transformation completed.")
    
    return books_df