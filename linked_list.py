class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        print_str=""
        itr = self.head
        while itr:
            print_str+= str(itr.data) + "-->"
            itr=itr.next
        print(print_str)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
        
    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data,None)
        if self.head == None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = node
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length(): raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count+=1
    
    def remove_at(self, index):
        if index < 0 or index > self.get_length(): raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = itr.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    
    def insert_values(self, data_list):
        self.head = None
        for d in data_list:
            self.insert_at_end(d)
