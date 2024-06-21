from employee.employee import Employee
import os


class EmployeeManager:
    """
    Manages a list of employees.
    :ivar _employees: list of employees to manage
    """

    def __init__(self):
        """
        Constructs an `EmployeeManager` object with the required attributes.
        """
        self._employees = []

    def read_employees(self, file: str):
        """
        Reads employees from a file into the `EmployeeManager`.
        :param file: the file to read
        :raises FileNotFoundError: if the file does not exist
        """
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
        """
        Writes employees to a file from the `EmployeeManager`.
        :param file: the file to write to
        :raises PermissionError: if the user does not have permission to write to the file
        """
        try:
            with open(file, 'w') as f:
                for employee in self._employees:
                    f.write(str(employee))
        except PermissionError:
            raise PermissionError('You do not have permission to write the file.')

    def add_employee(self, employee: Employee):
        """
        Adds an employee to the `EmployeeManager`. The employee cannot already exist in the manager as defined by the
        `Employee`'s __eq__ method.
        :param employee: the employee to add
        :raises ValueError: if the employee already exists in the manager
        """
        for emp in self._employees:
            if emp == employee:
                raise ValueError("Employee already in the system")
        self._employees.append(employee)

    def remove_employee(self, index: int):
        if index < 0 or index >= len(self._employees):
            raise ValueError("Index out of range")
        return self._employees.pop(index)
