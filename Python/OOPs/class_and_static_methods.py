import csv
class Item:
    pay_rate = 0.8 # discount rate for all items
    all=[]
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price{price} is not greater than or equal to 0" # to check what is happening according to your expectation or not
        assert quantity >= 0, f"Quantity{quantity} is not greater than  or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item( name=item.get("name"), price=float(item.get("price")), quantity=int(item.get("quantity")) )
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zeros
        # For i.e:5.0,10.0
        if isinstance(num, float):
            return num.is_integer()
            #count out the floats that are point zero
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item: {self.__class__.__name__}, price: {self.price}, quantity: {self.quantity}"

# rest code same only testing override for laptop
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.0))
