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
    return i-1,len(A) - 1

def quickSort(A, tot_comp,pivot_option):
    new_A = A.copy()
    n = len(new_A)
    if n < 2:
        return new_A,0
    if pivot_option == 2:
        temp = new_A[-1]
        new_A[-1] = new_A[0]
        new_A[0] = temp
    elif pivot_option == 3:
        if n%2 == 1:
            mid_idx = n//2
        else:
            mid_idx = (n//2) - 1
        first = new_A[0]
        mid = new_A[mid_idx]
        last = new_A[-1]
        if ((mid > first) and (mid < last)) or ((mid > last) and (mid < first)):
            new_A[0] = mid
            new_A[mid_idx] = first
        elif ((last > first) and (last < mid)) or ((last > mid) and (last < first)):
            new_A[0] = last
            new_A[-1] = first
    # print (A)
    # print (new_A)
    p_idx,comp = partition(new_A)
    left_sort,left_comp = quickSort(new_A[:p_idx],0,pivot_option)
    right_sort,right_comp = quickSort(new_A[(p_idx+1):],0,pivot_option)
    tot_comp = comp + left_comp + right_comp
    return left_sort + [new_A[p_idx]] + right_sort,tot_comp

def main(new_A,pivot_option):
    new_A,comp = quickSort(new_A,0,pivot_option)
    return comp

f = open("QuickSort_Assignment.txt",'r')
test_arr = [int(l) for l in f.readlines()]
