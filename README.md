# Book Store Web Scraping and Data Pipeline Project

### Overview

This project is a web scraping and data pipeline solution designed to extract book information from the website [Books to Scrape](https://books.toscrape.com/catalogue/page-1.html). The data is then transformed and loaded into a PostgreSQL database for storage and further analysis. This project demonstrates the use of Python for web scraping, data transformation, and ETL (Extract, Transform, Load) processes using Docker and PostgreSQL.

# Project Structure

The project consists of the following components:

- Docker Compose: To set up a PostgreSQL database environment.

- Python Scripts:

    - main.py: The main entry point that orchestrates the extraction, transformation, and loading of data.
        
    - extractors.py: Contains functions to scrape book data from the website.

    - transformers.py: Contains functions to clean and transform the extracted data.

    - loader.py: Contains functions to load the transformed data into a PostgreSQL database.
    
- .env.example: Environment variables for PostgreSQL configuration.
    
- requirements.txt: List of Python dependencies needed to run the project.

# Prerequisites

- Docker and Docker Compose installed on your machine.

- Python 3.x installed.

# Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Isioma57/webscraping_etl.git
cd webscraping_etl
```

### 2. Set Up Environment Variables

Rename the .env.example file to .env file in the root directory of the project with the following content:

```plaintext
# Postgres Setup
POSTGRES_USER=username_here
POSTGRES_PASSWORD=password_here
POSTGRES_DB=database_name_here
POSTGRES_PORT=5434
POSTGRES_HOST=localhost
```

### 3. Install Python Dependencies

Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 4. Run Docker Compose

Start the PostgreSQL service using Docker Compose:

```bash
docker-compose up -d
```

This will set up a PostgreSQL database with the credentials specified in the .env file.

### 5. Running the Project

Execute the main pipeline script:

```bash
python main.py
```
- The extract() function in extractors.py will scrape the book data from the website.
- The transform() function in transformers.py will clean and transform the extracted data.
- The load_to_postgres() function in loader.py will load the transformed data into the PostgreSQL database.

### 6. Accessing the Data

To access the data, you can connect to the PostgreSQL database using a SQL client like pgAdmin or DBeaver, or use the command line:

```bash
psql -h localhost -p 5434 -U <username> -d <database_name>
```

# Logging

Logging is set up in the scripts to track the execution flow, including starting and completing data extraction, transformation, and loading. Any errors encountered during these processes are logged as well.