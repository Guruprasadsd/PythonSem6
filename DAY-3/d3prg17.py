ml=[]
n=int(input("Enter how many elements in main list"))
for i in range(n):
    sl=[]
    m=int(input("Enter size of sublist"))
    for j in range(m):
        sl.append(int(input()))
    ml.append(sl)
size=int(input("Enter the size of list to be searched"))
il=[]
for i in range(size):
    il.append(int(input()))
print(il)
if il in ml:
    print("The list exist")
else:
    print("There is no such list")
    
 
#print("Given list is",l)
#ls=[]
#print("Enter the elements in sublist")
"""ls.append(input())
if ls in l: 
    print("Exist in list") 
else: 
    print("Does not exist in list")"""