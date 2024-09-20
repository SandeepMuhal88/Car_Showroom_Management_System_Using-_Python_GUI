# Car.py
 
class Car:
    def __init__(self, car_id, brand, model, price, stock):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock  # Number of cars available in stock

    def Car_deatils(self):
        return f"Car ID: {self.car_id}\n Brand: {self.brand}\n Model: {self.model}\n Price: {self.price}\n Stock: {self.stock}"

    def sell(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"{self.model} sold successfully!")
        else:
            print("Out of stock!")

# x=int(input("Enter car Id:-"))
# y=input("Enter car Brand :-")
# z=input("Enter car Model Number:-")
# Price=int(input("Enter Car proce:- "))
# st=int(input("Enter car stock:-"))
# obj=Car(x,y,z,Price,st)
# print(obj.__str__())
# obj.sell()