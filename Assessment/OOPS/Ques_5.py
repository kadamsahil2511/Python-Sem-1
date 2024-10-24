#Ques_5
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1)
cart.add_item("Banana", 2)
print(cart.total_price())
cart.remove_item("Apple")
print(cart.total_price())