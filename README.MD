# Enunciado

Diseñarán e implementarán un grafo para representar el conocimiento del top 300 de la lista “Books That Everyone Should Read At Least Once” de goodreads. Para hacer esta actividad, deberán: 
* Recopilar la información de este top 300 usando web scraping o la api de goodreads
** Tengan en cuenta que esta página usa paginación por cada 100 libros, así que deberán llegar a los demás por medio de las URLs. 
** De cada libro del top, deberán extraer su título, el nombre del autor, fecha de publicación completa (dd/mm/aa), su precio, su calificación y los tres primeros géneros en los que está clasificado el libro. Una imagen de ejemplo (léanlo que es muy bueno 😮):
![imagen info de web scraping](https://github.com/DaniGomAris/web_scraping_books/assets/99361024/ee670047-a6fb-4aac-afff-9f277a81066f)

* Diseñar un grafo para guardar la información y la relación. 
  * El diseño del grafo influirá directamente en cómo consultan la información alojada en éste.
  * Los nodos pueden ser la información que quieran, por ejemplo autores y libros; autores, libros y géneros; autores, libros, años, géneros, puntajes, etc.
  * Con las relaciones pasa algo similar, recuerden que las relaciones entre los nodos los dejará “viajar” entre nodos, así que dependerá de qué quieran responder o cómo lo quieran hacer para definir qué relaciones podrían existir. (Revisar anexo al final de este documento con un ejemplo de un grafo de conocimiento para películas). 
* Con base en este diseño, deberán implementar un grafo usando matriz de adyacencia o lista de adyacencia con toda la información recolectada.
* Con base en este grafo, deberán crear funciones para atender, de manera dinámica (con base en input del usuario), las siguientes funcionalidades:
  * Listar los libros del autor X ordenados por fecha de lanzamiento.
  * Recomendar N libros del mismo género y de la misma década que el libro X.
  * Listar a los autores del género X ordenados por la cantidad de libros escritos en este género.
  * Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios). 
  * Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios).
    * Por ejemplo, darme la mejor lista de compras posible para gastar 10 USD en los géneros clásico y horror.
      * El sistema deberá listar la mejor combinación de libros de estos dos géneros para maximizar la cantidad de libros a comprar con esa cantidad de dinero.
* Algunos recursos adicionales de web scraping:
  * https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607
  * https://realpython.com/python-web-scraping-practical-introduction/
  * https://www.geeksforgeeks.org/python-web-scraping-tutorial/
  * https://www.youtube.com/watch?v=XVv6mJpFOb0
* Una recomendación
  *Cuando validen el scraping y sepan que ya tienen toda la información bien, la pueden guardar en un archivo y seguir cargando desde allí para sus pruebas para que no les toque hacer todo ese proceso cada vez que corran el programa.


### Entrega y sustentación
* Puede realizar la práctica de manera individual o en parejas
* La entrega y sustentación será práctica e individual
  * La fecha, será entre el 22 y 24 de noviembre (por definir)
  * Recuerden que quien haga el parcial, lo hará en la fecha estipulada por la facultad. 
* Para la sustentación:
  * Traigan una imagen con la representación básica del grafo y la matriz o lista de adyacencia (ver anexo para ejemplo). Esto lo pueden hacer en diversas páginas online como grapheditor o graphonline, entre otras.
  * En la sustentación deberán justificar el diseño escogido y explicar cómo les aporta a la solución de las preguntas.
  * Plantearán, durante la sustentación, cómo abordarían una funcionalidad nueva que les plantearé. 
    * Esto será hablado, desde la lógica que implementaron.
* Implementación (30%) - Sustentación (70%)



## Anexo: ejemplo de representación de grafo usando información de IMDB (práctica semestre pasado)

Grafo para representar el top 250 de películas de IMDB, una base de datos en la nube sobre películas y shows de TV. 
* Este grafo contendrá información sobre personas de varios tipos: actor, directora, escritor o película → Nodos
* Un par de nodos v1 y v2 podrán tener las siguientes relaciones
  * acted_by de v1 a v2 si v1 es actuada por v2. En este caso v1 debe ser película y v2 debe ser actor.
  * acts_in de v1 a v2 si v1 actuó en v2. En este caso v1 debe ser actor y v2 película.
  * writes de v1 a v2 si v1 escribió a v2. En este caso, v1 debe ser escritora y v2 película.
  * directs de v1 a v2 si v1 dirigió a v2. En este caso, v1 debe ser directora y v2 película. 
  * directed_by de v1 a v2 si v1 es dirigida por v2. En este caso, v1 debe ser película y v2 director.
* Toda la información deberá ser extraída del top 250 de IMDB usando técnicas básicas de web scraping
* 
* Este es un ejemplo del grafo resultante y su matriz de adyacencia
![grafo](https://github.com/DaniGomAris/web_scraping_books/assets/99361024/f941ea4a-49a9-4d9d-a904-6f82d93458b2)
* En este ejemplo hay 8 nodos y 13 aristas que representan la relación entre los nodos. Tengan en cuenta que este grafo permite varias relaciones (multigrafo) y que además tiene un valor asociado a su relación (variación de grafo ponderado). 
* En el ejemplo, entre otras relaciones, tenemos que el actor “a1” actúa en la película “m1”, el escritor “w2” escribe la película “m2”, etc.
* Una posible representación de la matriz de adyacencia de este grafo sería:
![grafo example](https://github.com/DaniGomAris/web_scraping_books/assets/99361024/cc147010-3c1b-442c-82e4-a1f1b266b740)
