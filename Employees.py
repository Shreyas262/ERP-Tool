# phase 1 employees blueprint creation
from abc import ABC, abstractmethod

#1. The Master Template (Abstract Base Class)
class Entity(ABC):
    @abstractmethod
    def get_details(self):
        """Every child class must implement this or the python will complain."""
        pass


#2. Employee Blueprint
class Employee(Entity):
    def __init__(self, emp_id:str, name:str, role:str = 'staff', salary:float=150000.00):
        # Data is private
        self.__emp_id = emp_id
        self.__name = name
        self.__role = role
        self.__salary = salary
        self.assets = []

    # Getter for Emp id
    @property
    def emp_id(self):
        return self.__emp_id

    #getter and setter for salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary:float):
        self.__salary = new_salary

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name:str):
        self.__name = new_name

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, new_role:str):
        self.__role = new_role

    def get_details(self):
        return f'ID: {self.emp_id} | Name: {self.__name} | Role: {self.__role} | Salary: {self.__salary}'

    # Dunder Method: Making our object like real data
    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()
    def __eq__(self, other):
        return self.__emp_id == other.emp_id


#3. The manager Class(Inheritance from Employe)
class Manager(Employee):
    def __init__(self, emp_id: str, name: str, role: str = 'manager', salary:float = 20000.00, bonus:float = 1000.00):
        super().__init__(emp_id, name, role, salary)
        self.__bonus = bonus

    #polymorphism method overriding will change parent class method in child class
    def get_details(self):
        base = super().get_details()
        return f'{base} | Bonus: {self.__bonus}'

    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, new_bonus:float):
        self.__bonus = new_bonus

    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()
    def __eq__(self, other):
        return self.__emp_id == other.emp_id

