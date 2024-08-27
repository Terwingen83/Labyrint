# Erstmal eine Zufallszahl generiert
# User gibt eine Zahl ein
# Computer gibt aus ob die Zahl gefunden wurde, oder ob die eingegebene Zahl größer oder kleiner ist (wiederholt, bis die Zahl gefunden wurde)

import randint

random_number = randint(0, 50)

while True:
    entered_number = int(input("Gib bitte eine beliebige Zahl von 1 bis 50 ein"))



    if random_number == entered_number:
        print("Du hast die Zahl gefunden")
        break
    elif random_number < entered_number:
        print("Deine Zahl ist höher als die gesuchte Zahl")

    else:
        print("Deine Zahl ist niedriger als die gesuchte Zahl")
# break sprimgt hier her