#Read  a list of string sort the list in an alphabetical order of string and replace the substring ‘a’ in each string with ‘b’
n=int(input("ENter how many strings"))
str=[]
for i in range(n):
    str.append(input("String {}".format(i+1)))
str.sort()
for i in range(len(str)):
    if "a" in str[i]:
        str[i] = str[i].replace("a", "b")
print(str)
