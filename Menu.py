import sys

class Menu:
    def __init__(self, program):
        self.program = program

    def show_menu(self):
        """
        Menu de opciones para trabajar en el grafo
        """
        print()
        print("--------------------------------")
        print("""
MENU
1) Guardar el grafo en archivo .GRAPHML
2) Mostrar info de un vertice
3) Mostrar informacion de un libro
4) Listar los libros de un autor ordenados por fecha de lanzamiento
5) listar libros del mismo genero y mismo siglo
6) Listar a los autores de un genero ordenados por la cantidad de libros escritos del mismo genero
7) Listar libros por puntaje mayor escrito
8) Listar libros por dinero escrito y genero
9) Exit
""")

        self.get_menu_answer()

    def get_menu_answer(self):
        """
        Obtiene la respuesta desde la entrada option y realiza la acción 
        """
        option = int(input("Opción: "))
        print()
        print("--------------------------------")
        print()

        if option == 1:
            self.program.save_graph_graphml()
            print("El grafo se ha guardado correctamente! Puedes verlo en Cytoscape")
            self.show_menu()

        if option == 2:
            vertex = input("Name of vertex: ")
            self.program.vertex_information(vertex)
            self.show_menu()

        if option == 3:
            book = input("Name: ")
            self.program.show_book_info(book)
            self.show_menu()

        if option == 4:
            author = input("Author: ")
            self.program.list_books_by_author_same_years(author)
            self.show_menu()

        if option == 5:
            genre = input("Genre: ")
            decade_start = int(input("Decade: "))
            decade_end = decade_start + 10
            self.program.list_books_same_genre_by_decade(genre, decade_start, decade_end)
            self.show_menu()

        if option == 6:
            genre = input("Genre: ")
            self.program.list_authors_same_genre_by_number_books(genre)
            self.show_menu()

        if option == 7:
            valoration = int(input("Valoration: "))
            genre = input("Genre: ")
            self.program.list_books_same_by_valoration(valoration, genre)
            self.show_menu()

        if option == 8:
            price = int(input("Price: "))
            genre = input("Genre: ")
            self.program.list_cart_price_gender(price, genre)
            self.show_menu()
        
        if option == 9:
            sys.exit()