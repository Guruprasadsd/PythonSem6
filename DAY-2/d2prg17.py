x=int(input("Enter a number"))
sum=0
temp=x
while temp>0:
    num=temp%10
    sum+=num**3
    temp=temp//10
if x==sum:
    print(x,"is a Armstrong Number")
else:
    print(x,"is Not a Armstrong number")

