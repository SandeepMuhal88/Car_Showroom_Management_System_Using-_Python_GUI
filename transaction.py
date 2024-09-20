# transaction.py

class Transaction:
    def __init__(self, car, customer_name, amount):
        self.car = car
        self.customer_name = customer_name
        self.amount = amount

    def process_sale(self):
        if self.car.stock > 0:
            self.car.sell()
            print(f"Sale processed: {self.customer_name} bought {self.car.model} for ${self.amount}.")
        else:
            print("Sale failed: Car is out of stock!")
