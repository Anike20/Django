"""Move all zeros to the end while maintaining the 
relative order of all non-zero elements"""
l=[0,1,0,4,12,0,5]
res=[]
pos=0
for i in l:
    if i!=0:
        res.append(i)
        pos+=1
while pos<len(l):
    res.append(0)
    pos+=1
print(res)