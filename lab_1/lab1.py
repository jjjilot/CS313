class QueueCapacityTypeError(Exception):
    pass


class QueueCapacityBoundError(Exception):
    pass


class QueueIsFull(Exception):
    pass


class QueueIsEmpty(Exception):
    pass


class StackCapacityTypeError(Exception):
    pass


class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class StackCapacityBoundError(Exception):
    pass


class Node:

    def __init__(self, data=None):
        """

        """
        ####### YOUR CODE STARTS HERE #######
        self.data = data
        self.next = None


class Queue:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise QueueCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise QueueCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            self.head = None
            self.tail = None
            self.capacity = capacity
            self.currentSize = 0

    def enqueue(self, item):
        ####### YOUR CODE STARTS HERE #######
        if self.isFull():
            return False
        else:
            new_node = Node(data=item)
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
                
            self.currentSize += 1
            return True

    def dequeue(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        else:
            return_val = self.front()
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.currentSize -= 1
        if self.isEmpty():
            self.tail = None
        return return_val

    def front(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        return (self.currentSize == 0)

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        return (self.currentSize == self.capacity)


class Stack:

    def __init__(self, capacity):
        """

        """
        if type(capacity) != int:
            raise StackCapacityTypeError('Invalid type of capacity')
        elif capacity < 1:
            raise StackCapacityBoundError('Invalid capacity')
        else:
            ####### YOUR CODE STARTS HERE #######
            self.capacity = capacity
            self.head = None
            self.currentSize = 0

    def push(self, item):
        ####### YOUR CODE STARTS HERE #######
        if self.isFull():
            return False
        else:
            new_node = Node(data=item)
            new_node.next = self.head
            self.head = new_node
            self.currentSize += 1
        return True
        
    def pop(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        else:
            return_val = self.peek()
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.currentSize -= 1
        return return_val

    def peek(self):
        ####### YOUR CODE STARTS HERE #######
        if self.isEmpty():
            return False
        return self.head.data

    def isEmpty(self):
        ####### YOUR CODE STARTS HERE #######
        return self.currentSize == 0

    def isFull(self):
        ####### YOUR CODE STARTS HERE #######
        return self.capacity <= self.currentSize

# Q = Queue(6)
# N1 = Node(1)
# Q.head = Q.tail = N1
# Q.currentSize = 1
# ret = Q.dequeue()

# try:
#     assert Q.head is not N1
#     assert Q.tail is not N1
# except:
#     print("fuck you")

# print(N1.data)
# print(Q.head)
# print(Q.tail)