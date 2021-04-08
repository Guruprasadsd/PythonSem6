s=input("Enter a string:")
j=0
k=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        j=j+1
    elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        j=j+1
    elif(i>='a' and i<='z')or(i>='A' and i<='Z'):
        k=k+1
    else:
        pass
print("Number of Vowels = ",j)
print("Number of Consonants = ",k)
    