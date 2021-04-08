s=[]
n=int(input("Enter size of stack\n"))
while True:
    print("\n1.push\t2.pop\t3.display\t4.count\t5.exit")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        if len(s)==n:
            print("stack is overflow\n")
        else:
            print("Enter no push into stack")
            s.append(input())
    elif ch==2:
        if len(s)==0:
            print("stack is empty\n")
        else:
            n=s.pop()
            print("poped element is: ",n,"\n")
    elif ch==3:
        print("Stack is",s)
        #for i in s:
            #print(i,end='\t')
    elif ch==4:
        print("no of elements in stack is: ",len(s),"\n")
    elif ch==5:
        break
    else :
        print("invalid choice\n")
