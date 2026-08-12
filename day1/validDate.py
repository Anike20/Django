"""Check whether date is valid"""
date="31/2/2020"
l_date=date.split("/")

day=int(l_date[0])
month=int(l_date[1])
year=int(l_date[2])

count=[31,28,31,30,31,30,31,31,30,31,30,31]

if year%4==0 or (year%100==0 and year%400==0):
    l_date[1]=29
if 1<=month<=12 and 1<=day<=count[month-1]:
    print("Valid date")
else:
    print("Invalid date")