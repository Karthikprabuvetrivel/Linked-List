''' Circular Doubly Linked List'''

class Node():

    def __init__(self,data):

        self.data = data
        self.prev = None
        self.next = None


class LinkedList():

    def __init__(self):

        self.head = None
        self.tail = None

    def insertBegin(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = self.tail =  newNode
            self.head.next = self.head.prev = self.head

        else:
            
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.tail.next = self.head

    def insertEnd(self,data):

        newNode = Node(data)

        if self.tail == None:

            self.tail = self.head = newNode
            self.tail.prev = self.tail.next = self.tail

        else:

            newNode.prev = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            self.head.prev = self.tail

    def length(self):

        if self.head == None:

            return 0

        else:

            current = self.head
            count =1
            while current.next != self.head:
                
                current = current.next
                count +=1

            return count

    def insertAt(self,index,data):

        newNode= Node(data)

        if index < self.length():

            if index == 0:

                self.insertBegin(data)

            elif index == self.length()-1:

                self.insertEnd(data)

            else:

                prevNode = self.head
                pos = index-1

                while pos != 0:

                    prevNode = prevNode.next
                    pos -=1
                
                newNode.prev = prevNode
                newNode.next = prevNode.next
                prevNode.next.prev = newNode
                prevNode.next = newNode

        else:
            
            print("Index Outof Range")


    def deleteElement(self,element):

        if self.head == None:

            print("Empty LinkedList")
            return

        elif self.head.data == element:

            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            
            return
        
        elif self.tail.data == element:

            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            return

        else:

            current = self.head

            while current.next != self.head:

                
                if current.next.data == element:

                    current.next = current.next.next
                    current.next.prev = current

                    return 
                
                current = current.next

            print("Element Not Found")


    def showForward(self):

        if self.head == None:

            print("Empty LinkedList")

        else:

            current = self.head

            while current.next != self.head:

                print(current.data,end=",")
                current = current.next

            print(current.data)

    def showBackward(self):

        if self.tail == None:

            print("Empty LinkedList")

        else:

            current = self.tail

            while current.prev != self.tail:

                print(current.data,end=",")
                current = current.prev

            print(current.data)

if __name__ == "__main__":

    a = LinkedList()
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