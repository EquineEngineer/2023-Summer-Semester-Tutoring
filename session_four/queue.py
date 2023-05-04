from __future__ import annotations


class Queue:
    """
    Queue is FIFO

    Implement by next time
    """

    def __init__(self, *values):
        """
        Example init:

        queue = Queue(1, 2, 3, 4)
        """

        self.values = values

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


def test() -> int:
    queue = Queue(1, 2, 3, 4, 5)

    # Adding item
    queue.enqueue(6)

    print(f"{queue = !r}")

    # Removing item
    six = queue.dequeue()

    print(f"Removed item: {six}")

    print(f"{queue = !r}")

    # Iterating (Implement `__iter__`!)

    for element in queue:
        print(f"Current item: {element}")

    return 0


if __name__ == "__main__":
    raise SystemExit(test())
