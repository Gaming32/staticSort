def thatsOvens_staticSort(a):
    M = max(a) 
    size = len(a)
    for i in range(M + 1):
        a.append([])
    for i in range(size):
        a[a[0] + size].append(a[0])
        a.remove(a[0])
        size -= 1
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
