def Knapsack(W,Weights,Values,n):
    F = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                F[i][j] = 0
            elif Weights[i-1] <= j:
                F[i][j] = max(Values[i-1] + F[i-1][j-Weights[i-1]],F[i-1][j])
            else:
                F[i][j] = F[i-1][j]
    return F[n][W]

n=int(input("Enter the total number of items: "))
Weights=[]
Values=[]
for i in range(n):
    w=int(input("Enter the weight: "))
    v=int(input("Enter the value: "))
    Weights.append(w)
    Values.append(v)
W=int(input("Enter the Knapsack capacity: "))
solution=Knapsack(W,Weights,Values,n)
print(solution)
