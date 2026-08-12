"""wap to remove duplicate elements while preserving their first occurence.
without set()
"""
l=[1,4,2,2,1,0,2,3,4]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)