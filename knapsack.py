import time
import timeit
from collections import namedtuple
import matplotlib.pyplot as plt

class maxHeap:
    def __init__(self, array=None):
        self._heap = []

        if array is not None:
            for i in array:
                self.insert(i)

    def insert(self, value):
        self._heap.append(value)
        _sift_up(self._heap, len(self) - 1)

    def pop(self):
        _swap(self._heap, len(self) - 1, 0)
        i = self._heap.pop()
        _siftDown(self._heap, 0)
        return i

    def __len__(self):
        return len(self._heap)

    def print(self, idx=1, indent=0):
        print("\t" * indent, f"{self._heap[idx - 1].ratio}")
        left, right = 2 * idx, 2 * idx + 1
        if left <= len(self):
            self.print(left, indent=indent + 1)
        if right <= len(self):
            self.print(right, indent=indent + 1)


def _swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def _sift_up(heap, idx):
    parent_idx = (idx - 1) // 2

    # Hit the root
    if parent_idx < 0:
        return

    # Check for swap
    if heap[idx].ratio > heap[parent_idx].ratio:
        _swap(heap, idx, parent_idx)
        _sift_up(heap, parent_idx)


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


def heap_sort(array):
    heap = maxHeap(array)
    sorted_arr = []

    while len(heap) > 0:
        sorted_arr.append(heap.pop())

    return sorted_arr

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

def graph(list1a, list1b, list2a, list2b):
    label1 = "in-built sort"
    label2 = "max-heap"
    ax = plt.axes()
    title = 'Greedy Approach Comparison: '
    plt.title(title)

    maxX = max(max(list1a), max(list2a)) + 1
    maxY = max(max(list1b), max(list2b)) + 1

    ax.set(xlim=(0, maxX), ylim=(0, maxY))
    ax.plot(list1a, list1b, 'o', label=label1)
    ax.plot(list2a, list2b, 'o', label=label2)

    plt.legend()
    plt.xlabel("No. Items")
    plt.ylabel("Time Taken (ms)")
    plt.show()


def main():
    value = 0
    subset = []

    # Get user input
    #capFileName = input("Enter file containing the capacity: ")
    #weightFileName  = input("Enter file containing the weights: ")
    #valuesFileName = input("Enter file containing the values: ")

    capFileName = "p07_c.txt"
    weightFileName = "p07_w.txt"
    valuesFileName = "p07_v.txt"

    capFile = open('knapsack/' + capFileName, "r")
    weightFile = open('knapsack/' + weightFileName, "r")
    valuesFile = open('knapsack/' + valuesFileName, "r")

    cap = int(capFile.readline())
    weight = weightFile.readlines()
    values = valuesFile.readlines()

    for i in range(len(weight)):
        string = weight[i].strip()
        integer = int(string, 10)
        weight[i] = integer

    for i in range(len(values)):
        string = values[i].strip()
        integer = int(string, 10)
        values[i] = integer

    k = 1000000 #Time to milliseconds

    print()
    print('Knapsack capacity =', cap, '.', end=' ')
    print('Total number of items =', (len(values)))
    print()

    # Everything from here down just prints, nothing else for now.

    #print('Traditional Dynamic Programming Optimal value: ')
    #print('Traditional Dynamic Programming Optimal subset: ')
    #print('Traditional Dynamic Programming Time Taken: ')

    #print('Space-efficient Dynamic Programming Optimal value: ')
    #print('Space-efficient Dynamic Programming Optimal subset: ')
    #print('Space-efficient Dynamic Programming Time taken: ')

    start = timeit.default_timer()
    subset, value = greedySort(cap, weight, values)
    end = (timeit.default_timer() - start) * k

    print('Greedy Approach Optimal value: ', value)
    print('Greedy Approach Optimal subset:', subset)
    print('Greedy Approach Time taken: ', end, 'ms')

    print()

    # print('Traditional Dynamic Programming Optimal value: ')
    # print('Traditional Dynamic Programming Optimal subset: ')
    # print('Traditional Dynamic Programming Time Taken: ')


    start = timeit.default_timer()
    subset, value = greedyHeap(cap, weight, values)
    end = (timeit.default_timer() - start) * k

    print()

    print('Heap-based Greedy Approach Optimal value: ', value)
    print('Heap-based Greedy Approach Optimal subset: ', subset)
    print('Heap-based Greedy Approach Time taken: ', end, 'ms')

    #Do some graphing

    listNoItemsA = []
    listTimesA = []
    listNoItemsB = []
    listTimesB = []
    for fileNo in range(9):

        capFileName = "p0"+str(fileNo)+"_c.txt"
        weightFileName = "p0"+str(fileNo)+"_w.txt"
        valuesFileName = "p0"+str(fileNo)+"_v.txt"

        capFile = open('knapsack/' + capFileName, "r")
        weightFile = open('knapsack/' + weightFileName, "r")
        valuesFile = open('knapsack/' + valuesFileName, "r")

        cap = int(capFile.readline())
        weight = weightFile.readlines()
        values = valuesFile.readlines()

        for i in range(len(weight)):
            string = weight[i].strip()
            integer = int(string, 10)
            weight[i] = integer

        for i in range(len(values)):
            string = values[i].strip()
            integer = int(string, 10)
            values[i] = integer



        listNoItemsA.append(len(values))
        start = timeit.default_timer()
        greedySort(cap, weight, values)
        end = (timeit.default_timer() - start) * k
        listTimesA.append(end)

        listNoItemsB.append(len(values))
        start = timeit.default_timer()
        greedyHeap(cap, weight, values)
        end = (timeit.default_timer() - start) * k
        listTimesB.append(end)

    graph(listNoItemsA, listTimesA, listNoItemsB, listTimesB)

main()
