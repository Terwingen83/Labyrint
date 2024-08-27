import random
import sys

value_start = int(input("Bitte geben Sie den kleinsten Wert ein ein:"))
value_end = int(input("Bitte geben Sie den größten Wert ein ein:"))

randomnumber = random.randrange(value_start, value_end)
if value_start > value_end:
    print("Eingabe ungültig, Programm beendet.")
    sys.exit()
else:

    tries = 0

    while True:
        eingabe = int(input("Bitte geben Sie eine Ratezahl ein:"))
        tries = tries + 1
        if eingabe == randomnumber:
            print(f"Die eingegebene Zahl ist richtig! Du hast {tries} Versuche gebraucht.", end='')
            print(f"Die eingegebene Zahl ist richtig! Du hast {tries} Versuche gebraucht.", end='')
            sys.exit()
        else:
            print("Die eingegebene Zahl ist falsch")

            if eingabe > randomnumber:
                print("Die Zahl ist kleiner.")
            else:
                print("Die Zahl ist größer.")
