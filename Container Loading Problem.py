class Container:
    def __init__(self,id,w):
        self.id=id
        self.weight=w
def ContainerLoading(c,capacity,n,x):
    c.sort(key=lambda x: x.weight)
    for i in range(n):
        x.append(0)
    i=0
    while(i<n and c[i].weight<capacity):
        x[c[i].id]=1
        capacity=capacity-c[i].weight
        i=i+1
n=int(input("Enter the number of items: "))
objects = []
for i in range(n):
    id=i
    w=int(input("Enter the weight: "))
    objects.append(Container(id,w))
capacity=int(input("Enter the container capacity: "))
x=[]
import copy
backup = copy.deepcopy(objects)
ContainerLoading(objects,capacity,n,x)
print("Solution Vector: ",x)
print("Weights Loaded: ",end=" ")
for i in range(n):
    if(x[i]==1):
        print(backup[i].weight,end=',')