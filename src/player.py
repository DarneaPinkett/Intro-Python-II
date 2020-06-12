# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def move(self, direction):
        newRoom = getattr(self.current_room, f"{direction}_to")
        if newRoom == None:
            print("Try another direction")
        elif newRoom is not None:
            self.current_room = newRoom
            print("You are now in", self.current_room.name)
            print(self.current_room.description)

    def __str__(self):
        return f"Player Name: {self.name} \nPlayers {self.current_room}"

    def viewItems(self):
        print('Inventory contains: ')
        for item in self.items:
            print(item.name)

    def getItem(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                self.current_room.items.remove(i)
                print('Item added')
            else:
                print('No items here')

    def putDown(self, item):
        for i in self.items:
            if i.name == item:
                self.current_room.items.append(i)
                self.items.remove(i)
                print('Item removed')
            else:
                print('Cannot find item')