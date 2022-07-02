class Node:
    data = None
    nextNode = None
    
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
    def __repr__(self):
        "Data: %s" % self.data

class SinglyLinkedList:
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the head of the linked list to None
        """
        self.head = None
        self.__count = 0
    
    def __repr__(self):
        """
        We create a list called nodes, and then we iterate through the linked list, appending the data
        of each node to the list. 
        We also add a little bit of text to the beginning of each node's data to make it easier to read.
        Finally, we join the list together with " -> " between each node's data, and return the string
        """
        nodes = []
        current = self.head
        
        while(current):
            if current is self.head:
                nodes.append("[Head] %s" % current.data)
            elif current.nextNode is None:
                nodes.append("[Tail] %s" % current.data)
            else:
                nodes.append("[Body] %s" % current.data)
            current = current.nextNode
        return " -> ".join(nodes)
    
    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """
        return self.__count
    
    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next_node
    
    def isEmpty(self):
        """
        It checks if the list is empty.
        :return: True or False
        """
        return self.head is None
        
    def addNode(self, data):
        """
        It adds a new node to the beginning of the linked list.
        :param data: The data to be added to the list
        
        Algorithm: O(1) Constant time
        """
        newHead = Node(data, nextNode = self.head)
        self.head = newHead
        self.__count += 1
        
    def insertNode(self, data, index):
        """
        We create a new node, then we traverse the list until we reach the index we want to insert at,
        then we set the new node's next to the node at the index, and the node at the index's next to
        the new node
        
        :param data: the data to be inserted
        :param index: the position of the node to be inserted
        
        :Algorithm: 
            Insertion: 0(1) Constant Time.
            Finding the node insertion point/index: 0(n) Linear Time.
        """
        if index >= self.__count:
            raise IndexError("Index out of range")
        if index == 0:
            self.addNode(data)
            return
        elif index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.nextNode
                position -= 1
            
            prevNode = current
            nextNode = current.nextNode
            
            prevNode.nextNode = new
            new.nextNode = nextNode
        self.__count += 1
        
    def nodeAt(self, index):
        """
        It returns the node at the given index.
        
        :param index: The index of the node to return
        :return: The node at the given index.
        :Algorithm: 0(n) linear Time.
        """
        current = self.head
        
        if(current is not None):
            return current.data
        
        if index >= self.__count:
            raise IndexError('Index out of range')

        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.nextNode
                position += 1
                
        return current
         
    def searchNode(self, data):
        """
        It searches for a node in the linked list.
        :param data: The data to be searched for in the linked list
        :return: The node that contains the data that was passed in.
        Algorithm: 0(n) Linear time.
        """
        current = self.head
        
        while(current):
            if current.data == data:
                return current.data
            else:
                current = current.nextNode
        return "None"
    
    def getSize(self):
        """
        It counts the number of nodes in the linked list.
        :return: The size of the linked list
        """
        current = self.head
        count = 0
        
        while(current):
            count += 1
            current = current.nextNode
            
        return count
    
SinglyLinkedList = SinglyLinkedList()
N1 = Node(0);
SinglyLinkedList.addNode(1)
SinglyLinkedList.addNode(2)
SinglyLinkedList.addNode(3)
SinglyLinkedList.addNode(4)
SinglyLinkedList.insertNode(17, 2)

print(SinglyLinkedList)
# print(SinglyLinkedList.__len__())
print(SinglyLinkedList.nodeAt(0))
# print(SinglyLinkedList.getSize())