days=int(input("Enter days"))
year=int(days/365)
m1=days-(year*365)
months=int(m1/30)
rdays=m1-(months*30)
print("{} year, {} months, remaining days{}".format(year,months,rdays))
