def QuickSort(A,l,r):
    if l < r:
        s = HoarePartition(A,l,r)
        QuickSort(A,l,s-1)
        QuickSort(A,s+1,r)

def HoarePartition(A,l,r):
    p = A[l]
    i = l+1
    j = r
    while True:
        while i <= j and A[i] < p:
            i = i+1
        while i <= j and A[j] > p:
            j = j-1
        if (i < j):
            A[i] ,A[j] = A[j], A[i]
        else:
            break
    A[l] ,A[j] = A[j], A[l]
    return j

n = int(input("Enter the total number of elements : "))
Q = []
for i in range(n):
    e = int(input("Enter element : "))
    Q.append(e)
print("Before Sorting : ",Q)
QuickSort(Q,0,n-1)
print("After Sorting : ",Q)