class Book:
    """
    Clase para crear objetos de tipo libro
    """
    def __init__(self, title, link, author, price, valuation, pages, published, genders):
        self.title = title
        self.link = link
        self.author = author
        self.published = published
        self.price = price
        self.valuation = valuation
        self.pages = pages
        self.genders = genders