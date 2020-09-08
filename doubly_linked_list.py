'''Doubly LinkedList'''


''' Node class'''

class Node():

    def __init__(self,data):

        self.data = data
        self.prev = None
        self.next = None

'''LinkedList class'''

class LinkedList():

    def __init__(self):

        self.head = None
        self.tail = None
    
    def insertBegin(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode
            self.tail = newNode

        else:

            temp = self.head
            newNode.next = temp
            temp.prev = newNode

            self.head = newNode

    def insertEnd(self,data):

        newNode = Node(data)

        if self.tail == None:

            self.head = newNode
            self.tail = newNode

        else:

            temp = self.tail 

            newNode.prev = temp
            temp.next = newNode

            self.tail = newNode

    def length(self):

        if self.head ==  None:

            return 0

        else:

            current = self.head
            count = 0
            while current !=None:

                current = current.next
                count +=1

            return count

    def insertAt(self,index,data):

        if index<self.length():

            if index == 0:

                self.insertBegin(data)

            elif index == self.length()-1:

                self.insertEnd(data)

            else:

                newNode = Node(data)

                temp = self.head

                value = index

                while value!=0:

                    prevNode = temp
                    temp = temp.next
                    value -=1

                nextNode = prevNode.next
                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = nextNode
                nextNode.prev = newNode

        else:

            print("Index Outof Range")

    def deleteElement(self,element):

        if self.head == None:

            print("Empty LinkedList")

        elif self.head.data == element:

            temp = self.head.next
            self.head = temp
            self.head.prev = None
            temp = None
            return

        elif self.tail.data == element:

            temp = self.tail.prev
            self.tail = temp
            self.tail.next = None
            temp = None
            return
 
        else:

            current = self.head

            while current.next != None:

                if current.next.data == element:

                    nextNode = current.next.next
                    current.next = nextNode
                    nextNode.prev = current
                    return

                else:

                    current = current.next

            print("Element Not Found")

                                                                            
    def showForward(self):

        if self.head == None:

            print("Empty LinkedList")

        else:

            current = self.head

            while current.next !=None:

                print(current.data,end=",")

                current = current.next
            
            print(current.data)

    def showBackward(self):

        if self.tail == None:

            print("Empty LinkedList")

        else:

            current = self.tail

            while current.prev !=None:

                print(current.data,end=",")

                current = current.prev

            print(current.data)

if __name__ == "__main__":

    a= LinkedList()
    a.insertBegin(4)
    a.insertBegin(2)
    a.insertBegin(1)
    a.insertEnd(5)
    a.insertEnd(6)
    a.insertAt(2,3)
    a.insertAt(5,7)
    a.showForward()
    a.showBackward()
    a.deleteElement(7)
    a.showForward()
    a.showBackward()