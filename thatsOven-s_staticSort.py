def thatsOvens_staticSort(a):
    M = max(a) 
    size = len(a)
    if M > (size - 1):
        for i in range(M - size + 1):
            a.append([])
    if M == size:
        a.insert(0, [])
    counter = 0
    listcount = 0
    while listcount < size:
        if type(a[counter]) is list:
            counter += 1
        else:
            if int(a[counter]) == counter:
                temp = a[counter]
                a[counter] = [temp]
            else:
                if type(a[a[counter]]) is list:
                    a[a[counter]].append(a[counter])
                    a[counter] = []
                else:
                    temp = int(a[a[counter]])
                    a[a[counter]] = [a[counter]]
                    a[counter] = temp
            listcount += 1
    size = len(a)
    counter = 0
    for i in range(size):
        l = len(a[counter])
        if l == 0:
            a.remove(a[counter])
            size -= 1
        elif l == 1:
            a[counter] = a[counter][0]
            counter += 1
        else:
            temp = a[counter].copy()
            a.remove(a[counter])
            for j in range(len(temp)):
                a.insert(counter, temp[j])
                counter += 1
