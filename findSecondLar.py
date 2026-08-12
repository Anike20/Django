"""wap to find second largest number among numbers"""
nums=[12,13,11,10,9,18,20]
first=float('-inf')
second=float('-inf')
for i in nums:
    if i>first:
        second=first
        first=i
print(second)