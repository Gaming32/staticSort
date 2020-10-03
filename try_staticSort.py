from random import randrange
from time import time
inputa = []
number_quantity = 1000
maximum_number = 1000
for i in range(number_quantity):
    inputa.append(randrange(0, int(maximum_number), 1))
def insertion_sort(InputList, n):
    for i in range(1, n):
        j = i-1
        nxt_element = InputList[i]
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
from itertools import chain
def thatsOvens_staticSort(a):
    M = max(a)
    size = len(a)
    constant = M/(size+4)
    counter = 0
    listcount = 0
    while listcount < size:
        if type(a[counter]) is list:
            counter += 1
        else:
            if int(a[counter]*constant) == counter:
                a[counter] = [a[counter]]
            else:
                if type(a[int(a[counter]*constant)]) is list:
                    a[int(a[counter]*constant)].append(a[counter])
                    a[counter] = []
                else:
                    a[int(a[counter]*constant)], a[counter] = [a[counter]], a[int(a[counter]*constant)]
            listcount += 1 
    for i in range(len(a)):
        lt = len(a[i])
        if lt > 1:
            insertion_sort(a[i], lt)
    return list(chain.from_iterable(a))
print(inputa)
startime = time()
thatsOvens_staticSort(inputa)
fin = str(time() - startime)
print(inputa)
print("thatsOven's staticSort, Elapsed time: " + fin + ' s (' + str(float(fin) * 1000) + ' ms)')
print('Quantity of numbers: ' + str(len(inputa)) + ' , Maximum number: ' + str(max(inputa)))
input()
