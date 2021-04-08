city=[]
newcity=[]
n=int(input("Enter no of cities"))
print("Enter {} city names".format(n))
for i in range(n):
    s=input()
    city.append(s)
print("Elements in city list",city)
for k in city:
    if len(k)>3:
        print(k)
    else:
        newcity.append(k)
print("city names by excluding length>3",newcity)
    