from Book import Book
from bs4 import BeautifulSoup
import requests
import json
import os

def scrapper_books_info(book_url):
    pass

def scrapper_books_page():
    url = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page={}"
    books_list = []

    # Numero de paginas, de la 1 a la 3
    for page_num in range(1, 4): 
        page_url = url.format(page_num)
        result = requests.get(page_url)
        content = result.text
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find('table', class_="tableList js-dataTooltip")
        rows = table.find_all('tr')

        for row in rows:
            book_link = row.find('a', class_="bookTitle")  
            #print(book_link.text) # Imprimir nombres de los libros
            href = "https://www.goodreads.com/" + book_link['href']
            book_info = scrapper_books_info(href)
            books_list.append(book_info)
        
scrapper_books_page()