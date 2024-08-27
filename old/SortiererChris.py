import random



def sort_chris(shuffled_list):
    x = 0
    y = x + 1
    min_y = y
    y = x + 1
    while True:
        if shuffled_list[x] > shuffled_list[y]:
            if shuffled_list[y] > shuffled_list[min_y]:
                min_y = y

            y += 1
        elif shuffled_list[x] < shuffled_list[y]:
            y += 1
        if y > len(shuffled_list) - 1:
            x += 1
            y = x + 1

            temp = shuffled_list[min_y]
            shuffled_list[min_y] = shuffled_list[x]
            shuffled_list[x] = temp

        if x == len(shuffled_list) - 1:
            break
            print(shuffled_list)

from benchmark_list import benchmark

benchmark(sort_chris)
# sort_func <function sort_chris at 0x000001C27B9CE3A0> has 18000 reads and 4388 writes