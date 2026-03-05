#assets_name, value
#Hardware/ Software
#condition/ expiry
from Employees import Entity

class Assets(Entity):
    def __init__(self, asset_id, name, value):
        self.__asset_id = asset_id
        self.__name = name
        self.__value = value

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def value(self):
        return self.__value

    def calculate_depreciation(self, years):
        current_value = self.__value * (0.9 ** years)
        return round(current_value, 2)

    def get_details(self):
        return f'Asset ID: {self.__asset_id} | Name: {self.__name} | Value: {self.__value}'

    def __add__(self, other):
        return self.value + other.value

class Hardware(Assets):
    def __init__(self, asset_id, name, value, condition):
        super().__init__(asset_id, name, value)
        self.__condition = condition

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        self.__condition = value

    def get_details(self):
        base_data = super().get_details()
        return f'{base_data} | Condition: {self.__condition}'

class Software(Assets):
    def __init__(self, asset_id, name, value, expiry_date):
        super().__init__(asset_id, name, value)
        self.__expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self.__expiry_date

    def get_details(self):
        base_data = super().get_details()
        return f'{base_data} | Expiry_Date: {self.expiry_date}'