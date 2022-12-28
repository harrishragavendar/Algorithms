import math
def closest_pair(p):
    d_min = float("inf")
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            d = math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)
            if(d < d_min):
                d_min = d
                points = [ [p[i][0],p[i][1]] , [p[j][0],p[j][1]] ]
    print("Closest Pair of points : ",points)
    print("Distance between the closest pair of points : ",round(d_min,3))
n=int(input("Enter the number of points : "))
p=[]
for i in range(n):
    x=int(input("Enter the x co-ordinate : "))
    y=int(input("Enter the y co-ordinate : "))
    p.append([x,y])
closest_pair(p)