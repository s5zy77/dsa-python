class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = DNode(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_node(self, key):
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next
        if curr is None:
            print(f"Key {key} not found")
            return
        if curr.prev is not None:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev

    def reverse_iterative(self):
        curr = self.head
        temp = None
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev

    def display_forward(self):
        curr = self.head
        elems = []
        while curr is not None:
            elems.append(str(curr.data))
            curr = curr.next
        print("Forward:  None <-> " + " <-> ".join(elems) + " <-> None")

    def display_backward_recursive(self, node):
        if node is None:
            return
        self.display_backward_recursive(node.next)
        print(node.data, end=" <-> ")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_end(30)
    dll.insert_begin(5)
    dll.display_forward()

    dll.delete_node(20)
    dll.display_forward()

    dll.reverse_iterative()
    dll.display_forward()