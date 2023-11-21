def list_books_same_genre_by_years(self, genre: str):
        """
        Listar libros del mismo género con información del año de publicación
        """
        # Inicializar una lista para almacenar los libros que cumplen con los criterios
        selected_books = []

        # Iterar a través de los nodos del grafo
        for book, data in self.graph.adj_list.items():
            # Verificar si el nodo representa un libro
            if data['type'] == 'Libro':
                # Verificar si el libro pertenece al género especificado
                if genre in data['neighbors']:
                    # Obtener el año de publicación del libro
                    publication_year = data['neighbors'][2]
                    selected_books.append((book, publication_year))

        # Verificar si se encontraron libros que cumplen con los criterios
        if selected_books:
            print()
            print(f"Libros del género '{genre}':")
            
            # Imprimir los libros seleccionados con sus años de publicación
            for book, year in selected_books:
                print(f"- {book} / Año de publicación: {year}")
        else:
            print(f"No se encontraron libros del género '{genre}'.")