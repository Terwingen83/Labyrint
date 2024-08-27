import random

class BenchmarkList(list):
    def __init__(self, *args, **kwargs):
        self.read_counter = 0
        self.write_counter = 0
        super().__init__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
       self.read_counter += 1
       return super().__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
       self.write_counter += 1
       return super().__setitem__(*args, **kwargs)


def benchmark(sort_func):
    reads = 0
    writes = 0
    for i in range(100):
        shuffled_list = BenchmarkList(range(100))
        random.shuffle(shuffled_list)
        shuffled_list.read_counter = 0
        shuffled_list.write_counter = 0
        sort_func(shuffled_list)
        reads += shuffled_list.read_counter
        writes += shuffled_list.write_counter
    print(f'sort_func {sort_func} has {reads} reads and {writes} writes')


if __name__ == '__main__':
    def quicksort(shuffled_list):
        shuffled_list.sort()

    random.seed(0)
    benchmark(quicksort)
