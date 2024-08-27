from copy import copy
from math import sqrt
import random



"""
Mögliche Klassen:

Position
- x: int
- y: int
- add(...)
- sub(...)
- length(...)

Umgebungsobjekt
- symbol: str
- position: Position
- move(...)

Spieler(Umgebungsobjekt)
- ??? move(...)
 
Spielfeld
- list[Umgebungsobjekt]
- max_size: Position
- output(...)

"""

class Position:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def length(self):
        z = sqrt(self.x * self.x + self.y * self.y)
        return z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"<Position({self.x}, {self.y})>"

    def __hash__(self):
        return hash((self.x, self.y))


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



def pathfinding(map, start_pos, end_pos):
    north = Position(0, -1)
    south = Position(0, +1)
    west = Position(-1, 0)
    east = Position(+1, 0)
    directions = [north, east, south, west]

    known_fields = {}

    path = []
    player_pos = start_pos

    if start_pos == end_pos:
        return start_pos

    while True:
        if player_pos in path:
            path = path[:path.index(player_pos) + 1]
        else:
            path.append(player_pos)

        if player_pos == end_pos:
            break

        if player_pos in known_fields:
            known_fields[player_pos] += 1
        else:
            known_fields[player_pos] = 1

        shortest_distance = 99999999999

        # Für alle Nachbarfelder
        for dir in directions:
            new_pos = player_pos + dir

            # Wenn das Nachbarfeld belegt ist, ignorieren wir es. Zur Wegfindung interessieren uns nur leere Felder
            # die Start Position ist immer belegt, unsere Spielfigur steht ja immer noch dort - trotzdem können wir da lang gehen
            if not map.occupation(new_pos) or new_pos == start_pos:
                # Entfernung vom Nachbarfeld zum Ziel + wenn wir schon mal drauf waren, dann sollten wir besser versuchen
                # woanders lang zu laufen, weshalb wir etwas 'Entfernung' hinzu addieren
                distance = (end_pos - new_pos).length() + known_fields.get(new_pos, 0)

                if distance < shortest_distance:
                    shortest_distance = distance
                    shortest_distance_pos = new_pos
        if known_fields[start_pos] > 5: # in case we can't reach the target
            return None

        player_pos = shortest_distance_pos

    return path[1]




def fill_map(map, start_pos, end_pos):
    parts = [
        ###

        ###
        [Position(0, 0), Position(1, 0), Position(2, 0), Position(0, 2), Position(1, 2), Position(2, 2)],

        # #
        # #
        # #
        [Position(0, 0), Position(0, 1), Position(0, 2), Position(2, 0), Position(2, 1), Position(2, 2)],

        # #

        # #
        [Position(0, 0), Position(0, 2), Position(2, 0), Position(2, 2)],

        # #
        #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1)],

        # #
          #
        # #
        [Position(0, 0), Position(0, 2), Position(2, 0), Position(2, 2), Position(2, 1)],

        ###

        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0)],

        # #

        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 2)],

        ###
        #
        ###
        [Position(0, 0),  Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0), Position(0, 1), Position(1, 2)],

        ###
          #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 2), Position(2, 1)],

        # #
        # #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(2, 1), Position(1, 2)],

        ###
        # #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 0), Position(2, 1)],

        ###
          #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(1, 0), Position(1, 2)],

        ###
        #
        # #
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 0)],

        # #
          #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(2, 1), Position(1, 2)],

        # #
        #
        ###
        [Position(0, 0), Position(2, 0), Position(0, 2), Position(2, 2), Position(0, 1), Position(1, 2)]
    ]

    # TODO: Items zum einsammeln hinzufügen
    list_pathfinding_positions = []
    for x in range(1, map.maxsize.x - 1, PART_SIZE ):
        for y in range(1, map.maxsize.y - 1, PART_SIZE ):
            room_pos = Position(x, y)
            list_pathfinding_positions.append(room_pos)

    random.shuffle(list_pathfinding_positions)
    list_pathfinding_positions2 = copy(list_pathfinding_positions)

    for room_pos in list_pathfinding_positions2:
        random.shuffle(parts)

        for wall_part in parts:
            for wall_pos in wall_part:
                position = wall_pos + room_pos
                map.add_entity(Wall(position))

            level1.map_output()

            found_path = True
            for saved_room_position in list_pathfinding_positions:
                found_path = found_path and bool(pathfinding(map, start_pos, saved_room_position + Position(1, 1)))

            found_path_end = pathfinding(map, start_pos, end_pos)
            if found_path == False or found_path_end is None:
                for wall_position in wall_part:
                    position = wall_position + room_pos
                    wall = map.occupation(position)

                    if wall is not None:
                        map.remove_entity(wall)
            else:
                break




def player_input(player_position) -> Position:
    eingabe = input("Drücke bitte: W für nach oben, A für nach links, D für nach Rechts und S für nach unten\n").upper()
    if eingabe == "W":
        new_player_position = player_position + Position(x=0, y=-1)
    elif eingabe == "A":
        new_player_position = player_position + Position(x=-1, y=0)
    elif eingabe == "S":
        new_player_position = player_position + Position(x=0, y=1)
    elif eingabe == "D":
        new_player_position = player_position + Position(x=1, y=0)

    else:
        print("Drücke bitte die richtigen Tasten")
        new_player_position = player_position
    return new_player_position


