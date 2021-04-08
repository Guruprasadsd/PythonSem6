#Using CREATES () create a dictionary where keys are numbers from 1 to 5 and their multiplicands as value. 
#Find the multiplicands of the key using nested function FIND()
#D={1:[1,2,3,4,5,6,7,8,9,10], 2:[2,4,6,8,10,12,14,16,18,20]……}
def CREATE():
    
    def FIND(s):
       l=[]
       for i in range(1,11):
           l.append(i*s)
       return 1
    dict={}
    for i in range(1,11):
        dict[i]=FIND[i]
    print(dict)    
CREATE()