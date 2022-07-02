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
    
    def removeNode(self, key):
        """
        If the key is found, remove it from the list and return the node
        
        :param key: The value to be removed from the list
        :return: The node that was removed.
        
        :Algorithm: O(n) linear time
        """
        current = self.head
        previous = None
        isFound = False

        while current and not isFound:
            if current.data == key and current is self.head:
                isFound = True
                self.head = current.nextNode
                self.__count -= 1
                return current.data
            elif current.data == key:
                isFound = True
                previous.nextNode = current.nextNode
                self.__count -= 1
                return current.data
            else:
                previous = current
                current = current.nextNode

        return None
    
    def removeAtIndex(self, index):
        """
        The function removes the node at the specified index and returns the data of the removed node
        
        :param index: the index of the node to remove
        :return: The data of the node that was removed.
        :Algorithm: O(n) Linear time
        """
        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.nextNode
            self.__count -= 1
            return current.data

        position = index

        while position > 1:
            current = current.nextNode
            position -= 1

        prevNode = current
        current = current.nextNode
        nextNode = current.nextNode

        prevNode.nextNode = nextNode
        self.__count -= 1

        return current.data
        
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
        
        if index >= self.__count:
            raise IndexError('Index out of range')

        if index == 0:
            return current.data
        else:
            current = current.nextNode
            position = 1

            while position < index:
                current = current.nextNode
                position += 1
                
        return current.data
         
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

# Add nodes to Singly Linked List
SinglyLinkedList = SinglyLinkedList()
SinglyLinkedList.addNode(10)
SinglyLinkedList.addNode(20)
SinglyLinkedList.addNode(30)
SinglyLinkedList.addNode(40)
SinglyLinkedList.addNode(50)
SinglyLinkedList.insertNode(17, 2)

# Print the visual presentation of Singly Linked List
print("\n##################################################################################################")
print("\n[Original] LinkedList: %s" % SinglyLinkedList)

# Get the size of Original Singly Linked List
print("\n[Original] LinkedList Size: %s" % SinglyLinkedList.__len__())

# Print the node removed from the singly linked list
# print(SinglyLinkedList.removeNode(15))
# print(SinglyLinkedList.removeNode(30))
print("Node Removed: %s" % SinglyLinkedList.removeAtIndex(2))

# Print the visual presentation of Singly Linked List
print("\n[After] LinkedList: %s" % SinglyLinkedList)

# Print the data of node at index 2
print("Node at index 2: %s" % SinglyLinkedList.nodeAt(2))

# Get the size of After Singly Linked List
print("\n[After] LinkedList Size: %s" % SinglyLinkedList.__len__())

print("\n##################################################################################################")