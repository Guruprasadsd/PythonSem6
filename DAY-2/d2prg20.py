n=int(input("Enter n and m "))
m=int(input())
sum=0
even=0
odd=0
for i in range(n,m+1):
    sum=sum+i
print("Sum of numbers is",sum)

for j in range(n,m+1):
    if j%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers are",even)
print("odd numbers are",odd)