import array
import random

class Queque:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        #we don't make python built-in list, because its type is dynamically allocated
        #instead we create our own fixed list
        self.data = array.array('i', range(size_max))
        #This assign data with array type (i = integer, with range of defined max_size

    def empty(self):
        return self.size == 0#Return the boolean type if there isn't any

    def full(self):
        return self.size == self.max#return the boolean type if there is max_size

    def enqueue(self,x):
        if self.size == self.max:
            return False#Can't add anymore if  size is already max
        self.data[self.tail] =x#This we try to set the tail to point to x
        self.size +=1#This try to increase the size to 1
        self.tail += 1#This set tail to next element of list, not last
        if self.tail ==self.max:#If already max, set tail back to zero
            self.tail = 0
        return True

    def dequeue(self):#Simply work reverse of enqueue function
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

#Queue(2) ==> set size_max to 2
#enqueue(6) ==> append 6
#enqueue(6) ==> append 7
#enqueue(6) ==> False, already 2 element in the list
#deque()#return first element, 6
#deque()#return first element, 7
#deque() ==> return None, there isn't any left

q = Queque(2)
print q.tail

