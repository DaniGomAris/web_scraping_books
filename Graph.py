class Graph:
    
    def __init__(self, directed: bool = True):
        self.adj_list: dict = {} 
        self.directed: bool = directed


    def add_vertex(self, node_label, node_type=None):
        """
        Agrega un nuevo vertice al grafo
        """
        if node_label not in self.adj_list:
            # Los tipos de los vertices serán: Book, Title, Link, Author, Price, Valuation, Pages, Published, genre1, genre2, genre3
            self.adj_list[node_label] = {'type': node_type, 'neighbors': []}
            """
            Estructura de un vertice
            nombre del vertice: {'type': tipo del nodo, 'neighbors': []}
            ejemplo:
            {
                'To Kill a Mockingbird': {
                    'type': 'Book',
                    'neighbors': ['Harper Lee', 'https://www.goodreads.com//book/show/2657.To_Kill_a_Mockingbird', ...]
                }
            }
            """


    def add_edge(self, v1, v2):
        """
        Agrega una arista entre dos nodos en el grafo
        """
        # Verificamos que los nodos si estén presente en la lista de adyacencia, si no estan, entonces se agregan
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        # Le agregamos a v1 un nuevo vecino el cual será v2
        self.adj_list[v1]['neighbors'].append(v2)
        if not self.directed:
            # Si el grafo no es dirigido, entonces tambien le agregaremos a v2 de vecino v1 
            self.adj_list[v2]['neighbors'].append(v1)

    
    def print_graph(self):
        """
        Imprime la información del grafo en la consola
        """
        print("-------------- Grafo --------------")
        for node, data in self.adj_list.items():
            print(f"{node}:")
            print(f"'type': {data['type']},")
            print(f"'neighbors': {data['neighbors']}")
            print("-----------------------------------")