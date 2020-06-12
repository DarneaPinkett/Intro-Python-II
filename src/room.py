# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room(Item):
    def __init__(self, name, description, item = []):
        super().__init__(item, description)
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def pickUpItem(self, item):
        self.item.append(item)

    def dropItem(self, item):
        self.item.remove(item)


    def __str__(self):
        return f' {self.name}, {self.description}'