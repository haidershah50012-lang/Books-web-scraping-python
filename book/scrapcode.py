import requests
from bs4 import BeautifulSoup
import json 

base_url = "https://books.toscrape.com/"
page =  "catalogue/page-"
All_Books = []
def scrap(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    # html = soup.prettify()
    Books={}
    div = soup.find("div",class_="col-sm-8 col-md-9")
    ol = div.find("ol", class_="row")
    li = ol.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for i in li:
        name = i.find("h3").text.strip()
        Stock_price= i.find_all("div", class_="product_price")
        for i in Stock_price:
            price = i.find("p", class_="price_color").text.strip()
            stock = i.find("p", class_="instock availability").text.strip()

            Books[name] = {
                "price":price,
                "stock-availability":stock
            }
            All_Books.append(Books)

for i in range(1,50):
    urls = f"{base_url}{page}{i}.html"
    scrap(urls)
    print("Page 1 Scrapped")

with open("Books.json","w") as f:
    json.dump(All_Books,f,indent=4)

 