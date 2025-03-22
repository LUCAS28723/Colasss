class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_data = self.front_node.data
        self.front_node = self.front_node.next
        if not self.front_node:
            self.rear_node = None
        self.count -= 1
        return dequeued_data

    def front(self):
        return None if self.is_empty() else self.front_node.data

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

class PriorityQueue:
    def __init__(self):
        self.high_priority = Queue()
        self.normal_priority = Queue()

    def enqueue(self, element, priority=False):
        if priority:
            self.high_priority.enqueue(element)
        else:
            self.normal_priority.enqueue(element)

    def dequeue(self):
        if not self.high_priority.is_empty():
            return self.high_priority.dequeue()
        return self.normal_priority.dequeue()

    def is_empty(self):
        return self.high_priority.is_empty() and self.normal_priority.is_empty()

    def size(self):
        return self.high_priority.size() + self.normal_priority.size()

# Atención al cliente
def simulate_customer_service():
    service_queue = PriorityQueue()
    service_queue.enqueue("Cliente 1")
    service_queue.enqueue("Cliente VIP 1", priority=True)
    service_queue.enqueue("Cliente 2")
    service_queue.enqueue("Cliente VIP 2", priority=True)
    service_queue.enqueue("Cliente 3")
    
    while not service_queue.is_empty():
        print("Atendiendo a:", service_queue.dequeue())

simulate_customer_service()
