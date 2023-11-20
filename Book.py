class Book:
    """
    Clase para crear objetos de tipo libro
    """
    def __init__(self, title: str, link: str, author: str, price: float, valuation: float, pages: int, published: str, genre1: str, genre2: str, genre3: str):
        self.title: str= title
        self.link: str = link
        self.author: str = author
        self.published: str = published
        self.price: float = price
        self.valuation: float = valuation
        self.pages: int = pages
        self.genre1: str = genre1
        self.genre2: str = genre2
        self.genre3: str= genre3