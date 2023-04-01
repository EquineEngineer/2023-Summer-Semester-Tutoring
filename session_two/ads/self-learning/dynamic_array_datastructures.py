from abc import ABC, abstractmethod

from abstract_datastructures import AbstractList

from array import array

from typing import List

# The maximum (initial) size of the array list
MAX_SIZE_QUOTA = 5


"""

Arrays are fixed-size
[ int ; 7 ] (7 is size)
[ 1, 2, 3, 4, 5, 6, 7 ]


Arraylists are dynamic-size
[ int ; 7 ] (7 is initial capacity) [ | | | | | | | ]

... (Imagine I add 8 elements) 
[ 1, 2, 3, 4, 5, 6, 7 ]

copy the list ([ <numbers> ]) into a new space of greater capacity

[ int ; 10 ] (10 is initial capacity) [ | | | | | | | | | |]

[ 1, 2, 3, 4, 5, 6, 7, 8, NONE, NONE ]

[ ; 8 ]

[ ; 16 ]

[ ; 32 ]

mypy, pyright
lsp from vscode or pycharm

"""


class Array:
    def __init__(self, capacity):
        self.mem = bytearray([0] * capacity)


class DynamicArrayList(AbstractList):

    """
    An dynamic array list is a list implementation backed up by an array.
    When the number of elements that the list contains is larger than the size of the array,
    the list must grow the array by MAX_SIZE_QUOTA. So, initially the MAX_SIZE = 5, then it becomes 10, next 15.
    However, if the number of elements is BELOW the size of the array minus MAX_SIZE_QUOTA,
    the list must shrink the array by MAX_SIZE_QUOTA.
    """

    def __init__(self):
        super().__init__()
        self.array = []
        # self.mem = array("i", [0, 0, 0, 0, 0])  c-style
        self.capacity = MAX_SIZE_QUOTA

    def size(self):
        return len(self.array)

    def insert_element(self, element, position):
        if self.size() >= self.capacity:
            # calculate new capacity
            self.capacity += MAX_SIZE_QUOTA

            # create new buffer & copy elements into buffer
            buffer = [element for element in self.array]

            # alternatives:
            # for loop
            # unpacking
            # while loop
            # deepcopy
            # shallow copy
            # a binary mem copy
            # a file write
            # a mem swap

            # assign buffer to underlying array
            self.array = buffer

        # Insert `element` at `position`
        self.array.insert(position, element)


if __name__ == "__main__":
    dal = DynamicArrayList()
    print(dal)
