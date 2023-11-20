from Book import Book 

from bs4 import BeautifulSoup
import requests
import json
import re

class Scraping:

    def scrapper_books_info(self, book_url):
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
            match = re.search(r'First published (.+)', publication_scraping.text)
            published = match.group(1) if match else None

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
        genders_scraping = soup.find_all('span', class_='BookPageMetadataSection__genreButton')

        gender1_scraping = genders_scraping[0].find('span', class_='Button__labelItem') if genders_scraping else None
        gender1 = gender1_scraping.text if gender1_scraping else None

        gender2_scraping = genders_scraping[1].find('span', class_='Button__labelItem') if len(genders_scraping) > 1 else None
        gender2 = gender2_scraping.text if gender2_scraping else None

        gender3_scraping = genders_scraping[2].find('span', class_='Button__labelItem') if len(genders_scraping) > 2 else None
        gender3 = gender3_scraping.text if gender3_scraping else None

        book = Book(title, book_url, author, price, rating, pages, published, gender1, gender2, gender3)
        return book

    def scrapper_books_page(self):
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
                book_info = self.scrapper_books_info(href)
                books_list.append(book_info)
                print(book_info)

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
                "gender1": book.gender1,
                "gender2": book.gender2,
                "gender3": book.gender3
            }
            books_data.append(book_data)

        # Guardar la información en un archivo JSON
        with open('books.json', 'w', encoding='utf-8') as json_file:
            json.dump(books_data, json_file, ensure_ascii=False, indent=4)

        print(f"La información de las páginas 1 a 3 se ha guardado en books.json")
        return books_list

if __name__ == "__main__":
    scraper = Scraping()
    scraper.scrapper_books_page()
