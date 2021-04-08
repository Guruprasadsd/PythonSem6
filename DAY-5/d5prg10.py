#Convert string to dictionary or vice versa -Example   input   “A-13 B-14 C-14”   output {‘A’:13, ‘B’:14,’C’:14}
ch = int(input("Enter the option \n1.Dictionary to string\t2.string to dictionary\n"))
if ch == 2:
    str = [n.split("-") for n in input("Give the dictionary string for eg:'A-20' ").split()]
    print(str)
    dic = dict(str)
    for i in dic:
        dic[i] = int(dic[i])
    print(dic)
elif ch == 1:
    dic = {}
    n = int(input("Enter the no of elements"))
    for i in range(n):
        key = input("Enter the key")
        value = int(input("Enter the value"))
        dic[key] = value
    print(dic)
    stru = " "
    for i in dic:
        stru += i
        #stru += "-"
        stru += str(dic[i])
        stru += " "
    print("Converted\n",stru)
else:
    print("Invalid")