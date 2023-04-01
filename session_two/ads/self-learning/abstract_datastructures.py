from abc import ABC, abstractmethod


class AbstractList(ABC):
    """
    This abstract class defines the interface of any implementation of a List
    """

    def __init__(self):
        """
        A list has always an head
        """
        self.head = None

    @abstractmethod
    def size(self):
        """
        Return the size of the list, i.e., the number of elements contained in it
        """
        ...

    @abstractmethod
    def insert_element(self, element, position):
        """
        Insert the element in the list at the given position.
        Position 0 means that the element must be inserted at the beginning.
        Position self.size() means that the element must be added as last
        """
        pass

    @abstractmethod
    def delete_element(self, element, position):
        """
        Delete the element of the list at the given position.
        Position 0 means that the first element must be removed.
        Position self.size() - 1 means that the last element must be removed.
        Elements from an empty list cannot be removed (expected behavior, do nothing!)
        """
        pass

    @abstractmethod
    def to_string(self):
        """
        Returns a string that contains all the elements separated by commas, without spaces
        If the list contains the values 3, foo, -1.0 this methods returns "3,foo,-1.0"
        If the list contains only value bar this methods returns the string "bar"
        """
        pass

    @abstractmethod
    def contains(self, element):
        """
        Returns True if the list contains the element, False otherwise.
        """
        pass
