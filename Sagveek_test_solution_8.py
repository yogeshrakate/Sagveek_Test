'''
Question No. 8
Write a function that takes a list of integers and
returns the largest sum of non-adjacent numbers.

For example:
input:[2,4,6,2,5] ----> Output:13===>2+6+5
input:[5,1,1,5] ----> Output:13===>5+5
'''

def LargeSum(l):
    incl = 0
    excl = 0
    for i in l:
        new_excl = max(excl, incl)
        incl = excl + i 
        excl = new_excl
    return max(excl, incl)
    
print(LargeSum([2,4,6,2,5]))
print(LargeSum([5,5,1,1,5]))
