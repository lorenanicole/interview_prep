class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList(object):
    """
    Ref: https://stackabuse.com/python-linked-lists/
    """
    def __init__(self, val):
        self.head = Node(val) if not isinstance(Node, val) else val
        self.tail = None
        self.nodes = 1 if self.head else 0

    def insert(self, val):
        val = Node(val) if not isinstance(Node, val) else val
        previous = None

        if not self.head:  # add head node
            self.head = val
            self.tail = val
        else:  # otherwise update the current tail with next pointer
            previous = self.tail
            self.tail.next = val  # first add new next for current tail
            val.previous = previous  # update new node with the old/current tail as prev
            self.tail = val  # add new node to end

        self.nodes += 1

    def remove(self, data_to_remove):
        current = self.head

        while current:
            previous = current.previous
            next = current.next

            if current.data == data_to_remove:
                if previous:
                    previous.next = next
                    if next:
                        next.previous = previous
                else:
                    self.head = next
                    if next:
                        next.previous = None
                return

            current = next

    def size(self):
        return self.nodes

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next