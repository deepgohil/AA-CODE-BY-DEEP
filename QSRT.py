import random
import time
c1,c2=0,0
def RQs(arr):
    global c1
    if(len(arr)<=1):
        return arr
    pivot=random.choice(arr)
    less=[x for x in arr if x < pivot]
    eq=[x for x in arr if x == pivot]
    gt=[x for x in arr if x > pivot]
    c1+=len(less)+len(gt)
    return RQs(less)+eq+RQs(gt)

def Qs(arr):
    global c2
    if(len(arr)<=1):
        return arr    
    pivot=arr[0]
    left=[x for x in arr[1:] if x <= pivot]
    right=[x for x in arr[1:] if x > pivot]
    c2+=len(arr)-1
    return Qs(left)+[pivot]+Qs(right)


Marr = [10,9,8,7,6,5,4,1,3,2]
print(Qs(Marr))
print(c2)

Marr = [10,9,8,7,6,5,4,1,3,2]
print(RQs(Marr))
print(c1)