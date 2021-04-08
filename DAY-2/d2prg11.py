m=int(input("Enter m and n\n"))
n=int(input("\n"))
for i in range(m,n+1):
    for j in range(1,11):
        print("{}*{}={}\n".format(i,j,i*j),end=" ")
  
    print("\t")
    #print(i*1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10)