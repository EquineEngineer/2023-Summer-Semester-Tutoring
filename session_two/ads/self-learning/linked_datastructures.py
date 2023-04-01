from abc import ABC, abstractmethod

from abstract_datastructures import AbstractList


class LinkedList(AbstractList):

    """
    A linked list is a list implementation in which each node is linked to the next one.
    A node contains an element (anything) and points to the next node (an instance of LLNode)
    """

    class LLNode:
        """
        A class representing the Node of a Linked List
        """

        def __init__(element):
            self.value = element
            self.next = None

    def __init__():
        super().__init__()


class DoubleLinkedList(AbstractList):

    """
    A linked list is a list implementation in which each node is linked to the next and previous nodes.
    A node contains an element (anything) and points to the next and previous nodes (instances of DLLNode)
    """

    class DLLNode:
        def __init__(element):
            self.value = element
            self.next = None
            self.prev = None

    def to_string_reversed(self):
        """
        This method prints the content of the list in reverse order, thus, from the last to the
        first element. So if the list contains 3, foo, and 1.0, this method returns a string like this "1.0,foo,3"
        """
        pass


class CircularLinkedList(LinkedList):
    """
    A circular list is made of nodes linked as in the LinkedList, with the difference that
    the last LLNode is always attached to the head LLNode
    """

    pass
