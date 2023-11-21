import networkx as nx
import os

class GraphProgram:

    def __init__(self, graph):
        self.graph = graph

    def save_graph_graphml(self):
        """
        Crea un grafo NetworkX y lo guarda en formato GraphML
        """
        # Crear un nuevo grafo NetworkX
        G = nx.Graph()

        # Agregar vertices y aristas al grafo NetworkX, segun el grafo
        for node, attr in self.graph.adj_list.items():
            if node is not None:
                G.add_node(node, **attr)
                for neighbor in attr['neighbors']:
                    if neighbor is not None:
                        G.add_edge(node, neighbor)

        # Convertir los atributos a cadenas de texto
        for node in G.nodes:
            attr = G.nodes[node]
            for key, value in attr.items():
                if isinstance(value, (list, type)):
                    attr[key] = str(value)

        # Eliminar el archivo existente si ya existe
        if os.path.exists("graph.graphml"):
            os.remove("graph.graphml")

        # Guardar el grafo en formato GraphML
        nx.write_graphml(G, "graph.graphml")


    def vertex_information(self, vertex_label: str):
        """
        Muestra la informacion de un vertice
        """
        # Verificar si el vertice esta en el grafo
        if vertex_label in self.graph.adj_list:
            vertex_data = self.graph.adj_list[vertex_label]
            vertex_type = vertex_data['type']
            neighbors = vertex_data['neighbors']
            print()
            print("------Data------")
            print(f"Name: {vertex_label}")
            print(f"Type: {vertex_type}")
            print(f"Neighbors: {neighbors}")
        else:
            print("No se encontro el vertice buscado")
    

    def show_book_info(self, title: str):
        """
        Mostrar información detallada de un libro dado su título
        """
        # Verificar si el título del libro está en el grafo
        if title in self.graph.adj_list:
            book_data = self.graph.adj_list[title]
            book_type = book_data['type']
            neighbors = book_data['neighbors']

            if book_type is 'Book':
                print()
                print("-----Book Information-----")
                print(f"- Autor: {neighbors[0]}")
                print(f"- Enlace: {neighbors[1]}")
                print(f"- Publicado en: {neighbors[2]}")
                print(f"- Valoración: {neighbors[3]}")
                print(f"- Precio: {neighbors[4]}")
                print(f"- Páginas: {neighbors[5]}")
                print(f"- Géneros: {neighbors[6]},{neighbors[7]},{neighbors[8]}")
            else:
                print(f"'{title}' no es un libro")
        else:
            print(f"No se encontró un libro con el título '{title}' en el grafo")


    def list_books_by_author_same_years(self, author: str):
        """
        Listar los libros del autor X organizados por año
        """
        # Verificar si el autor está presente en el grafo
        if author in self.graph.adj_list:
            # Obtener la información del autor desde el grafo
            vertex_data = self.graph.adj_list[author]
            neighbors = vertex_data['neighbors']

            if neighbors:
                print()
                print(f"Libros escritos por {author} ordenados por año:")
                
                books_with_years = []
                
                # Recorrer los libros del autor y obtener los años de publicación
                for book in neighbors:
                    book_year = self.graph.adj_list[book]['neighbors'][2]
                    books_with_years.append((book, book_year))
                
                # Ordenar los libros por año de publicación
                sorted_books = sorted(books_with_years, key=lambda x: x[1])

                # Mostrar la lista de libros ordenada por año
                for book, year in sorted_books:
                    print(f"- {book} / {year}")
            else:
                print(f"No se encontraron libros escritos por {author}")
        else:
            print("No se encontró el autor buscado")


    def list_books_same_genre_by_decade(self, genre: str, decade_start: int, decade_end: int):
        """
        Listar libros del mismo género en la misma década
        """
        if genre in self.graph.adj_list:
            vertex_data = self.graph.adj_list[genre]
            neighbors = vertex_data['neighbors']

            print()
            print(f"Libros del género {genre} en la década {decade_start}-{decade_end}:")
            
            books_in_decade = []
            
            # Iterar sobre los libros del género dado
            for book in neighbors:
                # Obtener el año de publicación del libro
                book_year_str = self.graph.adj_list[book]['neighbors'][2]
                book_year = int(book_year_str)

                # Verificar si el año está en la década especificada
                if decade_start <= book_year < decade_end:
                    books_in_decade.append((book, book_year))

            if books_in_decade:
                for book, year in books_in_decade:
                    print(f"- {book} / {year}")
            else:
                print(f"No se encontraron libros del género {genre} en la década {decade_start}-{decade_end}")
        else:
            print("No se encontró el género buscado")


    def list_authors_same_genre_by_number_books(self, genre: str):
        """
        Listar a los autores del género X ordenados por la cantidad de libros escritos en este género
        """
        authors_with_genre = {}  # Diccionario para contar la cantidad de libros por autor

        # Recorrer todos los nodos del grafo
        for node, data in self.graph.adj_list.items():
            # Verificar si el nodo es de tipo 'Autor'
            if data['type'] == 'Autor':
                # Obtener los libros escritos por el autor
                author_books = [neighbor for neighbor in data['neighbors'] if 'Libro' in self.graph.adj_list[neighbor]['type']]
                
                # Contar la cantidad de libros en el género específico
                books_count = 0
                
                for book in author_books:
                    if genre in self.graph.adj_list[book]['neighbors']:
                        books_count += 1

                # Si el autor tiene al menos un libro en el género, agregar al diccionario
                if books_count > 0:
                    authors_with_genre[node] = books_count

        # Ordenar la lista de autores por la cantidad de libros en ese género
        sorted_authors = sorted(authors_with_genre.items(), key=lambda x: x[1], reverse=True)

        # Mostrar los resultados
        print(f"Autores del género '{genre}' ordenados por la cantidad de libros escritos:")
        for author, book_count in sorted_authors:
            print(f"{author}: {book_count} libros")


    def list_books_same_by_valoration(self, valoration: int, genre: str):
        """
        Recomendar libros de puntaje mayor a X en el mismo género
        """
        # Inicializar una lista para almacenar los libros que cumplen con los criterios
        selected_books = []

        # Iterar a través de los nodos del grafo
        for book, data in self.graph.adj_list.items():
            # Verificar si el nodo representa un libro y pertenece al género especificado
            if data['type'] == 'Libro' and genre in data['neighbors']:
                # Obtener la valoración del libro
                book_valoration = data['neighbors'][4]  # Índice 4 corresponde a la valoración en los neighbors

                # Verificar si la valoración del libro es mayor al umbral especificado
                if book_valoration and float(book_valoration) > valoration:
                    selected_books.append((book, book_valoration))

        # Verificar si se encontraron libros que cumplen con los criterios
        if selected_books:
            print()
            print(f"Libros del género {genre} con valoración mayor a {valoration}:")
            
            # Imprimir los libros seleccionados
            for book, book_valoration in selected_books:
                print(f"- {book} / Valoración: {book_valoration}")
        else:
            print(f"No se encontraron libros del género {genre} con valoración mayor a {valoration}")


    def list_cart_price_gender(self, price: int, genre: str):
        """
        Recomendar lista libros con base en X cantidad de dinero y un grupo de géneros
        """

        # Inicializar una lista para almacenar los libros que cumplen con los criterios
        selected_books = []

        # Iterar a través de los nodos del grafo
        for book, data in self.graph.adj_list.items():
            # Verificar si el nodo representa un libro y pertenece al género especificado
            if data['type'] == 'Libro' and genre in data['neighbors']:
                # Obtener la valoración del libro
                book_valoration = data['neighbors'][3]  # Índice 4 corresponde al precio en los neighbors

                # Verificar si la valoración del libro es mayor al umbral especificado
                if book_valoration and float(book_valoration) <= price:
                    selected_books.append((book, book_valoration))

        # Verificar si se encontraron libros que cumplen con los criterios
        if selected_books:
            print()
            print(f"Libros del género {genre} con precio menor a {price}:")
            
            # Imprimir los libros seleccionados
            for book, book_valoration in selected_books:
                print(f"- {book} / Precio: {book_valoration}")
        else:
            print(f"No se encontraron libros del género {genre} con precio menor a: {price}")