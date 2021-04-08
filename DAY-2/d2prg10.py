x=input("Enter a number")
for i in range(int(len(x)/2)):
    if x[i]==x[len(x)-i-1]:
        print("is a palindrome")
        break
    else:
         print("not a  palindrom")
         break