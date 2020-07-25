import random
numberOfStreaks = 0
list1 = []
list0 = []


for experimentNumber in range(10000):
    for i in range(100):
        i = random.randint(0,1)
        if i == 1:
            list1.append(i)
        if i == 0:
            list1 = []
        if len(list1) == 6:
            numberOfStreaks += 1
        if i == 0:
            list0.append(i)
        if i == 1:
            list0 = []
        if len(list0) == 6:
            numberOfStreaks += 1
        

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
