print("------------PATTERN---------------")
for k in range(1,5):
    for i in range(1,k+1):
        print(i,end=" ")
    print()
print("------------STAR PATTERN---------------")
for k in range(4,0,-1):
    for i in range(k,0,-1):
        print("*",end=" ")
    print()
    