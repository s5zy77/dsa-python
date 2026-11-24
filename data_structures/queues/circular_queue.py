class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Circular Queue Overflow")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue Underflow")
            return None
        val = self.items[self.front]
        self.items[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return val

    def display(self):
        if self.is_empty():
            print("Circular Queue is empty")
            return
        result = []
        i = self.front
        while True:
            result.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print("Circular Queue:", result)


if __name__ == "__main__":
    cq = CircularQueue(4)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.display()
    print("Dequeued:", cq.dequeue())
    cq.enqueue(50)
    cq.display()