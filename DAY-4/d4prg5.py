s={}
x=30
for i in range(1,x,2):
    b=i
    cube=b*b*b
    s.setdefault(i,cube)
print("Elements from 1-30 with cubes",s)