from dynamic_array_datastructures import DynamicArrayList
from linked_datastructures import LinkedList, DoubleLinkedList, CircularLinkedList


def test_init_linked_list():
    ll = LinkedList()
    assert ll.size() == 0

def test_init_double_linked_list():
    dll = DoubleLinkedList()
    assert dll.size() == 0

def test_init_circular_linked_list():
    cll = CircularLinkedList()
    assert cll.size() == 0

def test_init_dynamic_array_list():
    dal = DynamicArrayList()
    assert dal.size() == 0
