import time
import matplotlib.pyplot as plt
import greedy
import dynamic
import math
import basic_dynamic


def graphDynamic(time1a, time1b, space1a, space1b):
    label1 = "Traditional Dynamic"
    label2 = "Space-efficient Dynamic"
    title = "Dynamic Approach Comparison"
    plt.title(title)

    plt.xlabel("Space Taken")
    plt.ylabel("Time Taken (ns)")
    plt.loglog(space1a, time1a, 'o', label=label1)
    plt.loglog(space1b, time1b, 'o', label=label2)
    plt.legend()
    plt.show()


def graphGreedy(noItems, items2a, items2b):
    label1 = "in-built sort"
    label2 = "max-heap"
    ax = plt.axes()
    title = "Greedy Approach Comparison"
    plt.title(title)

    maxX = max(noItems) + 1
    maxY = max(max(items2a), max(items2b)) + 1

    ax.set(xlim=(0, maxX), ylim=(0, maxY))
    ax.plot(noItems, items2a, 'o', label=label1)
    ax.plot(noItems, items2b, 'o', label=label2)

    plt.legend()
    plt.xlabel("No. Items")
    plt.ylabel("Time Taken (ns)")
    plt.show()


def graph():
    listNoItems = []
    listtimes1A = []
    listtimes1B = []
    listSpace1A = []
    listSpace1B = []
    listTimes2A = []
    listTimes2B = []

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

        # This will shrink the data input considerably.
        # We lose a little precision, but gain a lot of speed
        for i in range(len(weight)):
           string = weight[i].strip()
           integer = int(string, 10)
           weight[i] = integer

        smallLen = len(str(min(weight)))

        if smallLen >= 4:
            valToDivide = (smallLen - 2) * 10
            cap /= valToDivide
            cap = math.ceil(cap)

            for i in range(len(weight)):
                weight[i] /= valToDivide
                weight[i] = math.ceil(weight[i])

        for i in range(len(values)):
            string = values[i].strip()
            integer = int(string, 10)
            values[i] = integer

        print(str(fileNo)+"     Running Task A1")

        listNoItems.append(len(values))
        start = time.perf_counter_ns()
        garbage, garbage, space = basic_dynamic.basicDynamicMethod(weight, values, cap)
        end = (time.perf_counter_ns() - start)
        listtimes1A.append(end)
        listSpace1A.append(space)

        print(str(fileNo) + "     Running Task A2")
        start = time.perf_counter_ns()
        garbage, garbage, space = dynamic.dynamicSort(cap, weight, values)
        end = (time.perf_counter_ns() - start)
        listtimes1B.append(end)
        listSpace1B.append(space)

        print(str(fileNo) + "     Running Task B1")
        start = time.perf_counter_ns()
        greedy.greedySort(cap, weight, values)
        end = (time.perf_counter_ns() - start)
        listTimes2A.append(end)

        print(str(fileNo) + "     Running Task B2")
        start = time.perf_counter_ns()
        greedy.greedyHeap(cap, weight, values)
        end = (time.perf_counter_ns() - start)
        listTimes2B.append(end)

    graphDynamic(listtimes1A, listtimes1B, listSpace1A, listSpace1B)
    graphGreedy(listNoItems, listTimes2A, listTimes2B)

def fileCheck(fn):
    try:
        open(fn, "r")
        return 1
    except IOError:
        print("Error: File not found.")
        return 0

def main():

    #Get user input
    print("All paths will be prefixed with 'knapsack/' !")
    print("Please have all your data files in a subfolder called 'knapsack'")
    print()

    capFileName = input("Enter file containing the capacity: ")
    result = fileCheck('knapsack/' + capFileName)
    if result == 0:
        while result == 0:
            capFileName = input("Enter file containing the capacity: ")
            result = fileCheck('knapsack/' + capFileName)

    weightFileName  = input("Enter file containing the weights: ")
    result = fileCheck('knapsack/' + weightFileName)
    if result == 0:
        while result == 0:
            weightFileName = input("Enter file containing the weights: ")
            result = fileCheck('knapsack/' + weightFileName)

    valuesFileName = input("Enter file containing the values: ")
    result = fileCheck('knapsack/' + valuesFileName)
    if result == 0:
        while result == 0:
            valuesFileName = input("Enter file containing the values: ")
            result = fileCheck('knapsack/' + valuesFileName)



    capFile = open('knapsack/' + capFileName, "r")
    weightFile = open('knapsack/' + weightFileName, "r")
    valuesFile = open('knapsack/' + valuesFileName, "r")

    cap = int(capFile.readline())
    weight = weightFile.readlines()
    values = valuesFile.readlines()

    # This will shrink the data input considerably.
    # We lose a little precision, but gain a lot of speed

    for i in range(len(weight)):
        string = weight[i].strip()
        integer = int(string, 10)
        weight[i] = integer

    oldCap = cap
    smallLen = len(str(min(weight)))

    if smallLen >= 4:
        valToDivide = (smallLen - 2) * 10
        cap /= valToDivide
        cap = math.ceil(cap)

        for i in range(len(weight)):
            weight[i] /= valToDivide
            weight[i] = math.ceil(weight[i])

    for i in range(len(values)):
        string = values[i].strip()
        integer = int(string, 10)
        values[i] = integer

    print()
    print('Knapsack capacity = ' + str(oldCap) + '. ', end='')
    print('Total number of items =', (len(values)))
    print()

    start = time.perf_counter_ns()
    subset, value, size = basic_dynamic.basicDynamicMethod(weight, values, cap)
    end = (time.perf_counter_ns() - start)


    print('Traditional Dynamic Programming Optimal value: ', value)
    print('Traditional Dynamic Programming Optimal subset: ', subset)
    print('Traditional Dynamic Programming Time Taken: ', end, 'ns')
    print()

    start = time.perf_counter_ns()
    subset, value, size = dynamic.dynamicSort(cap, weight, values)
    end = (time.perf_counter_ns() - start)
    time.perf_counter_ns()

    print('Space-efficient Dynamic Programming Optimal value: ', value)
    print('Space-efficient Dynamic Programming Optimal subset: ', subset)
    print('Space-efficient Dynamic Programming Time taken: ', end, 'ns')
    print()

    start = time.perf_counter_ns()
    subset, value = greedy.greedySort(cap, weight, values)
    end = (time.perf_counter_ns() - start)

    print('Greedy Approach Optimal value: ', value)
    print('Greedy Approach Optimal subset:', subset)
    print('Greedy Approach Time taken: ', end, 'ns')
    print()

    start = time.perf_counter_ns()
    subset, value = greedy.greedyHeap(cap, weight, values)
    end = (time.perf_counter_ns() - start)

    print('Heap-based Greedy Approach Optimal value: ', value)
    print('Heap-based Greedy Approach Optimal subset: ', subset)
    print('Heap-based Greedy Approach Time taken: ', end, 'ns')

    exitProg = False

    print("\n\n")
    while not exitProg:
        graphPrompt = input("Run graphs on all inputs? (Y/N): ")
        if graphPrompt == 'Y' or graphPrompt == 'y':
            graph()
        if graphPrompt == 'N' or graphPrompt == 'n':
            exitProg = True


main()
