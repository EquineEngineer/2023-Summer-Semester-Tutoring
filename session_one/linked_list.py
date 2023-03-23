from __future__ import annotations


class Node:
    """
    A node in a linked list.

    A node holds an integer value and a reference to the next node in the list.

    By default, a node points to None.
    """

    def __init__(self, value, ref=None):
        self.value = value
        self.ref = ref


class LinkedList:
    """
    A linked list.

    A linked list is a collection of nodes that are connected to each other.

    The first node in the list is called the head,
    and the last node is called the tail.

    Initialise a linked list like so:

    >>> ll = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> assert ll.head.value == 1
    >>> assert ll.tail.value == 9
    """

    def __init__(self, *nums):
        """
        Initialise a linked list.

        :param nums: The values to initialise the linked list with.

        :return: None
        """

        # Unpack the first value and the rest of the values
        first, *rest = nums

        # Set the head to the first value
        self.head = Node(first)

        # Set the current node to the head
        current = self.head

        # Loop through the rest of the values
        for num in rest:
            # Set the current node's reference to a new node with the current value
            current.ref = Node(num)

            # Set the current node to the new node
            current = current.ref

        # Set the tail to the current node
        self.tail = current

    def get(self, value):
        """
        Get a node in the linked list.

        :param value: The value of the node to get.

        :return: The node with the given value. None if the node does not exist.
        """
        current = self.head

        while current.ref is not None:

            if current.value == value:
                return current

            current = current.ref


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
