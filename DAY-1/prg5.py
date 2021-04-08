p=int(input("Enter p t and r"))
t=int(input())
r=int(input())
SI=p*t*r/100
CI=p*((pow((1+r/100),t)))
print("Simple interest=",SI)
print("compound interest =",CI)