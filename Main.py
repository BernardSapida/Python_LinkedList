class Node:
    data = None
    nextNode = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        "Data: %s" % self.data

class LinkedList:
    def __init__(self):
        """
        The function __init__() is a constructor that initializes the head of the linked list to None
        """
        self.head = None
        
    def isEmpty(self):
        """
        It checks if the list is empty.
        :return: True or False
        """
        return self.head == None
    
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
    
    def add(self, data):
        """
        It adds a new node to the beginning of the linked list.
        :param data: The data to be added to the list
        """
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
        
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
    
    
    
linkedList = LinkedList()

linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)

print(linkedList)
print(linkedList.getSize())
# print(linkedList.getSize())