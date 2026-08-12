"""how many elements in list are greater than avg of all elements"""
l=[11,12,10,14,15,9]
s=sum(l)
avg=s/len(l)
print(avg)
count=0
for i in l:
    if i>avg:
        count+=1
print(count)