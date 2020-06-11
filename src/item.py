class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickUp(self):
        print(f"{self.name} was picked up")
