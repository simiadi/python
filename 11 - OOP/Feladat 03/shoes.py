class Shoes:
    def __init__(self):
        super().__init__()
        self.brand: str = None
        self.model: str = None
        self.colorway: str = None
        self.price: int = 0
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.colorway} {self.price}$"