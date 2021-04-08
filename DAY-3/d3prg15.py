n=int(input("Enter no of rows"))
m=int(input("Enter no of columns"))
l=[]
for i in range(n):
    x=[]
    for j in range(m):
        x.append(int(input()))
    l.append(x)
print("elements of {}x{} matrix is".format(n,m))
for i in range (n):
    for j in range(m):
        print(l[i][j],end=" ")
    print()
trans=[]
print("Transpose of matrix")
for i in range (n):
    for j in range(m):
        print(l[j][i],end=" ")
    print()
    