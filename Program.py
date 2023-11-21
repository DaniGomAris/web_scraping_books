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


    def vertex_information(self, vertex_label):
        """
        Muestra la informacion de un vertice
        """
        if vertex_label in self.graph.adj_list:
            vertex_data = self.graph.adj_list[vertex_label]
            vertex_type = vertex_data['type']
            neighbors = vertex_data['neighbors']
            print()
            print("----Data----")
            print(f"Name: {vertex_label}")
            print(f"Type: {vertex_type}")
            print(f"Neighbors: {neighbors}")
        else:
            print("No se encontro el vertice buscado")
    

    def list_books_by_author_same_years(self, author: str):
        """
        Listar los libros del autor X organizados por año
        """
        if author in self.graph.adj_list:
            # Obtener la información del autor desde el grafo
            vertex_data = self.graph.adj_list[author]
            neighbors = vertex_data['neighbors']

            if neighbors:
                print()
                print(f"Libros escritos por {author} ordenados por año:")
                
                books_with_years = []
                
                for book in neighbors:
                    book_year = self.graph.adj_list[book]['neighbors'][2]

                    books_with_years.append((book, book_year))
                
                sorted_books = sorted(books_with_years, key=lambda x: x[1])

                for book, year in sorted_books:
                    print(f"- {book} / {year}")
            else:
                print(f"No se encontraron libros escritos por {author}")
        else:
            print("No se encontró el autor buscado")



    def list_books_same_genre_by_years(self, genre: str, year: int):
        """
        Recomendar N libros del mismo género y de la misma década
        """
        pass


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
                genre_books_count = sum(1 for book in author_books if genre in self.graph.adj_list[book]['neighbors'])

                # Si el autor tiene al menos un libro en el género, agregar al diccionario
                if genre_books_count > 0:
                    authors_with_genre[node] = genre_books_count

        # Ordenar la lista de autores por la cantidad de libros en ese género
        sorted_authors = sorted(authors_with_genre.items(), key=lambda x: x[1], reverse=True)

        # Mostrar los resultados
        print(f"Autores del género '{genre}' ordenados por la cantidad de libros escritos:")
        for author, book_count in sorted_authors:
            print(f"{author}: {book_count} libros")


    def list_books_same_by_valoration(self, valoration: int, genre: str):
        """
        Recomendar libros de puntaje mayor a X dentro de un grupo de géneros
        """
        pass


    def list_cart_price_gender(self, price: int, genre: str):
        """
        Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros
        """
        pass