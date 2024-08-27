
# index      0  1  2  3
# numbers = [5, 2, 1, 9]

# index, number
#   0      8
#   1      7
#   2      6
#   3      9

def max_number(numbers):
    highest_number = numbers[0]
    for number in numbers:
        if number > highest_number:
            highest_number = number

    return highest_number



def max_number_index(numbers):
    highest_number = numbers[0]
    highest_number_index = 0
    for index, number in enumerate(numbers):
        if number > highest_number:
            highest_number = number
            highest_number_index = index

    return highest_number_index



number = 6
if number > 0:
    print('Positive Zahl!')
elif number < 0:
    print('Negative Zahl!')
else:
    print("Zahl ist 0!")