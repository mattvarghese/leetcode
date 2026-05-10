from p__006_min_heap import MinHeap


def test_empty_heap():
    heap = MinHeap()
    assert heap.pop() is None


def test_single_element():
    heap = MinHeap()
    heap.push(10)
    assert heap.pop() == 10
    assert heap.pop() is None


def test_min_property_basic():
    heap = MinHeap()
    vals = [5, 3, 8, 1]
    for v in vals:
        heap.push(v)

    assert heap.pop() == 1
    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 8


def test_duplicate_elements():
    heap = MinHeap()
    vals = [10, 5, 10, 2, 5]
    for v in vals:
        heap.push(v)

    results = []
    while True:
        val = heap.pop()
        if val is None:
            break
        results.append(val)

    assert results == [2, 5, 5, 10, 10]


def test_large_random_sequence():
    import random

    heap = MinHeap()
    data = list(range(100))
    random.shuffle(data)

    for x in data:
        heap.push(x)

    results = []
    for _ in range(100):
        results.append(heap.pop())

    assert results == sorted(data)


def test_descending_order_input():
    heap = MinHeap()
    for i in range(10, 0, -1):
        heap.push(i)

    assert heap.pop() == 1
    assert heap.pop() == 2


def test_ascending_order_input():
    heap = MinHeap()
    for i in range(1, 11):
        heap.push(i)

    assert heap.pop() == 1
    assert heap.pop() == 2
