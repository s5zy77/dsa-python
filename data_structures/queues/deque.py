class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def insert_front(self, data):
        if self.is_full():
            print("Deque Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity
        self.items[self.front] = data

    def insert_rear(self, data):
        if self.is_full():
            print("Deque Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = data

    def delete_front(self):
        if self.is_empty():
            print("Deque Underflow")
            return None
        val = self.items[self.front]
        self.items[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return val

    def delete_rear(self):
        if self.is_empty():
            print("Deque Underflow")
            return None
        val = self.items[self.rear]
        self.items[self.rear] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return val

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return
        result = []
        i = self.front
        while True:
            result.append(self.items[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print("Deque:", result)


if __name__ == "__main__":
    dq = Deque(5)
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.display()
    print("Deleted front:", dq.delete_front())
    print("Deleted rear:", dq.delete_rear())
    dq.display()