# employee.py

class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"Employee ID: {self.emp_id}\n Name: {self.name}\n Position: {self.position}"
