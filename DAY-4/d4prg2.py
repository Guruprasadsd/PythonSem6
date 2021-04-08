x=[];p=[]
y=[];s=[]
z=[];r=[]
m=int(input("Size of main tuples\n"))
print("For 1st subtuple")
for i in range(m):
    n=int(input("Enter size of {} subtuple\n".format(i+1)))
    w=[]
    print("enter {} elemets".format(n))
    for j in range(n):
        k=int(input())
        w.append(k)
    x.append(w)

q=[]
print("For 2nd tuple")
for i in range(m):
    n=int(input("Enter size of {} subtuple\n".format(i+1)))
    q.append(n)
    w=[]
    print("enter {} elemets".format(n))
    for j in range(n):
        k=int(input())
        w.append(k)
    y.append(w)

for i in range(n):
    g=[]
    for j in range(len(x[0])):
        if x[i][j]>=y[i][j]:
            g.append(x[i][j])
        else:
            g.append(y[i][j])
    z.append(g)

for i in range(len(x)):
    t1=tuple(x[i])
    p.append(t1)
t1=tuple(p)
print("1st-\t",t1)
    
for i in range(len(y)):
    t2=tuple(y[i])
    s.append(t2)
t2=tuple(s)
print("2nd-\t",t2)

for i in range(len(z)):
    t3=tuple(z[i])
    r.append(t3)
t3=tuple(r)
print("\nResult-\t",t3)