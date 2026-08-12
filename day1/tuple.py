"""wap that accepts a tuple of integers and returns a new tuple containing 
all duplicate elements, all unique elements, second largest, second smallest and freq of every element 
"""
t=(1,2,1,2,3,4,1,2,5,6,7)
unq=[]
dup=[]
largest=s_largest=float('-inf')
smallest=s_smallest=float('inf')
freq={}

for i in t:
    freq[i]=freq.get(i,0)+1

    if i>largest:
        s_largest=largest
        largest=i
    elif i>s_largest and i!=largest:
        s_largest=i

    if i<smallest:
        s_smallest=smallest
        smallest=i
    elif i<s_smallest and i!=smallest:
        s_smallest=i

for key in freq:
    if freq[key]==1:
        unq.append(key)
    else:
        dup.append(key)   

res=(tuple(unq),tuple(dup),s_largest,s_smallest,tuple(freq.items()))
print(res)