#15......Using ISIN() check for the existence of a substring within a string and return Boolean value
#Count the number of  occurrences of a given word and character in a given string
str = input("Enter the string")
substr= input("Enter the substring to be searched for existance")
a=int(str.count(substr))
def isin():
    if a>0:
        print(True)
    else: 
        print(False)
isin()
    
