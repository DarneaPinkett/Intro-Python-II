from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

flaslight = Item('Flashlight', 'use the light to guide you')
axe = Item('axe', 'Protect yourself')
key = Item('key', 'Keep this safe')
chest = Item('chest', 'Use the key')

player = Player(input("Create a name: "), room['outside'].showItems())
print(f'Time to begin you adventure, {player.name}')
print(player.current_room.description)

room['outside'].items.append(key)
room['foyer'].items.append(flaslight)
room['narrow'].items.append(axe)
room['treasure'].items.append(chest)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

choice = 1

while True:
    choice = input('Which way would you like to go? Choose n, e, s, or w. \nTo view your inventory press i, \nTo take item enter take \nand to quit q.')
    if choice == 'n':
        player.move(choice)

    elif choice == 's':
        player.move(choice)

    elif choice == 'e':
        player.move(choice)

    elif choice == 'w':
        player.move(choice)

    elif choice == 'i':
        player.viewItems()

    elif choice.startswith('Take'):
        item = choice.split(' ')[1]
        player.getItem(item)
        player.viewItems()
    
    elif choice.startswith('Drop'):
        item = choice.split(' ')[1]
        player.putDown(item)
        player.viewItems()

    elif choice == 'q':
        print(f'Game over')
        break
    else:
        print("You can't go there!")


