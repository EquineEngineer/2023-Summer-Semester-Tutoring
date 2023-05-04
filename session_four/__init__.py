from __future__ import annotations


# Generators + Data Structures

# Linked Lists (Single OR Double)
# Queue
# Stack

# Bonus: !Hashmap

# !Big O is an estimate (for the number of primitive operations) of the worst-case scenario
# 1 + 1 (Simple maths operations are atomic)
# Ex.
#           0   1   2
# array = [ 1 | 2 | 3 | 4 | 5 | 6 ]
# array[2] : 3
#
#
# Assume each integer takes 32 bits of memory
# Address array[0]: 0x0c3234a33b
# Address of array[0 + n]: array[0] + n * 32bits
#
# Big O = 1 (Constant complexity) O(1)
# Translates similar to:
#   The function that accesses an array, grows as much as y = 1
#
# For-loops mean: multiply by n

# [HEAD] -> [ Value | Next* ] -> [ Value | Next* ] -> [ Value | None ]
# llist = LinkedList(1, 2, 3, 4, 5, 6)
# Big O Accessing an element in a LinkedList (get third value):
# A for loops that goes on n times, gives us
#
# Big O accessing an element in a linkedlist = N
# O(N)

# Array: Arrays are indexed (they use index [think 1, 2, 3 ...]),
# Arrays are also contiguous in memory


class Queue:
    """
    Queue is FIFO

    Implement by next time
    """

    def enqueue(self, value):
        """
        Add `value` to the queue
        """

        raise NotImplementedError(
            f"Implement `enqueue` for {self.__class__.__qualname__}"
        )

    def dequeue(self):
        """
        Removes first element from the Queue
        """

        raise NotImplementedError(
            f"Implement `dequeue` for {self.__class__.__qualname__}"
        )

    def __repr__(self):
        """
        String representation of a Queue
        """

        raise NotImplementedError(
            f"Implement `__repr__` for {self.__class__.__qualname__}"
        )

    def __iter__(self):
        """
        Implement __iter__
        """

        raise NotImplementedError(
            f"Implement `__iter__` for {self.__class__.__qualname__}"
        )


"""
Which one is nicer?

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)

ll.find(2)  : return Node(2, <...>)

OR

ll = LinkedList(1, 2, 3)

for element in [...]

for element in (...)

for element in {...}

"""


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
