class node():
    def __init__(self,value):
        self.value = value
        self.next = None

class myList():
    def __init__(self):
        self.head = None

    def showList(self):
        
        curr= self.head
        while (curr!=None):
            print(curr.value, end = '->')
            curr = curr.next
        print ('Finito\n')
    
    def headInsert(self, newValue):
        newNode = node(newValue)
        if(self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def tailInsert(self, newValue):
        if(self.head == None):
            self.headInsert(newValue)
        else:
            curr = self.head
            while (curr.next !=None):
                curr = curr.next
            
            newNode = node(newValue)
            curr.next = newNode

    def findElem(self, toFind):
        self.toFind = toFind
        print ("Sto cercando l'elemento ->"+ str(self.toFind))
        curr = self.head
        while (curr!=None):
            if (curr.value == toFind):
                return True
            else:
                curr = curr.next
        return False
    
    def headRemove (self):
        print ("Rimouviamo la testa \n")
        if(self.head !=None):
            headNode = self.head
            self.head = self.head.next
            headNode.next = None
            return headNode
        return None
    
    def tailRemove(self):
        print ("Rimouviamo la coda \n")
        if(self.head == None or self.head.next ==None):
            return self.headRemove()
        else:
            curr = self.head
            prev = None
            while (curr.next !=None):
                prev=curr
                curr = curr.next
            prev.next = curr.next
            return curr
        
    def positionRemove(self,index):
        pass

    def positionInsert (self, newValue, index):
        print ("Inseriamo nuovo elemento")
        if(index==0 or self.head ==None):
            self.headeInsert(newValue)
        else:
            i=0
            curr = self.head
            prev = None
            newNode = node(newValue)
            while (i<index and curr!=None):
                i=i+1
                prev=curr
                curr = curr.next
            
            if (curr==None):
                prev.next=newNode
            else:
                newNode.next = newNode
                prev.next = newNode

    
newList = myList()
newList.headInsert(1)
newList.headInsert(8)
#newList.showList()
newList.tailInsert(1)
newList.tailInsert(8)
newList.showList()
if newList.findElem(4):
    print ("....Perfetto, Elemento Trovato")
else:
    print ("....!Aia Elemento non trovato!")
newList.headRemove()
newList.showList()
newList.tailRemove()
newList.showList()
newList.positionInsert(3,5)
newList.showList()