print("Enter a series")
m=int(input("M"))
n=int(input("N"))
s=int(input("Enter number of Terms you need:"))
print(m,n,end=" ")
while s-2:
    c=m+n
    m=n
    n=c
    print(c,end=" ")
    s=s-1