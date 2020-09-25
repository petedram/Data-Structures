"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)
        # 1. add empty node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #2. add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.head
            self.tail = None
            self.head = None
            self.length -= 1
            return node.value
        else:
            node = self.head
            self.head.delete()
            self.head = self.head.next
            self.length -= 1
            return node.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create new node
        new_node = ListNode(value)
        #add an empty node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        #2. add to nonempty
        else:
            new_node.next = None #new tail points to None
            self.tail.next = new_node #previous tail points to new tail
            new_node.prev = self.tail #new tail prev points to previous tail 
            self.tail = new_node #set new node to tail
        self.length += 1 #add to length

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.length -= 1
            return node.value        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.delete()
        node.prev, node.next = self.tail, None
        self.tail.next = node
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
    #dont need to return value
    # Do need to return value
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: #list has +2 nodes
            self.head = node.next
            node.delete() #updating prev and/or next pointers
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
        self.length -= 1



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        max = self.head.value
        node = self.head.next
        while node is not None:
            if node.value > max:
                max = node.value
            node = node.next
        return max
