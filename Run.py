from Book import Book
from Graph import Graph
from Scrapper import Scraping

import json

if __name__ == "__main__":
    while True:
        option = int(input("""
---------Books Graph---------
          1. Start  
          2. Exit
          Option: """))

        if option == 1:
            my_graph = Graph()
            scraper = Scraping()

            with open("books.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

            # Crear una lista de libros con los datos del archivo JSON
            books_list = []
            for book_data in data:
                title = book_data["title"]
                link = book_data["link"]
                author = book_data["author"]
                published = book_data["published"]
                price = book_data["price"]
                valuation = book_data["valuation"]
                pages = book_data["pages"]
                gender1 = book_data["gender1"]
                gender2 = book_data["gender2"]
                gender3 = book_data["gender3"]

                # Crear el objeto Book solo si al menos un atributo no es None
                if any(value is not None for value in [price, author, link, published, valuation, pages, gender1, gender2, gender3]):
                    book = Book(title, link, author, price, valuation, pages, published, gender1, gender2, gender3)
                    books_list.append(book)

            for book in books_list:
                # Agrega un nodo para el libro
                my_graph.add_vertex(book.title, 'Libro')

                # Agrega nodos y aristas para otros atributos
                my_graph.add_vertex(book.author, 'Autor')
                my_graph.add_edge(book.title, book.author)
                my_graph.add_edge(book.author, book.title)

                my_graph.add_vertex(book.link, 'Link')
                my_graph.add_edge(book.title, book.link)
                my_graph.add_edge(book.link, book.title)
                
                my_graph.add_vertex(book.published, 'Publicación')
                my_graph.add_edge(book.title, book.published)
                my_graph.add_edge(book.published, book.title)

                my_graph.add_vertex(book.price, 'Precio')
                my_graph.add_edge(book.title, book.price)
                my_graph.add_edge(book.price, book.title)

                my_graph.add_vertex(book.valuation, 'Calificación')
                my_graph.add_edge(book.title, book.valuation)
                my_graph.add_edge(book.valuation, book.title)

                my_graph.add_vertex(book.pages, 'Páginas')
                my_graph.add_edge(book.title, book.pages)
                my_graph.add_edge(book.pages, book.title)

                my_graph.add_vertex(book.gender1, 'Género')
                my_graph.add_edge(book.title, book.gender1)
                my_graph.add_edge(book.gender1, book.title)

                my_graph.add_vertex(book.gender2, 'Género')
                my_graph.add_edge(book.title, book.gender2)
                my_graph.add_edge(book.gender2, book.title)

                my_graph.add_vertex(book.gender3, 'Género')
                my_graph.add_edge(book.title, book.gender3)
                my_graph.add_edge(book.gender3, book.title)

            my_graph.print_graph()

            break
        else:
            break
