# inheritance parent Item class and child Phone class
class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero!"
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    # changed Item to self.__class__.__name__ so it print Phone for phone object
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
# Phone class taking all thing from Item class
class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        # super function call parent init so no need to write again
        super().__init__(name,price,quantity)
        assert broken_phones>=0,f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        self.broken_phones=broken_phones
phone1=Phone("jscPhonev10",500,5,1)
print(Item.all)
print(Phone.all)
#  encapsulation rest whole codeis  same only just making name and price private
class ItemEncapsulated:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0
        assert quantity>=0
        # double underscore make variable private nobody can changeit  directly
        self.__name=name
        self.__price=price
        self.quantity=quantity
        ItemEncapsulated.all.append(self)
    # property makes price read only
    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price=self.__price*self.pay_rate
    def apply_increment(self,increment_value):
        self.__price=self.__price+self.__price*increment_value
    # getter for reading private name
    @property
    def name(self):
        return self.__name
    # setter is allowing to change name only if length is less than 10
    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long!")
        else:
            self.__name=value
item1=ItemEncapsulated("MyItem",750)
item1.name="OtherItem"
print(item1.name)
item1.apply_increment(0.2)
print(item1.price)
