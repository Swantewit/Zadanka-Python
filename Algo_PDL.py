from timeit import default_timer as timer

elapsed_time = timer()
print('Time start is: ' + str(elapsed_time))

import random
longList = list(random.randint(0,100000) for i in range(50000))

pivot = longList[25000]

print(str(pivot))

def QuickSort(longList):
    smallList = list()
    bigList = list()
    pivotList = list()
    for j in longList:
        if j < pivot:
            smallList.append(j)
        if j == pivot:
            pivotList.append(j)
        if j > pivot:
            bigList.append(j)
    print(smallList)
    print(pivotList)
    print(bigList)
    
    
QuickSort(longList)


print('Time stop is: ' + str(elapsed_time))
