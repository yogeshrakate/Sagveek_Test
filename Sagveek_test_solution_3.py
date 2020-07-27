'''Question No. 3
Compute the running median of a sequence of numbers.
'''

def runningMedian(s):
    for i in range(len(s)):
        l=s[:i+1]
        l.sort()
        if len(l)%2!=0:
            print(l[len(l)//2])
        else:
            print((l[len(l)//2]+l[(len(l)//2)-1])/2)
            
runningMedian([2,1,5,7,2,0,5])
