class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_begin(self, data):
        new_node = CNode(data)
        if self.last is None:
            self.last = new_node
            new_node.next = new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node

    def insert_end(self, data):
        new_node = CNode(data)
        if self.last is None:
            self.last = new_node
            new_node.next = new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def delete_node(self, key):
        if self.last is None:
            print("List is empty")
            return
        curr = self.last.next
        prev = self.last
        while True:
            if curr.data == key:
                if curr == self.last and curr.next == self.last:
                    self.last = None
                else:
                    prev.next = curr.next
                    if curr == self.last:
                        self.last = prev
                return
            prev = curr
            curr = curr.next
            if curr == self.last.next:
                break
        print(f"Key {key} not found")

    def display(self):
        if self.last is None:
            print("Circular List is empty")
            return
        curr = self.last.next
        elems = []
        while True:
            elems.append(str(curr.data))
            curr = curr.next
            if curr == self.last.next:
                break
        print("Circular List:", " -> ".join(elems) + " -> (head)")


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_begin(5)
    cll.display()
    cll.delete_node(20)
    cll.display()