class Graph:
    def __init__(self, directed=True):
        self.adj_list = {} 
        self.directed = directed

    def get_neighbors(self, node_label):
        if node_label in self.adj_list:
            return self.adj_list[node_label]['neighbors']
        else:
            return []

    def add_vertex(self, node_label, node_type=None):
        if node_label not in self.adj_list:
            #los tipos de los nodo serán Title, Link, Author, Price, Valuation, Pages, Published, Genders
            self.adj_list[node_label] = {'type': node_type, 'neighbors': []}
            '''
            Estructura de un nodo
            ejemplo"
            pelicula1: {
                    'type': Libro,
                    'neighbors': ['escritor', 'pages', 'publication', ...]
                    }
            '''
    def add_edge(self, v1, v2):
        #Verificamos que los nodos si estén presente en la lista de adyacencia, si no estan, entonces se agregan
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)

        #le agregamos a v1 un nuevo vecino el cual será v2
        self.adj_list[v1]['neighbors'].append(v2)
        if not self.directed:
            #si el grafo no es dirigido, entonces tambien le agregaremos a v2 de vecino v1 
            self.adj_list[v2]['neighbors'].append(v1)

    def DFS(self, start, visited=None):
        if visited is None:
            visited = []

        if start not in self.adj_list:
            return "No existe el nodo inicial en el grafo."
        else:
            if start not in visited:
                visited.append(start)
                neighbors = self.get_neighbors(start)
                for n in neighbors:
                    self.DFS(n, visited)
        return visited 
    
    def print_graph(self):
        print("-------------- Grafo --------------")
        for node, data in self.adj_list.items():
            print(f"{node}:")
            print(f"'type': {data['type']},")
            print(f"'neighbors': {data['neighbors']}")
            print("-----------------------------------")