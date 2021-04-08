import math
d=int(input("Enter a degree"))
x=math.radians(d)
sum=x
t=0
n=25
for i in range(3,n,2):
    t+=x**i/math.factorial(i)
print("sin(",x,")=",sum-t)
print("Using math function Sin(",x,")=",math.sin(x))