PART_SIZE = 3
if __name__ == '__main__':
    walls = 2
    level1 = Map(maxsize=Position(walls + 10*PART_SIZE, walls + 4*PART_SIZE))

    start_pos = Position(2, 2)
    player = Entity(symbol='♡', position=start_pos)
    level1.add_entity(entity=player)

    end_pos = Position(level1.maxsize.x - 3, level1.maxsize.y - 3)

    fill_map(level1, start_pos, end_pos)

    level1.map_output()

    while True:
        if player.position == end_pos:  # Wir haben das Ziel erreicht
            print("Du hast das Ziel erreicht")
            break

        # new_pos = pathfinding(level1, player.position, end_pos)
        # if new_pos is None:
        #     break
        new_pos = player_input(player.position)
        # is something on this new position?
        if not level1.occupation(new_pos):
            # the position isn't occupied
            player.position = new_pos
            level1.map_output()
            print()







    


"""     


Point = namedtuple("Point", "x y")

SPIELFELD_GROESSE_X = 20
SPIELFELD_GROESSE_Y = 60



def standard_spielfeld(groesse_x, groesse_y):
    spielfeld = dict()

    for x in range(0, groesse_x):
        for y in range(0, groesse_y):
            ist_mauer = randint(1, 100) < 30
            if ist_mauer == True:
                spielfeld[x, y] = "#"

            else:
                spielfeld[x, y] = '.'

    for x in range(0, groesse_x):
        spielfeld[x, 0] = "#"
        spielfeld[x, groesse_y - 1] = "#"

    for y in range(0, groesse_y):
        spielfeld[0, y] = "#"
        spielfeld[groesse_x - 1, y] = "#"

    return spielfeld





def umrechnung_intern_zu_raster(pos):
    raster_position = pos.x + pos.y * SPIELFELD_GROESSE_X + pos.y

    return raster_position


def ausgabe_spielfeld_wiederholung(spielfeld, ball_pos):
    spielfeld = copy(spielfeld)

    spielfeld[ball_pos] = "O"

    for x in range(0, SPIELFELD_GROESSE_X):
        zeile = ''
        for y in range(0, SPIELFELD_GROESSE_Y):
            zeile += spielfeld[x, y]
        print(zeile)



    '''
    raster_original = "" # ("." * SPIELFELD_GROESSE_X + "\n") * SPIELFELD_GROESSE_Y

    zeile_oben_unten = ""
    for var in range(SPIELFELD_GROESSE_X):
        zeile_oben_unten += "#"
    zeile_oben_unten += "\n"

    zeile = "" + "#"
    for var in range(SPIELFELD_GROESSE_X - 2):
        zeile += "."
    zeile += "#\n"



    for y in range(SPIELFELD_GROESSE_Y):
        if y == 0 or y == 19:
            raster_original += zeile_oben_unten
        if y in range(1, 19):
            raster_original += zeile



    raster_position = umrechnung_intern_zu_raster(ball_pos)
    raster_als_liste = list(raster_original)
    # print(raster_als_liste)

    # print(raster_als_liste)
    raster = ''.join(raster_als_liste)
   # print(f'Ball Position: {ball_pos}, Raster Position: {raster_position}')
    print(raster)
    '''

def eingabe(ball_pos):
    eingabe = input("Drücke bitte: W für nach oben, A für nach links, D für nach Rechts und S für nach unten\n").upper()
    if eingabe == "W":
        ball_pos = Point(x=ball_pos.x - 1, y=ball_pos.y)
    elif eingabe == "A":
        ball_pos = Point(x=ball_pos.x, y=ball_pos.y - 1)
    elif eingabe == "S":
        ball_pos = Point(x=ball_pos.x + 1, y=ball_pos.y)
    elif eingabe == "D":
        ball_pos = Point(x=ball_pos.x, y=ball_pos.y + 1)

    else:
        print("Drücke bitte die richtigen Tasten")

    return ball_pos



ball_pos = Point(x=1, y=1)

spielfeld = standard_spielfeld(SPIELFELD_GROESSE_X, SPIELFELD_GROESSE_Y)
ausgabe_spielfeld_wiederholung(spielfeld, ball_pos)


while True:
    neue_ball_pos = eingabe(ball_pos)

    x = neue_ball_pos.x
    x = max(x, 0)
    x = min(x, SPIELFELD_GROESSE_X - 1)

    y = neue_ball_pos.y
    y = max(y, 0)
    y = min(y, SPIELFELD_GROESSE_Y - 1)
    neue_ball_pos = Point(x=x, y=y)

    if spielfeld[x, y] == ".":
        ball_pos = neue_ball_pos

    ausgabe_spielfeld_wiederholung(spielfeld, ball_pos)
#"""

#          0  1  2   3   4
numbers = [4, 2, 15, 63, 36]
highest_number_index = 0
highest_number = numbers[0]

for index, x in enumerate(numbers):
    if x > highest_number:
        highest_number = x
        highest_number_index = index

print(highest_number)
print (highest_number_index)