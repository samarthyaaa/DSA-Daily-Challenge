# abstraction hiding unwanted function from user
class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        self.__name=name
        self.__price=price
        self.quantity=quantity
        Item.all.append(self)
    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price=self.__price*self.pay_rate
    # putting double underscore to hide this helperfrom outside
    def __connect(self,smtp_server):
        pass
    def __prepare_body(self):
        return f"Hello Someone. We have {self.__name} {self.quantity} times. Regards, JimShapedCoding"
    def __send(self):
        pass
    # user only calls send_email and it run all hidden function inside
    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
# polymorphism whole code is same only just adding Keyboard class
class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        super().__init__(name,price,quantity)
        self.broken_phones=broken_phones
class Keyboard(Item):
    # this line changes the giving 0.7 discount rate for keyboard
    pay_rate=0.7
    def __init__(self,name:str,price:float,quantity=0):
        super().__init__(name,price,quantity)
# same apply_discount function give different answer for keyboard and phone
item1=Keyboard("jscKeyboard",1000,3)
item1.apply_discount()
print(item1.price)
item2=Phone("jscPhone",1000,3)
item2.apply_discount()
print(item2.price)
