"""Leap year check"""
year=2004
if year%100 == 0 and year%400 == 0:
    print("Leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not leap year")