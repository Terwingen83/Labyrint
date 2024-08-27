from collections import namedtuple

Point = namedtuple("Point", "x y")

SPIELFELD_GROESSE_X = 20
SPIELFELD_GROESSE_Y = 60


def standard_spielfeld(groesse_x, groesse_y):
    spielfeld = dict()
    for x in range(0, groesse_x):
        for y in range(0, groesse_y):
            spielfeld[x, y] = '.'

    return spielfeld


def umrechnung_intern_zu_raster(pos):
    raster_position = pos.x + pos.y * SPIELFELD_GROESSE_X + pos.y

    return raster_position


def ausgabe_spielfeld_wiederholung(spielfeld, ball_pos):
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
    raster_als_liste[raster_position] = "O"
    # print(raster_als_liste)
    raster = ''.join(raster_als_liste)
   # print(f'Ball Position: {ball_pos}, Raster Position: {raster_position}')
    print(raster)
    '''

def eingabe(ball_pos):
    eingabe = input("Drücke bitte: W für nach oben, A für nach links, D für nach Rechts und S für nach unten\n").upper()
    if eingabe == "W":
        ball_pos = Point(x=ball_pos.x, y=ball_pos.y - 1)
    elif eingabe == "A":
        ball_pos = Point(x=ball_pos.x - 1, y=ball_pos.y)
    elif eingabe == "S":
        ball_pos = Point(x=ball_pos.x, y=ball_pos.y + 1)
    elif eingabe == "D":
        ball_pos = Point(x=ball_pos.x + 1, y=ball_pos.y)

    else:
        print("Drücke bitte die richtigen Tasten")

    return ball_pos



ball_pos = Point(x=1, y=1)

spielfeld = standard_spielfeld(SPIELFELD_GROESSE_X, SPIELFELD_GROESSE_Y)
ausgabe_spielfeld_wiederholung(spielfeld, ball_pos)


while True:
    ball_pos = eingabe(ball_pos)

    x = ball_pos.x
    x = max(x, 0)
    x = min(x, SPIELFELD_GROESSE_X - 1)

    y = ball_pos.y
    y = max(y, 0)
    y = min(y, SPIELFELD_GROESSE_Y - 1)

    ball_pos = Point(x=x, y=y)


    ausgabe_spielfeld_wiederholung(spielfeld, ball_pos)

#def raster_labyrinth(raster_original)