stack=[]
nop=0
cost=0

def push(data):
    stack.append(data)
    global nop
    global cost
    nop+=1
    cost+=1


def pop():
    if(len(stack)==0):
        print("Underflow")
    data=stack.pop()
    print(data)
    global nop
    global cost
    nop+=1
    cost+=1


def multipop(opr):
    for x in range(opr):
        pop()


push(10)
push(20)
push(30)


pop()
multipop(2)
print("Stack after multipop: ")
for i in stack:
    print(i, end=" ")

print("\n\nTotal operations: ", nop)
print("Total cost: ", cost)
print("Amortized cost: ", cost/nop)