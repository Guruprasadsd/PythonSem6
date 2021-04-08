x=int(input("Enter a number"))
if x==1:
    print("{} is neither prime nor composite")
else:
    f=True
    i=2
    while i<=x/2:
        if x%i==0:
            f=False
            break
        i=i+1
    if f:
        print("{} is prime".format(x))
    else: 
        print("{} is composite ".format(x))