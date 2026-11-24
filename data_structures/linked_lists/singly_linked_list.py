class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def insert_after(self, target_val, data):
        curr = self.head
        while curr is not None and curr.data != target_val:
            curr = curr.next
        if curr is None:
            print(f"Node {target_val} not found")
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr is not None and curr.data != key:
            prev = curr
            curr = curr.next
        if curr is None:
            print(f"Key {key} not found")
            return
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next

    # --- Iterative & Recursive Search ---
    def search_iterative(self, key):
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == key:
                return pos
            curr = curr.next
            pos += 1
        return -1

    def search_recursive(self, node, key, pos=0):
        if node is None:
            return -1
        if node.data == key:
            return pos
        return self.search_recursive(node.next, key, pos + 1)

    # --- Iterative & Recursive Reverse (High-yield exam question) ---
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def _reverse_rec_helper(self, curr):
        if curr is None or curr.next is None:
            return curr
        new_head = self._reverse_rec_helper(curr.next)
        curr.next.next = curr
        curr.next = None
        return new_head

    def reverse_recursive(self):
        self.head = self._reverse_rec_helper(self.head)

    # --- Iterative & Recursive Display ---
    def display_iterative(self):
        curr = self.head
        elems = []
        while curr is not None:
            elems.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elems) + " -> None")

    def display_recursive(self, node):
        if node is None:
            print("None")
            return
        print(node.data, end=" -> ")
        self.display_recursive(node.next)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_end(10)
    sll.insert_end(20)
    sll.insert_end(30)
    sll.insert_begin(5)
    sll.insert_after(20, 25)
    sll.delete_node(10)
    sll.display_iterative()

    print("Search 25 (Iterative):", sll.search_iterative(25))
    print("Search 25 (Recursive):", sll.search_recursive(sll.head, 25))

    sll.reverse_iterative()
    print("Reversed (Iterative): ", end="")
    sll.display_iterative()

    sll.reverse_recursive()
    print("Reversed (Recursive): ", end="")
    sll.display_recursive(sll.head)