print("Enter marks in 3 subjects")
m1=int(input())
m2=int(input())
m3=int(input())
perc=((m1+m2+m3)*100)/300
print("petrcentage=",perc)
if perc>=80:
    print("A grade")
elif perc>=60 :
    print("B grade")
elif perc>=40:
    print("C grade")
else:
    print("D grade")
    