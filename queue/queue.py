"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# 1.
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         return None


#2.
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        #add to tail
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        #remove from head
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        return None

#3. Because total number of items is changing, LL is more efficient worst case because of BigO:
# Adding/Removing items to queue with LL is Constant O(1)
# Appending item to queue with array is Linear O(n), removing from stack with array is O(1)

"""
Stretch:

If you could only use instances of your Stack class to implement the Queue:
    You would have stack 1 and stack 2:
        enqueue: the new element is entered at the top of a stack 1. This would be Constant O(1).
        dequeue: if stack 2 is empty then all elements are moved to stack 2 and then top of stack 2 is returned. O(n) Linear.
Therefore overall would be O(n), similar to using an Array.
"""