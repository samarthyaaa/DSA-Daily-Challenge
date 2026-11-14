# simple class 
class ItemBasic:
    pass
item1=ItemBasic()
item1.name="Phone"
item1.price=100
item1.quantity=5
print(type(item1))
print(type(item1.name))
# adding function inside the class
class ItemWithMethod:
    def calculate_total_price(self,x,y):
        return x*y
item1=ItemWithMethod()
item1.name="Phone"
item1.price=100
item1.quantity=5
print(item1.calculate_total_price(item1.price,item1.quantity))
# using __init__ so it run automatic when object create
class Item:

    def __init__(self,name:str,price:float,quantity=0):
        # it checks the price and quantity is not minus value
        assert price>=0,f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero!"
        self.name=name
        self.price=price
        self.quantity=quantity
    # using self directly no need to pass x and y again
    def calculate_total_price(self):
        return self.price*self.quantity
item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
# whole rest code is same just adding extra attribute to item2
item2.has_numpad=False
