class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        currentIndex = 0
        currentNode = self.head
        while currentNode:
            if currentIndex == index:
                return currentNode.val
            currentNode = currentNode.next
            currentIndex += 1
        return -1
    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val,None)
        if self.head == None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.get_length(): return
        if index == 0:
            self.addAtHead(val)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(val, itr.next)
                break
            itr = itr.next
            count+=1
        
    def deleteAtIndex(self, index: int) -> None:
        print(index, self.get_length())
        if index < 0 or index > self.get_length(): return
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1 and itr.next is not None:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)