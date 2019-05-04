import time

def greedySort(cap, weight, values):
    ratios = []
    subset = []

    for i in range(len(values)):
        ratios.append(int(values[i])/int(weight[i]))
        subset.append(i+1)

    ratios, values, weight, subset = (list(t) for t in zip(*sorted(zip(ratios, values, weight, subset), reverse=True)))

    finalSubset = []
    totalWeight = 0
    totalValue = 0

    for i in range(len(values)):

        if totalWeight + int(weight[i]) >= int(cap):
            finalSubset.sort()
            return finalSubset, totalValue
        else:
            finalSubset.append(subset[i])
            totalWeight += int(weight[i])
            totalValue += int(values[i])




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

    cap = int(capFile.readline())       # I'm making this an int, then back to str so it prints on one line...
    weight = weightFile.readlines()
    values = valuesFile.readlines()

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

    start = time.time_ns()
    subset, value = greedySort(cap, weight, values)
    end = time.time_ns() - start

    print('Greedy Approach Optimal value: ', value)
    print('Greedy Approach Optimal subset:', subset)
    print('Greedy Approach Time taken: ', end, 'ns')

    #print('Heap-based Greedy Approach Optimal value: ')
    #print('Heap-based Greedy Approach Optimal subset: ')
    #print('Heap-based Greedy Approach Time taken: ')

    #Do some graphing


main()
