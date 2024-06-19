from employee.employee import Employee


class EmployeeManager:

    def __init__(self):
        self._employees = []

    def read_employees(self):
        pass

    def write_employees(self):
        pass

    def add_employee(self, employee: Employee):
        for emp in self._employees:
            if emp == employee:
                raise ValueError("Employee already in the system")
        self._employees.append(employee)

    def remove_employee(self, index: int):
        if index < 0 or index >= len(self._employees):
            raise ValueError("Index out of range")
        return self._employees.pop(index)
