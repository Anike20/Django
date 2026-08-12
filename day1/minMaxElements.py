""" Find the maximum and the minimum element in a list """
l=[1,2,3,4,5]
ma=l[0]
mi=l[0]
for i in l:
    if i>ma:
        ma=i
    elif i<mi:
        mi=i
print(ma,mi)