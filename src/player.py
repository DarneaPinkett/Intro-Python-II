# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

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