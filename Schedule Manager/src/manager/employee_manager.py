from employee.employee import Employee

import os


class EmployeeManager:

    def __init__(self):
        self._employees = []

    def read_employees(self, file: str):
        if not os.path.exists(file):
            raise FileNotFoundError('The file specified does not exist.')
        with open(file, 'r') as f:
            for line in f.readlines():
                employee = Employee(*line.split(","))
                try:
                    self.add_employee(employee)
                except ValueError:
                    pass

    def write_employees(self, file: str):
        try:
            with open(file, 'w') as f:
                for employee in self._employees:
                    f.write(str(employee))
        except PermissionError:
            raise PermissionError('You do not have permission to write the file.')

    def add_employee(self, employee: Employee):
        for emp in self._employees:
            if emp == employee:
                raise ValueError("Employee already in the system")
        self._employees.append(employee)

    def remove_employee(self, index: int):
        if index < 0 or index >= len(self._employees):
            raise ValueError("Index out of range")
        return self._employees.pop(index)
