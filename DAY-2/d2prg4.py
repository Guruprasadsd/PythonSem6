x=[]
print("Enter 4 numbers")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    if a>c:
        if a>d:
            print("{} is largest".format(a))
        else:
            print("{} is large".format(d))
    elif c>d:
        print("{} is large".format(c))
    else:
        print("{} is large".format(d))
elif b>c and b>d:
    print("{} is large".format(b))
elif c>d:
    print("{} is large".format(c))
else:
    print("{} is large".format(d))