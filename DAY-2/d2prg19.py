import math
x=int(input("Enter a degree"))
t=1
n=int(input("enter n"))
for i in range(1,n):
    t+=x**i/math.factorial(i)
print("e^",x,"=",t)
print("Using math function e^",x,"=",math.e**x)