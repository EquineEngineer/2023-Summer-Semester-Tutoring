from __future__ import annotations


class Node:
    """
    Node for a LinkedList
    """

    def __init__(self, value, _next):
        self.value = value
        self._next = _next


class LinkedList:
    """
    Single-link linked list
    """

    def __init__(self):
        """
        Example init:

        ll = LinkedList()

        # Adding elements:

        ll.add(1)
        ll.add(2)
        ll.add(3)
        """

        self.head: Node | None = None

    def __iter__(self):
        """
        Takes your data structure and transforms it into an iterator
        """

        if self.head is None:
            return None

        current = self.head

        while current is not None:
            yield current
            current = current._next

    def add(self, value):
        """
        Takes `value` and appends it to the linked list
        """

        for element in self:
            if element._next is None:
                element._next = Node(value, None)

    def find(self, sentinel):
        """
        Returns the node where `value == sentinel`

        If no such node exists, return None
        """

        for element in self:
            if element.value == sentinel:
                return element
