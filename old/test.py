# from collections import namedtuple
# from time import sleep
#
# Point = namedtuple("Point", "x y")
#
# a = Point(x=1, y=1)
# print(f'Punkt a: {a}, ID: {id(a)}')
#
# b = Point(x=1, y=2)
# print(f'Punkt b: {b}, ID: {id(b)}')
#
# a = b
# print(f'Punkt a: {a}, ID: {id(a)}')
# print(f'Punkt b: {b}, ID: {id(b)}')
#
#
# for i in range(4):
#     print('\a')
#     sleep(1)



#
#
# ''.startswith()
#
# c_directory = ['AMD', 'Benutzer', 'cygwin64', 'Program Files', 'Programme', 'Windows']
#
# print(c_directory[0])  # => AMD
# print(c_directory[1])  # => Benutzer
# print(c_directory[2])  # => cygwin64
# print(c_directory[3])  # => Program Files
#
# # c_directory[2] = 'IrgendwasAnderes'
#
# # index = c_directory.find('cygwin64')
#
# index = c_directory.pop('cygwin64')
#
# print(c_directory[0])  # => AMD
# print(c_directory[1])  # => Benutzer
# print(c_directory[2])  # => Program Files
# print(c_directory[3])  # => Programme
#
#
# c_directory.insert(index, 'IrgendwasAnderes')
#
# print(c_directory[0])  # => AMD
# print(c_directory[1])  # => Benutzer
# print(c_directory[2])  # => IrgendwasAnderes
# print(c_directory[3])  # => Program Files
#
#
# a = {
#     'key': 'value',
#     'if': 'wenn',
#     'hello': 'Hallo',
# }
#
# a = {
#     0: 'AMD',
#     1: 'Benutzer',
#     2: 'cygwin64',
#     3: 'Program Files'
# }
#
# del a[2]

#print( 'Na' * 10 + 'Batman')

#raster_original = X *

x = 2
y = 9
d = 0
for var in range(y): # [0, 1, 2, 3, 4, 5, 6]
    d += x
print(d)