class Entity:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position

    def move(self):
        pass


class Wall(Entity):
    def __init__(self, position):
        super().__init__("█", position)

# TODO:
class Diamond(Entity):
    def __init__(self, position):
        super().__init__('✵')
