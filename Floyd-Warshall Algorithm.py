def Floyd(W):
    n=len(W)
    d=W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
    
n=int(input("Enter the number of vertices : "))
W=[]
print("Enter 99999 for infinity")
for i in range(n):
    W.append([])
    for j in range(n):
        print("Enter the weight of edge between vertex ",i+1," and ",j+1," : ")
        w=int(input())
        W[i].append(w)
print("Adjacency Matrix")
for i in range(n):
    for j in range(n):
        print(W[i][j],end= "\t")
    print()

W=Floyd(W)

print("D(",n,")")
for i in range(n):
    for j in range(n):
        print(W[i][j],end= "\t")
    print()