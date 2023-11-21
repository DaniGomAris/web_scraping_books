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
2) Mostrar info
3) Listar los libros de un autor ordenados por fecha de lanzamiento
4) listar libros del mismo genero y mismo año
5) Listar a los autores de un genero ordenados por la cantidad de libros escritos del mismo genero
6) Listar libros por puntaje mayor escrito
7) Listar libros por dinero escrito y genero
8) Exit
""")

        self.get_menu_answer()

    def get_menu_answer(self):
        """
        Obtiene la respuesta desde la entrada option y realiza la acción 
        """
        option = int(input("Opción: "))
        print()

        if option == 1:
            self.program.save_graph_graphml()
            print("El grafo se ha guardado correctamente! Puedes verlo en Cytoscape")
            self.show_menu()

        if option == 2:
            vertex = input("Name: ")
            self.program.vertex_information(vertex)
            self.show_menu()

        if option == 3:
            author = input("Author: ")
            self.program.list_books_by_author_same_years(author)
            self.show_menu()

        if option == 4:
            genre = input("Genre: ")
            year = input("Year: ")
            self.program.list_books_same_genre_by_years(genre, year)
            self.show_menu()

        if option == 5:
            genre = input("Genre: ")
            self.program.list_authors_same_genre_by_number_books(genre)
            self.show_menu()

        if option == 6:
            valoration = input("Valoration: ")
            genre = input("Genre: ")
            self.program.list_books_same_by_valoration(valoration, genre)
            self.show_menu()

        if option == 7:
            price = input("Price: ")
            genre = input("Genre: ")
            self.program.list_cart_price_gender(price, genre)
            self.show_menu()
        
        if option == 8:
            sys.exit()