"""
Question No. 9
Given an array of int, return a new array that each element a
t index i of the new array is the product of all the numbers
in the original array except the one at i.

For Example:
input: [1,2,3,4,5]----> output: [120,60,40,30,24]
input: [3,2,1]----> output: [2,3,6]
"""

def productOfElements(l):
    prod=1
    for i in range(len(l)):
        prod*=l[i]
    return [int(prod/l[i]) for i in range(len(l))]
print(productOfElements([1,2,3,4,5]))
print(productOfElements([3,2,1]))

'''
If we can't use division
'''
def productOfElementsWithoutDivision(l):
    ans=[]
    for i in range(len(l)):
        pro=1
        for j in range(len(l)):
            if j!=i:
                pro*=l[j]
        ans.append(pro)
    return ans
    
print(productOfElementsWithoutDivision([1,2,3,4,5]))
print(productOfElementsWithoutDivision([3,2,1]))
        
