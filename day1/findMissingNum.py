"""A list contains n distinct numbers from zero to n.
Find the missing number from zero to n without using sum()"""

l=[0,1,2,4]
s1,s2=0,0
for i in range(len(l)+1):
    s1+=i
for i in l:
    s2+=i
print(s1-s2)