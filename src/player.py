# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, room, item = []):
        super().__init__(item)
        self.name = name
        self.room = room

    def pickUpItem(self,item):
        self.item.append(item)

    def dropItem(self, item):
        self.item.remove(item)


    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.room}"