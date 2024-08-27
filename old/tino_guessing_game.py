import random
from enum import Enum

START = 0
END = 100


class GuessingGameResult(Enum):
    HIGHER = 1
    FOUND = 0
    LOWER = -1


class GuessingGame:
    def __init__(self, start=0, end=100):
        random.seed(0)
        self._number = random.randint(start, end)

    def guess(self, number):
        if self._number > number:
            return GuessingGameResult.HIGHER
        elif self._number < number:
            return GuessingGameResult.LOWER
        return GuessingGameResult.FOUND


game = GuessingGame(start=START, end=END)

Resume = True
middle = END - START / 2
halving = middle
while Resume:
    halving = halving / 2
    higher_or_lower = game.guess(middle)
    if higher_or_lower == GuessingGameResult.FOUND:
        print("Richtige Zahl gefunden: "+middle)
        Resume = False
    if higher_or_lower == "HIGHER":
        middle = halving + middle
    if higher_or_lower == "LOWER":
        middle = halving - middle
    print("Programm beendet")