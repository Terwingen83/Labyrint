import random
from enum import Enum



class GuessingGameResult(Enum):
    HIGHER = 1
    FOUND = 0
    LOWER = -1


class GuessingGame:
    def __init__(self, start=0, end=100):
        self._number = random.randint(start, end)

    def guess(self, number):
        if self._number > number:
            return GuessingGameResult.HIGHER
        elif self._number < number:
            return GuessingGameResult.LOWER
        return GuessingGameResult.FOUND



start = 0
end = 100
game = GuessingGame(start=start, end=end)







def benchmark(func):
    start = 0
    end = 100
    loops = 1000
    steps = 0
    min_steps = 99999999
    max_steps = 0
    random.seed(0)

    for _ in range(loops):
        game = GuessingGame(start=start, end=end)
        steps_in_loop = func(game, start, end)
        max_steps = max(max_steps, steps_in_loop)
        min_steps = min(min_steps, steps_in_loop)
        steps += steps_in_loop
    print(f"steps: {steps / loops:.2f}, max_steps: {max_steps}, min_steps: {min_steps}")








def daniels_func(game, start, end):
    steps = 0
    min_value = start
    max_value = end

    while True:
        steps += 1
        random_number = random.randint(min_value, max_value)

        if game.guess(random_number) == GuessingGameResult.LOWER:
            max_value = random_number - 1
        elif game.guess(random_number) == GuessingGameResult.HIGHER:
            min_value = random_number + 1
        else:
            print(f"FOUND {random_number}")
            break
    return steps



benchmark(daniels_func)