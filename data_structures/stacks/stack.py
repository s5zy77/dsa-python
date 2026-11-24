class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.items[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        val = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.top]

    def reverse_iterative(self):
        left, right = 0, self.top
        while left < right:
            self.items[left], self.items[right] = self.items[right], self.items[left]
            left += 1
            right -= 1

    def _insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
            return
        temp = self.pop()
        self._insert_at_bottom(item)
        self.push(temp)

    def reverse_recursive(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse_recursive()
            self._insert_at_bottom(temp)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top to bottom):", [self.items[i] for i in range(self.top, -1, -1)])


if __name__ == "__main__":
    s = Stack(5)
    for x in [10, 20, 30, 40]:
        s.push(x)
    s.display()
    s.reverse_recursive()
    print("After Recursive Reverse:")
    s.display()
    s.reverse_iterative()
    print("After Iterative Reverse:")
    s.display()