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


from models.position import Position
from models.map import Map
from models.entity import Entity, Wall, Diamond
from utils.fill_map import fill_map, PART_SIZE




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