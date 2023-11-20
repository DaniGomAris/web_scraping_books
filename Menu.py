from Program import GraphProgram

class Menu:
    def __init__(self, program):
        self.program = program


    def show_menu(self):
        print()
        print("--------------------------------")
        print("""
MENU
1) Guardar el grafo en archivo .GRAPHML
2) Listar los libros de un autor ordenados por fecha de lanzamiento
3) listar libros del mismo genero y mismo año
4) Listar a los autores de un genero ordenados por la cantidad de libros escritos del mismo genero
5) Listar libros por puntaje mayor al escrito
6) Listar libros por dinero escrito y genero
""")

        self.get_menu_answer()


    def get_menu_answer(self):
        option = input("Opción: ")
        print()

        if option == "1":
            print()
            self.program.save_graph_graphml()
            print("El grafo se ha guardado correctamente! Puedes verlo en Cytoscape")
            self.show_menu()

        if option == 2:
            print()
            self.program.list_books_by_author_same_years()
            self.show_menu()

        if option == 3:
            print()
            self.program.list_books_same_genre_by_years()
            self.show_menu()

        if option == 4:
            print()
            self.program.list_authors_same_genre_by_number_books()
            self.show_menu()

        if option == 5:
            print()
            self.program.list_books_same_by_valoration()
            self.show_menu()

        if option == 6:
            print()
            self.program.list_cart_price_gender()
            self.show_menu()

        