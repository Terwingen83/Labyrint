from collections import namedtuple

Point = namedtuple("Point", "x y")




def umrechnung_intern_zu_raster(pos):
    raster_position = pos.x + pos.y * 5 + pos.y
    return raster_position


def ausgabe_spielfeld_wiederholung(ball_pos):
    raster_original = """XXXXX
XXXXX
XXXXX
XXXXX
XXXXX"""
    raster_position = umrechnung_intern_zu_raster(ball_pos)
    raster_als_liste = list(raster_original)
    # print(raster_als_liste)
    raster_als_liste[raster_position] = "O"
    # print(raster_als_liste)
    raster = ''.join(raster_als_liste)
   # print(f'Ball Position: {ball_pos}, Raster Position: {raster_position}')
    print(raster)


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



ball_pos = Point(x=2, y=2)

ausgabe_spielfeld_wiederholung(ball_pos)



while True:
    ball_pos = eingabe(ball_pos)

    x = ball_pos.x
    x = max(x, 0)
    x = min(x, 4)

    y = ball_pos.y
    y = max(y, 0)
    y = min(y, 4)

    ball_pos = Point(x=x, y=y)


    ausgabe_spielfeld_wiederholung(ball_pos)



# ohne funktion

#pos = Point(x=2, y=3)

##raster[pos.x + pos.y * 5 + pos.y]
#raster_position = pos.x + pos.y * 5 + pos.y

#raster_als_liste = list(raster_original)
#print(raster_als_liste)

#raster_als_liste[raster_position] = "O"
#print(raster_als_liste)

#raster_grundposition = ''.join(raster_als_liste)
#print(raster_grundposition)







# grundversion

# eingabe = input("Drücke bitte: W für nach oben, A für nach links, D für nach Rechts und S für nach unten")
# if (eingabe == "W") or (eingabe == "w"):
#     pos = Point(x=pos.x, y=pos.y - 1)
# elif (eingabe == "A") or (eingabe == "a"):
#     pos = Point(x=pos.x - 1, y=pos.y)
# elif (eingabe == "S") or (eingabe == "s"):
#     pos = Point(x=pos.x, y=pos.y + 1)
# elif (eingabe == "D") or (eingabe == "d"):
#     pos = Point(x=pos.x + 1, y=pos.y)
#
# else:
#     print("Drücke bitte die richtigen Tasten")


# verbesserte version 1

# eingabe = input("Drücke bitte: W für nach oben, A für nach links, D für nach Rechts und S für nach unten")
# if eingabe in ['W', 'w']:
#     pos = Point(x=pos.x, y=pos.y - 1)
# elif eingabe in ['A', 'a']:
#     pos = Point(x=pos.x - 1, y=pos.y)
# elif eingabe in ['S', 's']:
#     pos = Point(x=pos.x, y=pos.y + 1)
# elif eingabe in ['D', 'd']:
#     pos = Point(x=pos.x + 1, y=pos.y)
#
# else:
#     print("Drücke bitte die richtigen Tasten")

# verbesserte version 2





