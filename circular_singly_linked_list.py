'''Circular Singly Linked List '''

class Node():

    def __init__(self,data):

        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):

        self.head = None
    
    def insertBegin(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode
            newNode.next = self.head

        else:

            current = self.head
            while current.next != self.head:
                current = current.next

            newNode.next = self.head
            current.next = newNode
            self.head = newNode

    def insertEnd(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode
            self.head.next = self.head

        else:

            current = self.head

            while current.next != self.head:

                current = current.next

            newNode.next = self.head
            current.next = newNode

    
    def length(self):

        if self.head == None:

            return 0

        else:

            current = self.head
            count = 1
            while current.next != self.head:

                current = current.next
                count +=1

            return count
    
    def insertAt(self,index,data):

        newNode = Node(data)

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

                nextNode = prevNode.next
                newNode.next = nextNode
                prevNode.next = newNode

        else:

            print("Index Outof Range")

    def deleteElement(self,element):

        if self.head.data == element:

            temp = self.head
            self.head = temp.next

            current = self.head

            while current.next != temp:

                current = current.next

            current.next = self.head
            return

        else:

            temp = self.head
            current = self.head
            
            while current.next != temp:

                if current.next.data == element:

                    current.next = current.next.next
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

            print(current.data,end=" ")
         
    
if __name__ == "__main__":

    a = LinkedList()
    a.insertBegin(4)
    a.insertBegin(3)
    a.insertBegin(1)
    a.insertEnd(5)
    a.insertEnd(6)
    a.insertAt(0,0)
    a.insertAt(2,2)
    a.insertAt(6,7)
    a.showForward()
    a.deleteElement(9)
    a.showForward()
            