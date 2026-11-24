class PriorityQueue:
    # Lower priority number = higher priority (Min-Priority Queue)
    def __init__(self):
        self.items = []  # stores tuples of (priority, data)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data, priority):
        new_item = (priority, data)
        inserted = False
        for i in range(len(self.items)):
            if priority < self.items[i][0]:
                self.items.insert(i, new_item)
                inserted = True
                break
        if not inserted:
            self.items.append(new_item)

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue Underflow")
            return None
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            print("Priority Queue is empty")
            return
        print("Priority Queue (priority, data):", self.items)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task C", 3)
    pq.enqueue("Task A", 1)
    pq.enqueue("Task B", 2)
    pq.display()
    print("Served:", pq.dequeue())
    pq.display()