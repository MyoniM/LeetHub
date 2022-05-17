class MyCircularDeque:

    def __init__(self, k: int):
        self.s = k
        self.f = -1
        self.r = -1
        self.arr = [None] * k
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.f = self.r = 0
                self.arr[self.f] = value
            elif self.f == 0:
                self.f = self.s - 1
                self.arr[self.f] = value
            else:
                self.f-=1
                self.arr[self.f] = value
            return True
        return False
    
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.f = self.r = 0
                self.arr[self.r] = value
            elif self.r == self.s - 1:
                self.r = 0
                self.arr[self.r] = value
            else:
                self.r+=1
                self.arr[self.r] = value
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            if self.r == self.f:
                self.r = self.f = -1
            elif self.f == self.s - 1:
                self.arr[self.f] = None
                self.f = 0               
            else:
                self.arr[self.f] = None
                self.f+=1      
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if self.r == self.f:
                self.r = self.f = -1
            elif self.r == 0:
                self.arr[self.r] = None
                self.r = self.s - 1                   
            else:
                self.arr[self.r] = None
                self.r-=1 
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.f]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.r]

    def isEmpty(self) -> bool:
        if self.f == -1 and self.f == -1:
            return True  
        return False  

    def isFull(self) -> bool:
        if self.f == self.r + 1 or (self.f == 0 and self.r == self.s - 1):
            return True  
        return False  


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()