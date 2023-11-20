class Book:
    """
    Clase para crear objetos de tipo libro
    """
    def __init__(self, title: str, link: str, author: str, price: float, valuation: float, pages: int, published: str, gender1: str, gender2: str, gender3: str):
        self.title: str= title
        self.link: str = link
        self.author: str = author
        self.published: str = published
        self.price: float = price
        self.valuation: float = valuation
        self.pages: int = pages
        self.gender1: str = gender1
        self.gender2: str = gender2
        self.gender3: str= gender3