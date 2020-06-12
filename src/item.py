class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickUp(self):
        return f'You picked up {self.name}'

    def putDown(self):
        return f'You put down {self.name}'
