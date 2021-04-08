s={}
n=int(input("Enter no of students"))
print("Enter {} students name and scores in 3 subjects".format(n))
for i in range(n):
    nm=input("Name")
    m1=int(input())
    m2=int(input())
    m3=int(input())
    tm=m1+m2+m3
    for i in range(n):
        s.setdefault(nm,tm)
print("the dictionary is",s)
s1=s.values()
m=max(s1)
for j in s:
    if s[j]==m:
        print("student with highest score=",j)
k=s.keys()
k=sorted(k)
ns={}
for j in k:
    ns[j]=s[j]
print("soted dictionary is",ns)
    