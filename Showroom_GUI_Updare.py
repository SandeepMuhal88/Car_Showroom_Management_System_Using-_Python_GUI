import tkinter as tk
from tkinter import messagebox, ttk
from showroom import Showroom

class ShowroomApp:
    def __init__(self, root, showroom):
        self.root = root
        self.showroom = showroom
        self.root.title("Car Showroom Management System")
        self.root.geometry("600x600")  # Set window size

        # Styling
        self.bg_color = "#f4f4f4"
        self.root.config(bg=self.bg_color)
        self.default_font = ("Arial", 12)

        # Section: Add New Car
        self.create_car_section()

        # Section: Add New Employee
        self.create_employee_section()

        # Section: Display and Search
        self.create_show_search_section()

        # Output Section: Displays results (scrollable text box)
        self.create_output_section()

    def create_car_section(self):
        car_frame = tk.LabelFrame(self.root, text="Add New Car", padx=10, pady=10, bg=self.bg_color, font=self.default_font)
        car_frame.pack(fill='x', padx=10, pady=5)

        self.car_id_entry = self.create_entry(car_frame, "Car ID:")
        self.car_brand_entry = self.create_entry(car_frame, "Car Brand:")
        self.car_model_entry = self.create_entry(car_frame, "Car Model:")
        self.car_price_entry = self.create_entry(car_frame, "Car Price:")
        self.car_stock_entry = self.create_entry(car_frame, "Car Stock:")

        add_car_button = tk.Button(car_frame, text="Add Car", command=self.add_car, bg="#4CAF50", fg="white", font=self.default_font)
        add_car_button.pack(pady=5)

    def create_employee_section(self):
        emp_frame = tk.LabelFrame(self.root, text="Add New Employee", padx=10, pady=10, bg=self.bg_color, font=self.default_font)
        emp_frame.pack(fill='x', padx=10, pady=5)

        self.emp_id_entry = self.create_entry(emp_frame, "Employee ID:")
        self.emp_name_entry = self.create_entry(emp_frame, "Employee Name:")
        self.emp_position_entry = self.create_entry(emp_frame, "Employee Position:")

        add_emp_button = tk.Button(emp_frame, text="Add Employee", command=self.add_employee, bg="#4CAF50", fg="white", font=self.default_font)
        add_emp_button.pack(pady=5)

    def create_show_search_section(self):
        show_frame = tk.Frame(self.root, padx=10, pady=10, bg=self.bg_color)
        show_frame.pack(fill='x')

        show_cars_button = tk.Button(show_frame, text="Show Available Cars", command=self.show_cars, bg="#2196F3", fg="white", font=self.default_font)
        show_cars_button.pack(side='left', padx=5)

        show_employees_button = tk.Button(show_frame, text="Show Employees", command=self.show_employees, bg="#2196F3", fg="white", font=self.default_font)
        show_employees_button.pack(side='left', padx=5)

        search_frame = tk.LabelFrame(self.root, text="Search Cars by Brand", padx=10, pady=10, bg=self.bg_color, font=self.default_font)
        search_frame.pack(fill='x', padx=10, pady=5)

        self.search_car_entry = self.create_entry(search_frame, "Brand:")
        search_car_button = tk.Button(search_frame, text="Search", command=self.search_car, bg="#FF9800", fg="white", font=self.default_font)
        search_car_button.pack(pady=5)

    def create_output_section(self):
        output_frame = tk.Frame(self.root, padx=10, pady=10, bg=self.bg_color)
        output_frame.pack(fill='both', expand=True)

        output_label = tk.Label(output_frame, text="Output:", bg=self.bg_color, font=self.default_font)
        output_label.pack(anchor='w')

        self.output_text = tk.Text(output_frame, height=10, width=80, font=self.default_font)
        self.output_text.pack(side='left', fill='both', expand=True)

        # Add scrollbars for output
        scroll_bar = tk.Scrollbar(output_frame, command=self.output_text.yview)
        scroll_bar.pack(side='right', fill='y')
        self.output_text.config(yscrollcommand=scroll_bar.set)

    # Function to create labeled entry fields
    def create_entry(self, frame, label_text):
        label = tk.Label(frame, text=label_text, bg=self.bg_color, font=self.default_font)
        label.pack(anchor='w')
        entry = tk.Entry(frame, font=self.default_font, width=30)
        entry.pack(pady=2)
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
            self.clear_entries([self.car_id_entry, self.car_brand_entry, self.car_model_entry, self.car_price_entry, self.car_stock_entry])
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
            self.clear_entries([self.emp_id_entry, self.emp_name_entry, self.emp_position_entry])
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data for the employee.")

    # Function to clear entries after data is added
    def clear_entries(self, entries):
        for entry in entries:
            entry.delete(0, tk.END)

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
    showroom = Showroom("Luxury Car Showroom")

    # Add some sample data for testing
    showroom.add_car(101, "Tesla", "Model X", 80000, 5)
    showroom.add_car(102, "BMW", "X5", 65000, 3)
    showroom.add_employee(201, "Alice", "Manager")
    showroom.add_employee(202, "Bob", "Salesperson")

    app = ShowroomApp(root, showroom)
    root.mainloop()
