n=int(input("Enter two numbers n and m"))
m=int(input())
for i in range(n,m+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            if i%10!=3:
                print(i)
            
        