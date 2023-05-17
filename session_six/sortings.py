from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar, MutableSequence, Callable


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...


CT = TypeVar("CT", bound=Comparable)
Predicate = Callable[[CT, Any], bool]


def merge_sort(arr: MutableSequence[CT]) -> MutableSequence[CT]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(lhs := arr[:mid])
    right = merge_sort(rhs := arr[mid:])
    print(lhs, rhs)
    return merge(left, right)


def merge(
    left: MutableSequence[CT],
    right: MutableSequence[CT],
    cmp: Predicate = lambda x, y: x < y,
) -> MutableSequence[CT]:
    result = []
    while len(left) and len(right):
        if cmp(left[0], right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
