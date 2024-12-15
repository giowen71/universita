#Classe di NOdo
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Pila
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size=0

#    def __str__(self):
#        cur= self.head.next
#        out = ""
#       while cur:
#            out += str(cur.value)+"->"
#            cur=cur.next
#        return out[:2]
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]  # Taglia gli ultimi due caratteri "->"

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size ==0

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.head.next.value

    def push (self, value):
        #print (value)
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    def pop(self):
        if self.isEmpty():
            raise Exception ("Empty Stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -=1
        return remove.value

#Main
A = Stack()
A.push(100)
A.push(20)
A.push(10)
A.push(5)


print(A)
print(A.peek());
print(A.pop())
print(A)
