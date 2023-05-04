# Sanity Check [ OK ]

# Algorithms & Data Structures

## Big-O Notation

Big-O notation is a way of describing the performance of an algorithm. It is a way of describing how the runtime of an algorithm scales with respect to the size of the input in the worst case scenario, as the size of the input grows arbitrarily large.

Examples: [Session one](../session_one/notes.md#complexity-analysis)

## Linked List

A linked list is a data structure that consists of a sequence of nodes. Each node contains a value and a reference to the next node in the sequence. The first node in the sequence is called the head and the last node is called the tail. The tail node's next reference is null.

### Interface

```
    add(value): None - adds a node with the given value to the end of the list
    find(value): Node - returns the first node with the given value
```

Find implementation [here](./linked_list.py).

## Stack

A stack is a data structure that consists of a sequence of values. It is a LIFO (last in, first out) data structure. The last value added to the stack is the first value removed from the stack.

### Interface

```
    push(value): None - adds a value to the top of the stack
    pop(): value - removes and returns the value at the top of the stack
    peek(): value - returns the value at the top of the stack without removing it
```

Find implementation [here](./stack.py).

## Queue

A queue is a data structure that consists of a sequence of values. It is a FIFO (first in, first out) data structure. The first value added to the queue is the first value removed from the queue.

### Interface

```
    enqueue(value): None - adds a value to the end of the queue
    dequeue(): value - removes and returns the value at the front of the queue
```

Find implementation [here](./queue.py).


## Exercises

### Stack

Navigate to the [Stack implementation](./stack.py#47) and implement the `__iter__` method.

### Queue

Navigate to the [Queue implementation](./queue.py#47) and implement the missing methods.