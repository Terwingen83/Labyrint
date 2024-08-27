
def create_number_sequence():
    for x in range(20):
        x += 1
        even2 = is_even(x)
        output(even2)


# Umrechnung

def is_even(number2):
    if number2 % 2 == 0:
        even1 = True
    else:
        even1 = False
    return even1


def output(even3):
    if even3 == True:
        print("Zahl ist gerade")
    else:
        print("Zahl ist ungerade")



create_number_sequence()

def foobar():

    for number1 in range(20):

        even2 = is_even(number1)
        #abhand des outputs ausgibt ob gerade oder ungerade
        output(even2)



for number in range(20):
    if number % 2:
        print(number, "ist ungerade" )
    else:
        print(number, "ist gerade")

#foobar()