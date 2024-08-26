import requests
import pandas as pd
from bs4 import BeautifulSoup
import logging


def extract() -> pd.DataFrame:
    logging.info("Starting Data Extraction...")
    
    # Initialize an empty list to store book details across all pages
    books = []

    # URL of the website to scrape
    for i in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        
        # Send a get request to the website
        response = requests.get(url)

        # Check if the response was succesful
        if response.status_code != 200:
            raise Exception(f"Failed to load page {url}")
        
        soup = BeautifulSoup(response.content, 'html.parser')   # Parse the html content using beautiful soup
        ol = soup.find('ol')    # Find the ordered list containing all the books
        
        # Extract book details from each article tag within the ol
        for book in ol.find_all('article', class_='product_pod'):
            title = book.find('img')['alt']
            price = book.find('p', class_='price_color').text.strip()
            availability = book.find('p', class_ = 'instock availability').text.strip()
            star = book.find('p', class_ = 'star-rating')['class']
            rating = star[1]
                
            # Append the extracted details to the list
            books.append({
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            })   
    books_df = pd.DataFrame(books)
    books_df.to_csv('books.csv', index=False)

    logging.info("Data Extraction completed.")
    
    return books_df
