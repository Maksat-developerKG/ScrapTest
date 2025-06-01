import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_doenv 


load_doenv

URL = os.getenv("PARSE_URL", "https://books.toscrape.com/")


def parse_book():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to get the page: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a['title']
        price = book.select_one(".price_color").text
        books.append({"title": title, "price":price})
        
    return books 

if __name__ == "__main__":
    books = parse_book()
    for book in books[:5]:
        print(f"{book['title']} - {book['price']}")
        