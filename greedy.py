from collections import namedtuple


# This is our heap class
class maxHeap:
    def __init__(self, array=None):
        self._heap = []

        if array is not None:  # The constructor, builds the heap from a list
            for i in array:
                self.insert(i)

    # Insert takes value to insert as input, appends it to the array, then
    # calls sift up to find it's place in the heap
    def insert(self, value):
        self._heap.append(value)
        _sift_up(self._heap, len(self) - 1)

    # Pop removes and returns the maximum value at the root
    def pop(self):
        _swap(self._heap, len(self) - 1, 0)
        i = self._heap.pop()
        _siftDown(self._heap, 0)
        return i

    def __len__(self):
        return len(self._heap)


# Swap the two values in the list
def _swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# Find the new value's place in the heap
def _sift_up(heap, idx):
    parent_idx = (idx - 1) // 2

    # Hit the root
    if parent_idx < 0:
        return

    # Check for swap
    if heap[idx].ratio > heap[parent_idx].ratio:
        _swap(heap, idx, parent_idx)
        _sift_up(heap, parent_idx)


# After removing the root, find a new one and sift up
def _siftDown(heap, idx):
    child_idx = 2 * idx + 1

    if child_idx >= len(heap):
        return

    # Hit the root
    if child_idx + 1 < len(heap) and heap[child_idx].ratio < heap[child_idx + 1].ratio:
        child_idx += 1

    # Check for swap
    if heap[child_idx].ratio > heap[idx].ratio:
        _swap(heap, child_idx, idx)
        _siftDown(heap, child_idx)


# takes an array as input, turns it into a heap,
# and returns the sorted values as a list.
def heap_sort(array):
    heap = maxHeap(array)
    sorted_arr = []

    while len(heap) > 0:
        sorted_arr.append(heap.pop())

    return sorted_arr


# Knapsack algorithm using the built-in list
def greedySort(cap, weight, values):
    ratios = []
    subset = []

    for i in range(len(values)):
        ratios.append(values[i]/weight[i])
        subset.append(i+1)

    ratios, values, weight, subset = (list(t) for t in zip(*sorted(zip(ratios, values, weight, subset), reverse=True)))

    finalSubset = []
    totalWeight = 0
    totalValue = 0

    for i in range(len(values)):

        if totalWeight + weight[i] >= cap:
            finalSubset.sort()
            return finalSubset, totalValue
        else:
            finalSubset.append(subset[i])
            totalWeight += weight[i]
            totalValue += values[i]


# Knapsack algorithm using our heap class
def greedyHeap(cap, weight, values):
    myHeap = namedtuple("myHeap", "weight value idx ratio")
    items = []
    ratios = []

    for i in range(len(values)):
        ratios.append(values[i]/weight[i])

    for i in range(len(values)):
        m = myHeap(weight=weight[i], value=values[i], idx=i+1, ratio=ratios[i])
        items.append(m)

    items = heap_sort(items)

    finalSubset = []
    totalWeight = 0
    totalValue = 0

    for i in items:

        if totalWeight + i.weight >= cap:
            finalSubset.sort()
            return finalSubset, totalValue
        else:
            finalSubset.append(i.idx)
            totalWeight += i.weight
            totalValue += i.value