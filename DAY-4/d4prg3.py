l=[]
m=[]
p=[]
r=[]
n=int(input("Enter How Many subtuples\n"))
print("Enter {} subtuples".format(n))
for i in range(n):
    print("enter size of {}rd subtuple".format(i+1))
    a=int(input())
    l=[]
    print("enter {} no's".format(a))
    for j in range(a):
        b=int(input())
        l.append(b)
    m.append(l)

print("enter size of search subtuple")
c=int(input())
print("Enter elements of search tuple")
for i in range(c):
    d=int(input())
    p.append(d)
f=False
for i in m:
    if p in m:
        f=True
        del m[m.index(p)]        
    
if f:
    print("Found\n")
else:
    print("Not found\n")

for i in m:
    t1=tuple(i)
    r.append(t1)

t2=tuple(r)
print(t2) 