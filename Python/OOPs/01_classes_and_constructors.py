# Classes
class ItemBasic:
    pass
# Creating instance and assigning attributes
item_basic=ItemBasic()
item_basic.name="Phone"
item_basic.price=100
item_basic.quantity=5
print(type(item_basic))
print(type(item_basic.name))
# Methods, __init__ Constructor & Validation
class Item:
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign validated arguments to instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity
    #method calculating total price
    def calculate_total_price(self):
        return self.price*self.quantity
item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
