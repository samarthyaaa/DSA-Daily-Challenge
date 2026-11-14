import csv
with open("items.csv","w") as f:
    f.write('name,price,quantity\n"Phone",100,1\n"Laptop",1000,3\n"Cable",10,5\n"Mouse",50,5\n"Keyboard",75,5\n')
# class attribute and repr function
class Item:
    #this two variable is common for all object
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0,f"Price {price} is not greater than or equal to zero!"
        assert quantity>=0,f"Quantity {quantity} is not greater than or equal to zero!
        self.name=name
        self.price=price
        self.quantity=quantity
        #adding every new item into all list
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price*self.quantity
    # using self.pay_rate so we can change discount for single item also
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    # this show object name properly when printing list
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
# rest code same  checking dict and changing discount for laptop
print(Item.__dict__)
print(item1.__dict__)
item1.apply_discount()
print(item1.price)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)
# whole rest code is same just adding classmethod and staticmethod below
# classmethod take cls and read data from csv file
@classmethod
def instantiate_from_csv(cls):
    with open("items.csv","r") as f:
        reader=csv.DictReader(f)
        items=list(reader)
    for item in items:
        Item(
            name=item.get("name"),
            price=float(item.get("price")),
            quantity=int(item.get("quantity")),
        )
# staticmethod is like normal function inside class it dont use self or cls
@staticmethod
def is_integer(num):
    if isinstance(num,float):
        return num.is_integer()
    elif isinstance(num,int):
        return True
    else:
        return False
Item.instantiate_from_csv=instantiate_from_csv
Item.is_integer=is_integer
Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.0))
