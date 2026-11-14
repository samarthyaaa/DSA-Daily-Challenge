class Item:
    pay_rate = 0.8
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price{price} is not greater than or equal to 0" # to check what is happening according to your expectation or not
        assert quantity >= 0, f"Quantity{quantity} is not greater than  or equal to 0"
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        #Action to execute
        Item.all.append(self)
    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def __connect(self, smtp_server):# hiding helper function using double underscore
        pass
    def __prepare_body(self):
        return f"Hello Someone. We have {self.__name} {self.quantity} times. Regards, JimShapedCoding"
    def __send(self):
        pass
    def send_email(self):# user only call this function and rest run inside
        self.__connect("")
        self.__prepare_body()
        self.__send()
class Phone(Item):# inheritance
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
        self.broken_phones = broken_phones
class Keyboard(Item):# polymorphism example
    pay_rate = 0.7 # only this line changed to give different discount for keyboard
    def __init__(self, name: str, price: float, quantity=0):
        super().__init__(
            name, price, quantity
        )
item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount() # uses 0.7 rate
print(item1.price)
item2 = Phone("jscPhone", 1000, 3)
item2.apply_discount() 
print(item2.price)
