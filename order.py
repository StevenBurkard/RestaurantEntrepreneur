class Order:
    def __init__(self, name, price, store):
        self.name = name
        self.price = price
        self.store = store

class Pizza(Order):
    def __init__(self):
        super().__init__("Pizza", 12.00, "Paul's Pizza")
    

class Pasta(Order):
    def __init__(self):
        super().__init__("Pasta", 8.50, "Bob's Bolognese")
    

class Salad(Order):
    def __init__(self):
        super().__init__("Salad", 5.25, "Caesar's Salad Bar")
    
