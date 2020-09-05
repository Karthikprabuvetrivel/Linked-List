
''' Node Creation '''

class Node():

    def __init__(self,data):

        self.data = data
        self.next = None

''' Singly Linked List '''

class LinkedList():

    def __init__(self):

        self.head = None

    def insertBegin(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode

        else:
            
            newNode.next = self.head
            self.head = newNode
    
    def insertEnd(self,data):

        newNode = Node(data)

        if self.head == None:

            self.head = newNode

        else:

            lastNode = self.head

            while lastNode.next:

                lastNode = lastNode.next

            lastNode.next = newNode

    
    def insertAt(self,index,data):

        newNode = Node(data)

        if self.head != None:

            if 0<=index < self.length():

                if index == 0:

                    self.insertBegin(data)

                elif index == self.length()-1:

                    self.insertEnd(data)

                else:
                    num = index - 1
                    prev_node = self.head
                    while num!=0:

                        prev_node = prev_node.next
                        current_node = prev_node.next
                        num -=1
                    
                    newNode.next = current_node
                    prev_node.next = newNode

            else:

                print("Index out of Range")

        else:

            print("Empty List")
    
    def length(self):

        length = 0

        if self.head == None:

            return 0

        else:

            temp = self.head

            while temp:

                temp = temp.next
                length +=1

            return length

    def show(self): 

        if self.head == None:

            print("Empty LinkedList")
        
        else:

            temp =self.head

            while temp:
                
                print(temp.data,end=" ")
                temp = temp.next

    def deleteElement(self,element):

        if self.head == None:

            print("Empty Linked List")

            return

        elif self.head.data == element:

            temp = self.head.next
            self.head = temp
            temp = None
            return

        else:

            current = self.head

            while current.next != None:

                if current.next.data == element:

                    temp = current.next
                    current.next = temp.next
                    return

                else:
                    
                    current = current.next

            print("Element Not Found")


    def searchElement(self,element):

        index = 0
        
        if self.head == None:

            print("Empty Linked List")
            return 
        
        elif self.head.data == element:

            print("The element {} is in {} th index".format(element,index))
            return

        else:

            current = self.head
            index +=1
            while current.next !=None:

                if current.next.data == element:

                    print("The element {} is in {} th index".format(element,index))
                    return

                else:

                    current = current.next
                    index +=1

            print("Element Not Found")

    def reverse(self):

        if self.head == None:

            print("Empty LinkedList")

        else:

            prev = None
            current = self.head

            while current != None:

                next_ = current.next
                current.next  = prev
                prev = current
                current = next_

            self.head = prev
        
if __name__ == "__main__":

    a = LinkedList()

                






