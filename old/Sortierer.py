import random

from benchmark_list import benchmark

def sort_daniel(shuffled_list):


    i = 0
    number1 = shuffled_list[i]
    number2 = shuffled_list[i + 1]

    is_sorted = True
    while True:

        number1 = shuffled_list[i]
        number2 = shuffled_list[i + 1]

        if number1 > number2:
            shuffled_list[i + 1] = number1
            shuffled_list[i] = number2
            is_sorted = False

        # print(shuffled_list, i, number1, number2)
        i += 1
        if i == 9:
            i = 0

            if is_sorted == True:
                break
            is_sorted = True




benchmark(sort_daniel)
# sort_func <function sort_daniel at 0x000001E8D3A80280> has 13682 reads and 4612 writes