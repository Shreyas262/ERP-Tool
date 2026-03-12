#assets_name, value
#Hardware/ Software
#condition/ expiry
from Employees import Entity

class Assets(Entity):
    def __init__(self, asset_id, asset_type, name, value):
        self.__asset_id = asset_id
        self.__asset_type = asset_type
        self.__name = name
        self.__value = value

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def asset_type(self):
        return self.__asset_type

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    def get_current_value(self):
        return self.value

    def get_details(self):
        return f'Asset ID: {self.__asset_id} | Asset Type: {self.__asset_type} | Name: {self.__name} | Value: {self.__value}'

    def __add__(self, other):
        return self.value + other.value

class Hardware(Assets):
    def __init__(self, asset_id, asset_type, name, value, condition, depreciation:float = 0.0):
        super().__init__(asset_id, asset_type, name, value)
        self.__condition = condition
        self.__depreciation = depreciation

    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        self.__condition = value

    @property
    def depreciation(self):
        return self.__depreciation

    @depreciation.setter
    def depreciation(self, value):
        self.__depreciation = value

    def calculate_depreciation(self, years):
        current_value = self.value * (0.9 ** years)
        self.__depreciation = round(current_value, 2)
        return self.__depreciation

    def get_current_value(self):
        return self.__depreciation if self.__depreciation else self.value

    def get_details(self):
        base_data = super().get_details()
        return f'{base_data} | Condition: {self.__condition} | Depreciated Value: {self.__depreciation}'

class Software(Assets):
    def __init__(self, asset_id, asset_type, name, value, expiry_date):
        super().__init__(asset_id, asset_type, name, value)
        self.__expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self.__expiry_date

    def get_details(self):
        base_data = super().get_details()
        return f'{base_data} | Expiry_Date: {self.expiry_date}'