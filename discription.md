# Books Scraper - Python

A web scraper built with Python that extracts book data
from books.toscrape.com across multiple pages.

## What it Does
- Scrapes 50 pages of books automatically
- Extracts book name, price, and stock availability
- Saves all data into a clean Books.json file

## Libraries Used
- requests
- beautifulsoup4
- json

## How to Run
1. Install libraries:
   pip install requests beautifulsoup4

2. Run the scraper:
   python scraper.py

3. Output will be saved in Books.json

## Output Format
```json
{
    "Book Name": {
        "price": "£51.77",
        "stock-availability": "In stock"
    }
}
```

## Concepts Used
- HTTP requests with requests library
- HTML parsing with BeautifulSoup
- Nested HTML element navigation
- JSON data storage
- Loops and functions
- Multi-page scraping

## Author
BSIT Student | Aspiring Python Developer
University of Education
