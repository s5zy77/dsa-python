class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.items[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        val = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return val

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", [self.items[i] for i in range(self.front, self.rear + 1)])


if __name__ == "__main__":
    q = LinearQueue(4)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    print("Dequeued:", q.dequeue())
    q.display()