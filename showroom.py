# showroom.py

from car import Car
from employee import Employee

class Showroom:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.cars = []

    # Add a new car to the showroom
    def add_car(self, car_id, brand, model, price, stock):
        new_car = Car(car_id, brand, model, price, stock)
        self.cars.append(new_car)
        print(f"Car {brand} {model} added to showroom.")

    # Add a new employee
    def add_employee(self, emp_id, name, position):
        new_employee = Employee(emp_id, name, position)
        self.employees.append(new_employee)
        print(f"Employee {name} added to showroom.")

    # Display all available cars
    def show_available_cars(self):
        if self.cars:
            print("Available cars in the showroom:")
            for car in self.cars:
                if car.stock > 0:
                    print(car)
        else:
            print("No cars available.")

    # Search for a car by brand
    def search_car_by_brand(self, brand):
        found_cars = [car for car in self.cars if car.brand.lower() == brand.lower()]
        if found_cars:
            for car in found_cars:
                print(car)
        else:
            print(f"No cars found for brand {brand}")

    # Search for an employee by ID
    def search_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print(employee)
                return
        print(f"No employee found with ID {emp_id}")
