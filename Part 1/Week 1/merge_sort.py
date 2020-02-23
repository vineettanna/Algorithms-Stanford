def split(a):
    mid = len(a)//2
    p = a[:mid]
    q = a[mid:]
    return p,q


def merge(a,b):
    n = len(a)+len(b)
    merged = [None for i in range(n)]
    i,j = 0,0
    flag = 0
    for k in range(n):
        if flag == 0:
            if a[i] < b[j]:
                merged[k] = a[i]
                i+=1
                if i == len(a):
                    flag = 1
            else:
                merged[k] = b[j]
                j+=1
                if j == len(b):
                    flag = 2
        elif flag == 1:
            merged[k] = b[j]
            j+=1
        else:
            merged[k] = a[i]
            i+=1
    return merged


def mergeSort(a):
    if len(a) == 1:
        return a
    p,q = split(a)
    return merge(mergeSort(p),mergeSort(q))

print (mergeSort([5,4,3,2,1]))