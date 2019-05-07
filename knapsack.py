import time
import matplotlib.pyplot as plt
import greedy
import dynamic

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
    plt.ylabel("Time Taken (ns)")
    plt.show()


def main():

    # Get user input
    #capFileName = input("Enter file containing the capacity: ")
    #weightFileName  = input("Enter file containing the weights: ")
    #valuesFileName = input("Enter file containing the values: ")

    capFileName = "p10_c.txt"
    weightFileName = "p10_w.txt"
    valuesFileName = "p10_v.txt"

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
    start = time.perf_counter_ns()
    subset, value = greedy.greedySort(cap, weight, values)
    end = (time.perf_counter_ns() - start)

    print('Greedy Approach Optimal value: ', value)
    print('Greedy Approach Optimal subset:', subset)
    print('Greedy Approach Time taken: ', end, 'ns')

    print()

    # print('Traditional Dynamic Programming Optimal value: ')
    # print('Traditional Dynamic Programming Optimal subset: ')
    # print('Traditional Dynamic Programming Time Taken: ')


    start = time.perf_counter_ns()
    subset, value = greedy.greedyHeap(cap, weight, values)
    end = (time.perf_counter_ns() - start)

    print()

    print('Heap-based Greedy Approach Optimal value: ', value)
    print('Heap-based Greedy Approach Optimal subset: ', subset)
    print('Heap-based Greedy Approach Time taken: ', end, 'ns')

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
        start = time.perf_counter_ns()
        greedy.greedySort(cap, weight, values)
        end = (time.perf_counter_ns() - start)
        listTimesA.append(end)

        listNoItemsB.append(len(values))
        start = time.perf_counter_ns()
        greedy.greedyHeap(cap, weight, values)
        end = (time.perf_counter_ns() - start)
        listTimesB.append(end)

    graph(listNoItemsA, listTimesA, listNoItemsB, listTimesB)

main()
