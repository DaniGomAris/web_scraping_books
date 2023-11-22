from bs4 import BeautifulSoup
from dateutil import parser
import requests
import json
import re

from Book import Book 


class Scraping:
    
    @staticmethod
    def scrapper_books_info(book_url) -> Book:
        """
        Extrae la información de un libro a partir de su URL
        """
        result = requests.get(book_url)
        content = result.text
        soup = BeautifulSoup(content, 'html.parser')

        # Scraping titulo
        title_scraping = soup.find('h1', class_='Text Text__title1')
        title = title_scraping.text if title_scraping else None

        # Scraping autor
        author_scraping = soup.find('span', class_='ContributorLink__name')
        author = author_scraping.text if author_scraping else None

        # Scraping fecha de publicacion
        publication_scraping = soup.find('p', {'data-testid': 'publicationInfo'})
        published = None
        if publication_scraping:
            published_text = re.search(r'First published (.+)', publication_scraping.text).group(1)
            published = parser.parse(published_text).year

        # Scraping precio
        price_scraping = soup.find('button', {'class': 'Button--buy'})
        price_element = price_scraping.find('span', {'class': 'Button__labelItem'}) if price_scraping else None
        price_text = price_element.text if price_element else None
        match = re.search(r'\d+\.\d+', price_text) if price_text else None
        price = float(match.group()) if match and match.group() else None if match else None

        # Scraping valoracion
        valuation_scraping = soup.find('div', {'class': 'RatingStatistics__rating'})
        rating = float(valuation_scraping.text) if valuation_scraping else None

        # Scraping numero de paginas
        pages_scraping = soup.find('p', {'data-testid': 'pagesFormat'})
        pages = int(re.search(r'\d+', pages_scraping.text.strip()).group()) if pages_scraping else None

        # Scraping 3 primeros generos
        genres_scraping = soup.find_all('span', class_='BookPageMetadataSection__genreButton')

        genre1_scraping = genres_scraping[0].find('span', class_='Button__labelItem') if genres_scraping else None
        genre1 = genre1_scraping.text if genre1_scraping else None

        genre2_scraping = genres_scraping[1].find('span', class_='Button__labelItem') if len(genres_scraping) > 1 else None
        genre2 = genre2_scraping.text if genre2_scraping else None

        genre3_scraping = genres_scraping[2].find('span', class_='Button__labelItem') if len(genres_scraping) > 2 else None
        genre3 = genre3_scraping.text if genre3_scraping else None

        book = Book(title, book_url, author, price, rating, pages, published, genre1, genre2, genre3)
        return book


    @staticmethod
    def scrapper_books_page() -> list:
        """
        Scraping de la información de libros en varias paginas de Goodreads
        """
        url = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page={}"
        books_list = []

        for page_num in range(1, 4): 
            page_url = url.format(page_num)
            result = requests.get(page_url)
            content = result.text
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.find('table', class_="tableList js-dataTooltip")
            rows = table.find_all('tr')

            for row in rows:
                book_link = row.find('a', class_="bookTitle")  
                href = "https://www.goodreads.com/" + book_link['href']
                book_info = Scraping.scrapper_books_info(href)
                books_list.append(book_info)
                print(book_info)

        return books_list


    @staticmethod
    def create_json_file(books_list):
        """
        Crea un archivo JSON con la información de los libros
        """
        # Crear una lista de diccionarios con la información de los libros
        books_data = []
        for book in books_list:
            book_data = {
                "title": book.title,
                "author": book.author,
                "published": book.published,
                "price": book.price,
                "valuation": book.valuation,
                "pages": book.pages,
                "link": book.link,
                "genre1": book.genre1,
                "genre2": book.genre2,
                "genre3": book.genre3
            }
            books_data.append(book_data)

        # Guardar la información en un archivo JSON
        with open('books.json', 'w', encoding='utf-8') as json_file:
            json.dump(books_data, json_file, ensure_ascii=False, indent=4)

        print(f"La información de las páginas 1 a 3 se ha guardado en books.json")
        return books_list


# Para iniciar el scrapping
if __name__ == "__main__":
    scraper = Scraping()
    books_list = scraper.scrapper_books_page()
    scraper.create_json_file(books_list)