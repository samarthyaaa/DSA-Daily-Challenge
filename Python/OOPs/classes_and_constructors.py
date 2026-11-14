class ItemBasic:
    pass
item1=ItemBasic()
item1.name="Phone"
item1.price=100
item1.quantity=5
print(type(item1)) # it checks what type is item1
print(type(item1.name))
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price{price} is not greater than or equal to 0" # to check what is happening according to your expectation or not
        assert quantity >= 0, f"Quantity{quantity} is not greater than  or equal to 0"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False # adding extra attribute only for laptop
print(item1.calculate_total_price())
print(item2.calculate_total_price())
