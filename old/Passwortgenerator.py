import random
import string


passwordlist = list()


for x in range(50):
    randomnumber = random.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase + """!"§$%&/()=?`ß´+#'* """)


    passwordlist.insert(0, randomnumber)

print(passwordlist)


#passwordlist = list()

#print(string.digits)
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)

#randomletter_list = 'ABCDEF' # ["A", "B", "C", "D", "E", "F"]


#for x in range(10):
#    randomletter = random.choice(randomletter_list)
#    passwordlist.insert(0, randomletter)

#print(passwordlist)




