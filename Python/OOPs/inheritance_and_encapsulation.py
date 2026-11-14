import csv
class Item:
    pay_rate = 0.8
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price{price} is not greater than or equal to 0" # to check what is happening according to your expectation or not
        assert quantity >= 0, f"Quantity{quantity} is not greater than  or equal to 0"

        # Assign to self object
        self.__name = name # double underscore make it private so nobody change direct
        self.__price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    @property # property make price read only
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property # getter to read private name
    def name(self):
        return self.__name

    @name.setter # setter check length before changing name
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def __repr__(self):
        return f"Item: {self.__class__.__name__}, price: {self.__price}, quantity: {self.quantity}"

class Phone(Item):# inheritance
    all=[]
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )# the super class allows us to us multiple codes that are required again and again
        """assert price >= 0, f"Price{price} is not greater than or equal to 0" # to check what is happening according to your expectation or not"""
        assert broken_phones >= 0, f"Broken_phones{broken_phones} is not greater than  or equal to 0"
        self.broken_phones = broken_phones

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(Item.all)
print(Phone.all)

item1 = Item("MyItem", 750)
item1.name = "OtherItem" # this call the setter function
print(item1.name)
item1.apply_increment(0.2)
print(item1.price)
