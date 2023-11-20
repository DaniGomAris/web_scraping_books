import json

from Book import Book
from Graph import Graph
from Scrapper import Scraping
from Menu import Menu
from Program import GraphProgram

if __name__ == "__main__":
    while True:
        option = int(input("""
---------Books Graph---------
          1. Start  
          2. Exit
          Option: """))
        
        if option == 1:
            graph = Graph()
            scraper = Scraping()
            program = GraphProgram(graph)
            menu = Menu(program)

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
                genre1 = book_data["genre1"]
                genre2 = book_data["genre2"]
                genre3 = book_data["genre3"]

                # Crear el objeto Book solo si al menos un atributo no es None
                if any(value is not None for value in [price, author, link, published, valuation, pages, genre1, genre2, genre3]):
                    book = Book(title, link, author, price, valuation, pages, published, genre1, genre2, genre3)
                    books_list.append(book)

            for book in books_list:
                # Agrega un nodo para el libro
                graph.add_vertex(book.title, 'Libro')

                # Agrega nodos y aristas para otros atributos
                graph.add_vertex(book.author, 'Autor')
                graph.add_edge(book.title, book.author)
                graph.add_edge(book.author, book.title)

                graph.add_vertex(book.link, 'Link')
                graph.add_edge(book.title, book.link)
                graph.add_edge(book.link, book.title)
                
                graph.add_vertex(book.published, 'Publicación')
                graph.add_edge(book.title, book.published)
                graph.add_edge(book.published, book.title)

                graph.add_vertex(book.price, 'Precio')
                graph.add_edge(book.title, book.price)
                graph.add_edge(book.price, book.title)

                graph.add_vertex(book.valuation, 'Calificación')
                graph.add_edge(book.title, book.valuation)
                graph.add_edge(book.valuation, book.title)

                graph.add_vertex(book.pages, 'Páginas')
                graph.add_edge(book.title, book.pages)
                graph.add_edge(book.pages, book.title)

                graph.add_vertex(book.genre1, 'Género')
                graph.add_edge(book.title, book.genre1)
                graph.add_edge(book.genre1, book.title)

                graph.add_vertex(book.genre2, 'Género')
                graph.add_edge(book.title, book.genre2)
                graph.add_edge(book.genre2, book.title)

                graph.add_vertex(book.genre3, 'Género')
                graph.add_edge(book.title, book.genre3)
                graph.add_edge(book.genre3, book.title)

            menu.show_menu()

        else:
            break