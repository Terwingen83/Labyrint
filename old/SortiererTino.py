import random
from benchmark_list import benchmark, BenchmarkList

def sort_tino(shuffled_list):
    Length = len(shuffled_list)
    Testnumber = 0
    i1 = 0
    i2 = 0
    sorted_list = BenchmarkList(range(Length))
    while i1 < Length - 1:
        i1 = i1 + 1
        while i2 < Length - 1:
            i2 = i2 + 1
            if shuffled_list[i2] > Testnumber:
                Testnumber = shuffled_list[i2]
                shuffled_list[i2] = 0

        sorted_list[Length-1-i2] = Testnumber
        Testnumber = 0

    shuffled_list.write_counter += sorted_list.write_counter
    shuffled_list.write_counter += sorted_list.write_counter

benchmark(sort_tino)
# sort_func <function sort_daniel at 0x000001BB4E0D0280> has 13772 reads and 4628 writes