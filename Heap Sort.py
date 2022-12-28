def HeapBottomUp(H): 
    n = len(H)-1
    for i in range(n//2,0,-1):
        k = i
        v = H[k]
        heap=False
        while(not heap and 2*k <= n):
            j = 2*k
            if(j<n):
                if(H[j] < H[j+1]):
                    j = j + 1
            if (v >= H[j]):
                heap=True
            else:
                H[k] = H[j]
                k=j
        H[k] = v
    return H

def HeapSort(H):
    s=[]
    n=len(H)
    for i in range(n-1):
        s.insert(0,H[1])
        H[1]=H[-1]
        H=H[:-1]
        H=HeapBottomUp(H)
    return s

n = int(input("Enter the total number of elements : "))
H = ['#']
for i in range(n):
    e = int(input("Enter element : "))
    H.append(e)
print("Before Sorting : ",H[1:])
H = HeapBottomUp(H)
print("Max Heap : ",H[1:])
H = HeapSort(H)
print("After Sorting : ",H)