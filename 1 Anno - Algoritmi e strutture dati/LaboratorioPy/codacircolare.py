class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue (self):
        if (len(self.queue)==0):
            return None
        else:
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) ==0

class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue (self,item):
        if((self.tail +1)%self.size == self.head):
            print ("Queue is Full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue [self.tail] = item
        else:
            self.tail = (self.tail +1)%self.size
            self.queue[self.tail]=item
    
    def dequeue(self):
        if (self.head == -1):
            print ("Queue is empty")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) %self.size
            return temp
    
    def display(self):
        if(self.head== -1):
            print("Non ci sono elementi nella coda")
        elif (self.tail >=self.head):
            for i in range (self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range (0,self.tail+1):
                print (self.queue[i], end=" ")
        
queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(3)
queue.enqueue(3)
queue.enqueue(3)
queue.display()

print ("\n")
print (queue.dequeue())
print (queue.dequeue())
print (queue.dequeue())
print (queue.dequeue())

queue.display()