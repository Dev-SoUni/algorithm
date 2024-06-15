class Queue:
    def __init__(self):
        self.queue_data = []

    def enqueue(self, data):
        self.queue_data.append(data)

    def dequeue(self):
        return self.queue_data.pop(0)


queue = Queue()
queue.enqueue("test")
queue.enqueue("aa")
queue.enqueue("bb")
queue.enqueue("cc")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

