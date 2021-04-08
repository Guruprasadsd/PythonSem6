n=int(input("How many elements"))
l1=[]
l2=[]
l3=[]
print("Enter 1st tuple elements\n")
for i in range(n):
    l1.append(int(input()))
print("Enter 2nd tuple elements\n")
for i in range(n):
    l2.append(int(input()))
for i in range(n):
    x=l1[i]+l2[i]
    l3.append(x)
t1=tuple(l1)
t2=tuple(l2)
t3=tuple(l3)
print("first tuple",t1)
print("second tuple",t2)
print("sum of elements of tuples t1 and t2",t3)