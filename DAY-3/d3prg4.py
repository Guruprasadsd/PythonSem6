n=int(input("enter the no of elements"))
ele=[]
for i in range(n):
    ele.append(int(input()))
occ=[]
j=0
for i in ele:
    if ele.index(i)<j:
        j=j+1
        continue
    else:
        j=j+1
        occ.append(ele.count(i))
print("occurance list=",occ)
