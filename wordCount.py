# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
        self.wordCount = 1


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    f = open("speech.txt", "r")
    x = (f.readline())
    x = x.split()
    print(x)
    print("Hello world")

    llist.head = Node(x[0])
    temp = llist.head
    r = 0
    for r in x:
        temp.data = Node(r)
        temp.next = Node("end")
        temp = temp.next
    #    r = r+1
    # llist.head.next = second;  # Link first node with second
    # second.next = third;  # Link second node with the third node
    print (llist.head.data.data)
    temp = llist.head

    while temp.next.next is not None:
        print (temp.data.data)
        temp = temp.next
