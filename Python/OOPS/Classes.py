class Item:# creating a class
    pay_rate = 0.8#The pay rate after 20% discount #class attribute
    def __init__(self,name:str,price:float,quantity=0):# magic methods can use default method # constructor
        assert price >=0,  f"Price{price} is not greater than or equal to 0"# to check what is happening according to your expectation or not
        assert quantity >= 0, f"Quantity{quantity} is not greater than  or equal to 0"
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate
"""# instance attributes
item1 = Item("Phone",100,5) # created an instance #creating attributes for the instance item1 of
#print(item1.calculate_total_price(item1.price, item1.quantity)) # calling the fn and passing the args
item2 = Item("Laptop",1000,3)# if push str then it will repeat the str
print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
print(Item.__dict__)# All the attributes for class level __dict__
print(item1.__dict__)# All the attributes for instance level
print(item2.pay_rate)"""
item1 = Item("Phone",100,5)
item1.apply_discount()
print(item1.price)

item2= Item("Laptop",1000,3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

