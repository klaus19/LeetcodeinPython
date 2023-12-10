class Queue(object):

     def __init__(self):
         self.items = []

     def enqueue(self,item):
         self.items.append(item)

     def dequeue(self):
         if not self.is_empty():
             return self.items.pop(0)
         else:
             print("Queue is empty")


     def is_empty(self):
         return len(self.items) == 0

     def size(self):
         return len(self.items)

if __name__ == "__main__":
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    # Dequeue elements
    print(my_queue.dequeue())  # Output: 1
    print(my_queue.dequeue())  # Output: 2

    # Check if the queue is empty
    print(my_queue.is_empty())  # Output: False

    # Enqueue more elements
    my_queue.enqueue(4)
    my_queue.enqueue(5)

    # Get the size of the queue
    print(my_queue.size())  # Output: 3


