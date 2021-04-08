x=float(input("Enter x and y coordinates"))
y=float((input()))
if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
else:
    print("4th quadrant")