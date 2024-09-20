# main.py

from showroom import Showroom

def main():
    showroom = Showroom("Luxury Car Showroom")

   
    showroom.add_car(101, "Tesla", "Model X", 80000, 10)
    showroom.add_car(102, "BMW", "X5", 65000, 5)

    showroom.add_employee(201, "Alice", "Manager")
    showroom.add_employee(202, "Bob", "Salesperson")

  
    showroom.show_available_cars()

    showroom.search_car_by_brand("Tesla")

   
    showroom.search_employee_by_id(201)

if __name__ == "__main__":
    main()
