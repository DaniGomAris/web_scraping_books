from Scrapper import Scraping
from Book import Book
from Graph import Graph

import networkx as nx
import os
import json

class GraphProgram:
    
    def __init__(self, graph):
        self.graph = graph

    def save_graph(self):
        # Crear el grafo de Networkx
        G = nx.Graph()
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

        if os.path.exists("graph.graphml"):
            os.remove("graph.graphml")

        # Guardar el grafo en formato GraphML
        nx.write_graphml(G, "graph.graphml")