"""
Question No. 10
Given a list of numbers and a number k, return
whether any two numbers from the list add up to k.

For example:
input: List=[10,15,3,7], K=17
output: True

"""

def sumToK(l,k):
    c=0
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j and l[i]+l[j]==k:
                c=1
    if c==1:
        return True
    else:
        return False
print(sumToK([10,15,3,7],17))
print(sumToK([10,15,3,7],18))
print(sumToK([10,15,3,7],19))
print(sumToK([10,15,3,7],20))
print(sumToK([10,15,3,7],25))

"""
If iit is to be solved in single pass
"""

from itertools import combinations
def sumToKInSinglePass(l,k):
    c=0
    for i in combinations(l,2):
        if sum(i)==k:
            c=1
    if c==1:
        return True
    else:
        return False
print(sumToKInSinglePass([10,15,3,7],17))
print(sumToKInSinglePass([10,15,3,7],18))
print(sumToKInSinglePass([10,15,3,7],19))
print(sumToKInSinglePass([10,15,3,7],20))
print(sumToKInSinglePass([10,15,3,7],25))
