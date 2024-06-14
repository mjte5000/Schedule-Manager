class Employee:
    """
    Creates an object representing an employee. Each employee has a last name, first name, email address, wage, and
    availability.
    :ivar _last: the last name of the employee
    :ivar _first: the first name of the employee
    :ivar _email: the email address of the employee
    :ivar _wage: the wage of the employee
    :ivar _availability: the availability of the employee
    """
    MIN_WAGE: float = 18.00

    def __init__(self, last: str, first: str, email: str, wage: int | str, availability: str):
        """
        Constructs an `Employee` object with the required attributes.
        :param last: the last name of the employee.
        :param first: the first name of the employee.
        :param email: the email address of the employee.
        :param wage: the hourly wage of the employee.
        :param availability: the availability of the employee.
        """
        self._last = None
        self._first = None
        self._email = None
        self._wage = None
        self._availability = None

        self.set_last(last)
        self.set_first(first)
        self.set_email(email)
        self.set_wage(wage)
        self.set_availability(availability)

    def __eq__(self, other):
        """
        Returns whether an employee is equal to another object.
        :param other: the object to compare this instance to.
        :return: `True` if the objects are equal, `False` otherwise.
        """
        if not isinstance(other, Employee):
            return False
        if self.last != other.last:
            return False
        if self.first != other.first:
            return False
        return True

    def __str__(self):
        """
        Returns a string representation of the object.
        :return: the string representation of the object.
        """
        return self._last + ',' + self._first + ',' + self._email + ',' + str(self._wage) + ',' + self._availability

    def set_last(self, last: str):
        """
        Sets the last name of the employee. The last name must not be empty.
        :param last: the last name of the employee.
        :raises ValueError: if the last name is empty.
        """
        if last is None or last == '':
            raise ValueError('Last cannot be empty')
        self._last = last

    def last(self):
        """
        Returns the last name of the employee.
        :return: the last name of the employee.
        """
        return self._last

    def set_first(self, first: str):
        """
        Sets the first name of the employee. The first name must not be empty.
        :param first: the first name of the employee.
        :return: the first name of the employee.
        :raises ValueError: if the first name is empty.
        """
        if first is None or first == '':
            raise ValueError('First cannot be empty')
        self._first = first

    def first(self):
        """
        Returns the first name of the employee.
        :return: the first name of the employee.
        """
        return self._first

    def set_email(self, email: str):
        """
        Sets the email address of the employee. The address must not be empty. It also must contain an "@" symbol and a
        "." symbol in that order.
        :param email: the email address of the employee.
        :raises ValueError: if the email address is invalid; the address must contain an "@" symbol and a ". symbol in
        that order.
        """
        if email is None or email == '':
            raise ValueError('Email cannot be empty')
        if '@' not in email:
            raise ValueError('Email must contain "@"')
        if '.' not in email:
            raise ValueError('Email must contain "."')
        if email.find('@') > email.find('.'):
            raise ValueError('Email must contain "@" before "."')
        self._email = email

    def email(self):
        """
        Returns the email address of the employee.
        :return: the email address of the employee.
        """
        return self._email

    def set_wage(self, wage: int | str):
        """
        Sets the hourly wage of the employee. The wage must be greater than or equal to the minimum hourly wage.
        :param wage: the hourly wage of the employee.
        :raises ValueError: if the wage is not a number or is less than the minimum hourly wage.
        """
        if wage is None or wage == '':
            raise ValueError('Wage cannot be empty')
        if type(wage) is str:
            try:
                wage = float(wage)
            except ValueError:
                raise ValueError('Wage must be a floating point number')
        if wage < Employee.MIN_WAGE:
            raise ValueError(f'Wage must be greater than or equal to {Employee.MIN_WAGE}')
        self._wage = wage

    def wage(self):
        """
        Returns the hourly wage of the employee.
        :return: the hourly wage of the employee.
        """
        return self._wage

    def set_availability(self, availability: str):
        """
        Sets the availability of the employee. The availability must be a string containing only the days of the week
        (U, M, T, W, H, F, and S).
        :param availability: the availability of the employee.
        :raises ValueError: if the availability is invalid. The availability must be a string containing only the days
        of the week represented by U, M, T, W, H, F, and S. Each day must only appear once in the string
        """
        if availability is None or availability == '':
            raise ValueError('Availability cannot be empty')
        avail = availability.upper()
        avail_list = Employee._availability_list(availability)
        if sum(avail_list) != len(avail):
            raise ValueError('Availability must only contain the letters U, M, T, W, H, F, and S')
        for count in avail_list:
            if count > 1:
                raise ValueError('Availability must only contain one letter per day of the week')
        self._availability = availability

    def availability(self):
        """
        Returns the availability of the employee as a string.
        :return: the availability of the employee as a string.
        """
        return self._availability

    def availability_list(self):
        """
        Returns the availability of the employee as a list. There are seven elements in the list, each representing the
        employee's availability throughout the week from Sunday to Saturday. Each element is either 1 if the employee is
        available or 0 if they are not.
        :return: the availability of the employee as a list.
        """
        return Employee.availability_list(self._availability)

    @staticmethod
    def _availability_list(availability: str):
        """
        Returns the availability of the employee as a list given the availability string. There are seven elements in
        the list, each representing the employee's availability throughout the week from Sunday to Saturday. Each
        element is either 1 if the employee is available or 0 if they are not.
        :param availability: the availability of the employee.
        :return: the availability of the employee as a list.
        """
        return [availability.count('U'),
                availability.count('M'),
                availability.count('T'),
                availability.count('W'),
                availability.count('H'),
                availability.count('F'),
                availability.count('S')]