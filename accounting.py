class accounting:
    def __init__(self):
        self.stack=[]
        self.cost=0
        self.amcost=0
        self.totalop=0
        self.creditbank=0

    def push(self,data):
        print(f"push {data}")
        self.stack.append(data)
        self.cost+=1
        self.amcost+=2
        self.totalop+=1
        self.creditbank+=1
        self.printD()
    def pop(self):
        print("pop data")
        self.stack.pop()
        self.cost+=1
        self.amcost+=0
        self.totalop+=1
        self.creditbank-=1
        self.printD()
    def multipop(self,k):
        for i in range(k):
            self.pop()


    def printD(self):
        if(len(self.stack)<=0):
            print("no data")
        else:
            for i in self.stack:
                print(i,end=" ")
        print("\n")    

stack = accounting()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.multipop(2)


print("Actual Cost: ", stack.cost)
print("Total Operations: ", stack.totalop)
print("Amortized Cost: ", stack.amcost)