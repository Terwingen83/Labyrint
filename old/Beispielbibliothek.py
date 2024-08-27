import random

#Fibonaccireihe
"""
Operatoren für Bedingungen
var1 != var2
var1 == var2
var1 < var2
var1 <= var2
var1 > var2
var1 >= var2
"""

def fibonacci_sequence():
    first_value = 1
    second_value = 1
    final_value = 0

    while final_value <= 10000:
        final_value = first_value + second_value
        print(final_value)
        first_value = second_value
        second_value = final_value
        # if final_value >= 10000:
        #    break

# https://de.wikipedia.org/wiki/Division_mit_Rest#Modulo
print(6 / 4) # genaues Kommaergebniss
print(6 % 4) # Restmengenausgabe (Modulo)
print(6 // 4) # Ganzzahlausgabe


#Gerade/Ungerade Berechnung
zahl = 10

if zahl % 2 == 1:
    print("Zahl ist ungerade")
else:
    print("Zahl ist gerade")


# Passwortgenerator
print("Passwordgenerator" + "1" + "1")
random_password = ""
password_length = 10


for x in range(password_length):
    random_value = random.choice(["W", "1", "D", "2", "6", "H", "L"])
    random_password = (random_password) + (random_value)

print(random_password)


# Klassen und Objekte

class Car:
    def __init__(self, color):
        self.color = color
        self.speed = 0
        self.max_speed = 120
        self.type = 'undefined'

    def accelerate(self):
        self.speed = min(self.max_speed, self.speed + 1)


red_car = Car(color='ROT')
print(red_car.speed) # => 0
red_car.accelerate()
print(red_car.speed) # => 1

white_car = Car('WEIß')
print(white_car.color) # => WEIß



class RacingCar(Car):
    def __init__(self, color):
        super().__init__(color)

        self.max_speed = 300

    def accelerate(self):
        self.speed = min(self.max_speed, self.speed + 5)

red_racingcar = RacingCar('ROT')
red_racingcar.accelerate()
print(red_racingcar.speed)  # => 5

for y in range(1, map.maxsize.y - 1):
    wall = Entity('#', Position(0, y))
    map.add_entity(wall)
    wall = Entity('#', Position(map.maxsize.x - 1, y))
    map.add_entity(wall)

for y in range(map.maxsize.y):
    if not map.occupation(Position(0, y)):
        wall = Entity('#', Position(0, y))
        map.add_entity(wall)

    if not map.occupation(Position(map.maxsize.x - 1, y)):
        wall = Entity('#', Position(map.maxsize.x - 1, y))
        map.add_entity(wall)

################################


# len(numbers)