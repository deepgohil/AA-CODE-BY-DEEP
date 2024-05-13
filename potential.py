class potential:
    def __init__(self):
        self.stack=[]
        self.size=0
        self.acost=0
    def push(self,data):
        
        self.stack.append(data)
        self.acost+=1+len(self.stack)-self.size
        self.size+=1
        print("stack is")
        self.printD()
        print(f"push cost is {self.acost}")
    def pop(self):
        
        self.stack.pop()
        self.acost+=1+len(self.stack)-self.size
        self.size-=1
        print("stack is")
        self.printD()
        print(f"pop cost is {self.acost}")
    def multipop(self,k):
        
        for i in range(k):
            self.stack.pop()
        self.acost+=k+len(self.stack)-self.size
        self.size-=k
        print("stack is")
        self.printD()
       
        print(f"pop cost is {self.acost}")
    
    
    def printD(self):
        if(len(self.stack)<=0):
            print("empty")
        for i in self.stack:
            print(f"{i}-",end=' ')

stack= potential()
stack.push(10)
stack.push(20)
stack.push(30)


stack.pop()
stack.multipop(2)