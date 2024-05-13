from operator import itemgetter

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def makekdt(points,depth=0):
    if(len(points)==0):
        return None
    
    k=len(points[0])
    axis=depth%k
    points.sort(key=itemgetter(axis))
    mid=len(points)//2
    node=Node(points[mid])
    node.left=makekdt(points[:mid],depth+1)
    node.right=makekdt(points[mid+1:],depth+1)
    return node

def traversal(root):
    if root:
        traversal(root.left)
        print(root.val)
        traversal(root.right)
    
seq = [[6,2], [7,1], [2,9], [3,6], [4,8], [8,4], [5,3], [1,5], [9,5]]
root=makekdt(seq)
traversal(root)