class Phone:
    def __init__(self, brand: str, model: str, color: str):
        super().__init__()
        self.brand: str = brand
        self.model: str = model
        self.color: str = color