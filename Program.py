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
    
    def list_books_by_author_same_years(self, author: str):
        """
        Listar los libros del autor X ordenados por fecha de lanzamiento
        """
        pass

    def list_books_same_genre_by_years(self, genre: str, year: int):
        """
        Recomendar N libros del mismo género y de la misma década
        """
        pass

    def list_authors_same_genre_by_number_books(self, genre: str):
        """
        Listar a los autores del género X ordenados por la cantidad de libros escritos en este género
        """
        pass

    def list_books_same_by_valoration(self, valoration: int, genre: str):
        """
        Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios)
        """
        pass

    def list_cart_price_gender(self, price: int, genre: str):
        """
        Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios)
        """
        pass