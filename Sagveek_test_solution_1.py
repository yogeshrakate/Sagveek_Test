'''
Problem No. 1.
Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k
'''

def num_sum_list(S,k):
    l1=[]
    l2=[]
    for r in range(1,len(S)+1):#1
        def groups(S, r):
            l=list(S)
            n=len(l)
            if r>n:
                return
            indices=list(range(r))
            yield list(l[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i]!=i+n-r:
                        break
                else:
                    return
                indices[i]+=1
                for j in range(i+1, r):
                    indices[j]=indices[j-1]+1
                yield list(l[i] for i in indices)
        comb=groups(S,r)
        for i in comb:
            l1.append(i)
        for i in l1:
            if sum(i)==k and i not in l2:
                l2.append(list(i))
                break
    if len(l2)==0:
        return -1
    else:
        return l2[0]
print(num_sum_list([12,1,61,5,9,2],24))


