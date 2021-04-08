x=input("Enter a string")
if x.isalpha():
    if x.isupper():
        print("{} is alpha and in uppercase".format(x))
    else:
       
        print("converted to upper as {}".format(x.upper()))
elif x.isnumeric():
    print(bin(int(x)))
else:
    print("invalid")