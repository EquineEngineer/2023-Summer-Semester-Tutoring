from __future__ import annotations


class Stack:
    """
    Stack is FILO
    """

    def __init__(self, *values):
        """
        Example init:

        stack = Stack(1, 2, 3, 4, 5)
        """
        self.values = values

    def push(self, value):
        """

        Add element at the end
        """
        # (1, 2, 3)     1, 2, 3, value
        self.values = (*self.values, value)

    def pop(self):
        """

        Remove last element and return it
        """

        *rest, last = self.values
        self.values = rest
        return last

    def peek(self):
        """

        Return last element without removing it
        """
        *_, last = self.values

        return last

    def __repr__(self):
        return "Stack [ " + ", ".join(str(val) for val in self.values) + " ]"

    def __iter__(self):
        """
        Implement __iter__
        """
        raise NotImplementedError(
            f"Implement `__iter__()` for {self.__class__.__qualname__}"
        )


def test() -> int:
    stack = Stack(1, 2, 3)

    # Adding item
    stack.push(4)

    print(f"{stack = !r}")

    # Removing item
    four = stack.pop()

    print(f"Removed item: {four}")

    print(f"{stack = !r}")

    # Peek last item

    three = stack.peek()

    print(f"Peeking at {three}")

    print(f"{stack = !r}")

    # Iterating (Implement `__iter__`!)

    for element in stack:
        print(f"Current item: {element}")

    return 0


if __name__ == "__main__":
    raise SystemExit(test())
