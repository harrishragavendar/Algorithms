def insertion_sort(arr):
    for i in range(1, len(arr)):
        v = arr[i]
        j = i-1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j = j-1
        arr[j + 1] = v
        
n=int(input("Enter the number of elements : "))
arr=[]
for i in range(n):
    n=int(input("Enter element : "))
    arr.append(n)
print("Unsorted Array : ",arr)
insertion_sort(arr)
print("Sorted Array : ",arr)