import math
number = 10


square_number = int(math.sqrt(number))
is_prim = True

for x in range(2, number + 1):
    for y in range(2, number + 1):
        result = x * y
        if result == number:
            is_prim = False


if is_prim:
    print ("Ergebnis ist eine Primzahl")
else:
    print("Ergebnis ist keine Primzahl")

#--------------------------------------------------

square_number = int(math.sqrt(number))
is_prim = True

for x in range(2, square_number + 1):
    if number % x  == 0:
        is_prim = False

if is_prim:
    print ("Ergebnis ist eine Primzahl")
else:
    print("Ergebnis ist keine Primzahl")


#-----------------------------------------------

number = 81

primzahl = True

if number == 1:
    primzahl = False

for i in range(2, number):
    if number % i == 0:
        primzahl = False

if primzahl == True:
    print("Es ist eine Primzahl")
else:
    print("Es ist keine Primzahl")