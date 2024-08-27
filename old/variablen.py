from copy import copy



def add_one(var):
    var.append('1')


x = list()
print(x)
add_one(x)
print(x)