from abc import ABC, abstractmethod


BONUS_PERCENTAGE = 0.15
WORKLOAD = 8


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self._salary = salary
        self._department = department

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value

    def get_department(self):
        return self._department.name

    def set_department(self, department):
        self._department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    @classmethod
    def get_hours(cls):
        return WORKLOAD


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("managers", 1))

    def calc_bonus(self):
        return self.salary * BONUS_PERCENTAGE


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department("sellers", 2))
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, sale):
        self._sales = self.get_sales() + sale

    def calc_bonus(self):
        return self.get_sales() * BONUS_PERCENTAGE
