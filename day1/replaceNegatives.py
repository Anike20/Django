"""Replace all -ve numbers in the list with zeros"""
l=[-1,2,9,0,-2,4,-6,-7]
for i in range(len(l)):
    if l[i]<0:
        l[i]=0
print(l)