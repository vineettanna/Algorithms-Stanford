def split(a):
    mid = len(a)//2
    p = a[:mid]
    q = a[mid:]
    return p,q


def countSplit(a,b):
    n = len(a)+len(b)
    merged = [None for i in range(n)]
    i,j = 0,0
    flag = 0
    n_inv = 0
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
                n_inv += len(a) - i
                if j == len(b):
                    flag = 2
        elif flag == 1:
            merged[k] = b[j]
            j+=1
        else:
            merged[k] = a[i]
            i+=1
    return merged,n_inv


def mergeSort(a,n_inv):
    if len(a) == 1:
        return a,0
    p,q = split(a)
    inv_p,inv_q = 0,0
    sorted_p, inv_p = mergeSort(p,inv_p)
    sorted_q, inv_q = mergeSort(q,inv_q)
    merged, inv_split = countSplit(sorted_p,sorted_q)
    n_inv += inv_p + inv_q + inv_split
    return merged,n_inv

print (mergeSort([5,4,3,2,1],0))