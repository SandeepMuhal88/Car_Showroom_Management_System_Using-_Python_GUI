import tkinter as tk
from tkinter import messagebox
from showroom import Showroom

# Main application class for GUI
class ShowroomApp:
    def __init__(self, root, showroom):
        self.root = root
        self.showroom = showroom
        self.root.title("Car Showroom Management System")

        # Car management section
        self.car_frame = tk.Frame(root, padx=10, pady=10)
        self.car_frame.pack(fill='x')

        self.car_label = tk.Label(self.car_frame, text="Add New Car", font=("Arial", 14))
        self.car_label.pack()

        self.car_id_entry = self.create_entry("Car ID:", self.car_frame)
        self.car_brand_entry = self.create_entry("Car Brand:", self.car_frame)
        self.car_model_entry = self.create_entry("Car Model:", self.car_frame)
        self.car_price_entry = self.create_entry("Car Price:", self.car_frame)
        self.car_stock_entry = self.create_entry("Car Stock:", self.car_frame)

        self.add_car_button = tk.Button(self.car_frame, text="Add Car", command=self.add_car)
        self.add_car_button.pack(pady=5)

        # Employee management section
        self.employee_frame = tk.Frame(root, padx=10, pady=10)
        self.employee_frame.pack(fill='x')

        self.employee_label = tk.Label(self.employee_frame, text="Add New Employee", font=("Arial", 14))
        self.employee_label.pack()

        self.emp_id_entry = self.create_entry("Employee ID:", self.employee_frame)
        self.emp_name_entry = self.create_entry("Employee Name:", self.employee_frame)
        self.emp_position_entry = self.create_entry("Employee Position:", self.employee_frame)

        self.add_emp_button = tk.Button(self.employee_frame, text="Add Employee", command=self.add_employee)
        self.add_emp_button.pack(pady=5)

        # Show available cars and employees
        self.show_frame = tk.Frame(root, padx=10, pady=10)
        self.show_frame.pack(fill='x')

        self.show_cars_button = tk.Button(self.show_frame, text="Show Available Cars", command=self.show_cars)
        self.show_cars_button.pack(side='left', padx=5)

        self.show_employees_button = tk.Button(self.show_frame, text="Show Employees", command=self.show_employees)
        self.show_employees_button.pack(side='left', padx=5)

        # Search functionality
        self.search_frame = tk.Frame(root, padx=10, pady=10)
        self.search_frame.pack(fill='x')

        self.search_car_label = tk.Label(self.search_frame, text="Search Cars by Brand", font=("Arial", 14))
        self.search_car_label.pack()

        self.search_car_entry = self.create_entry("Brand:", self.search_frame)
        self.search_car_button = tk.Button(self.search_frame, text="Search", command=self.search_car)
        self.search_car_button.pack(pady=5)

        # Output box
        self.output_text = tk.Text(root, height=10, width=80)
        self.output_text.pack(pady=10)

    # Helper method to create labeled entry fields
    def create_entry(self, label_text, frame):
        label = tk.Label(frame, text=label_text)
        label.pack()
        entry = tk.Entry(frame, width=30)
        entry.pack()
        return entry

    # Function to add a new car
    def add_car(self):
        try:
            car_id = int(self.car_id_entry.get())
            brand = self.car_brand_entry.get()
            model = self.car_model_entry.get()
            price = float(self.car_price_entry.get())
            stock = int(self.car_stock_entry.get())

            self.showroom.add_car(car_id, brand, model, price, stock)
            messagebox.showinfo("Success", f"Car {brand} {model} added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data for the car.")

    # Function to add a new employee
    def add_employee(self):
        try:
            emp_id = int(self.emp_id_entry.get())
            name = self.emp_name_entry.get()
            position = self.emp_position_entry.get()

            self.showroom.add_employee(emp_id, name, position)
            messagebox.showinfo("Success", f"Employee {name} added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data for the employee.")

    # Function to display available cars
    def show_cars(self):
        self.output_text.delete(1.0, tk.END)
        if self.showroom.cars:
            self.output_text.insert(tk.END, "Available Cars:\n")
            for car in self.showroom.cars:
                self.output_text.insert(tk.END, f"{car}\n")
        else:
            self.output_text.insert(tk.END, "No cars available.\n")

    # Function to display employees
    def show_employees(self):
        self.output_text.delete(1.0, tk.END)
        if self.showroom.employees:
            self.output_text.insert(tk.END, "Employees:\n")
            for emp in self.showroom.employees:
                self.output_text.insert(tk.END, f"{emp}\n")
        else:
            self.output_text.insert(tk.END, "No employees available.\n")

    # Function to search for cars by brand
    def search_car(self):
        brand = self.search_car_entry.get()
        found_cars = [car for car in self.showroom.cars if car.brand.lower() == brand.lower()]

        self.output_text.delete(1.0, tk.END)
        if found_cars:
            self.output_text.insert(tk.END, f"Cars of brand {brand}:\n")
            for car in found_cars:
                self.output_text.insert(tk.END, f"{car}\n")
        else:
            self.output_text.insert(tk.END, f"No cars found for brand {brand}.\n")


# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    showroom = Showroom("Luxury Car Showroom")  # You can modify the name

    # Adding some sample data for testing
    showroom.add_car(101, "Tesla", "Model X", 80000, 5)
    showroom.add_car(102, "BMW", "X5", 65000, 3)
    showroom.add_employee(201, "Alice", "Manager")
    showroom.add_employee(202, "Bob", "Salesperson")

    app = ShowroomApp(root, showroom)
    root.mainloop()
