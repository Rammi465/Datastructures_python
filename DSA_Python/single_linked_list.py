class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head =  None
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
    
        itr  = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
            
        print(llstr)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
            
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head =  node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head =  Node(data, None)
            return 
        
        itr =  self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
            
    def remove_at(self, index):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid Number")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_after_value(self, data_after, data_to_insert):
        #Search for first occurance of data_after value in linked list
        #Now insert data_to_insert after data_after node
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
            
    def remove_by_value(self, data):
        #Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            
            
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values(["banana", "Mango", "Grapes", "Orange"])
    ll.print()
    ll.insert_after_value("Mango", "apple")
    ll.print()
    ll.remove_by_value("Orange")
    ll.print()
    ll.remove_at(0)
    ll.print()
    print("length: ", ll.get_length())
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("Mango")
    ll.remove_by_value("Grapes")
    ll.remove_by_value("apple")
    ll.print()
