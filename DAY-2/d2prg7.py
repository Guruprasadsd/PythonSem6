import math
a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter C value:"))
d=(b**2)-(4*a*c)
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are Real and Distinct=",r1,r2)
elif d==0:
    r1=(-b)/(2*a)
    r2=(-b)/(2*a)
    print("Roots are real and equal",r1,r2)
else:
    r1=complex((-b/(2*a)),(math.sqrt(d)/2*a))
    r2=complex((-b/(2*a)),(-math.sqrt(d)/2*a))
    print("Roots are complex and imaginary")