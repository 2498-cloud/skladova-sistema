class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    @staticmethod
    def from_dict(data):
        return Product(data["name"], data["quantity"], data["price"])

    def __str__(self):
        return f"{self.name} | {self.quantity} бр. | {self.price} лв."