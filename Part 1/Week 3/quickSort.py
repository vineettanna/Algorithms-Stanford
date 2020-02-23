def partition(A):
    p = A[0]
    i = 1
    for j in range(1,len(A)):
        if A[j] < p:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    A[0] = A[i-1]
    A[i-1] = p
    return i-1

def quickSort(A):
    new_A = A.copy()
    n = len(new_A)
    if n < 2:
        return new_A
    p_idx = partition(new_A)
    left_sort = quickSort(new_A[:p_idx])
    right_sort = quickSort(new_A[(p_idx+1):])
    return left_sort + [new_A[p_idx]] + right_sort
arr = [3,8,2,5,1,4,7,6]
print(quickSort(arr))