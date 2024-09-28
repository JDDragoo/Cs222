class ShoppingCart:
    def __init__(self):
        self.item = []
    def AddItem(self, item):
        self.items.append(item)
    def RemoveItem(self, item):
        if item in self.items:
            self.item.remove(item)
    def TotalPrice(self):
        #result = 0
        #for item in self.items:
        #    result += item.price
        #return result
        return sum(item.price for item in self.items)
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price