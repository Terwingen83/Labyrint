from src.models.entity import Entity, Wall
from src.models.position import Position


class Map:
    def __init__(self, maxsize):
        self.maxsize: Position = maxsize
        self.entities: list[Entity] = []

        for x in range(0, self.maxsize.x):
            wall = Wall(Position(x, 0))
            self.add_entity(wall)
            wall = Wall(Position(x, self.maxsize.y - 1))
            self.add_entity(wall)

        for y in range(1, self.maxsize.y - 1):
            wall = Wall(Position(0, y))
            self.add_entity(wall)
            wall = Wall(Position(self.maxsize.x - 1, y))
            self.add_entity(wall)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def add_entity(self, entity):
        self.entities.append(entity)

    def occupation(self, position):
        for entity in self.entities:
            if entity.position == position:
                return entity
        return None

    def map_output(self):
        for y in range(self.maxsize.y):
            for x in range(self.maxsize.x):
                entity = self.occupation(Position(x, y))

                if entity == None:
                    print(" ", end='')
                else:
                    print(entity.symbol, end='')
            print()
