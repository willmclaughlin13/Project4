def main():

    # Get user input
    #capFileName = input("Enter file containing the capacity: ")
    #weightFileName  = input("Enter file containing the weights: ")
    #valuesFileName = input("Enter file containing the values: ")

    capFileName = "p01_c.txt"
    weightFileName = "p01_w.txt"
    valuesFileName = "p01_v.txt"

    capFile = open('knapsack/' + capFileName, "r")
    weightFile = open('knapsack/' + weightFileName, "r")
    valuesFile = open('knapsack/' + valuesFileName, "r")

    cap = int(capFile.readline())       # I'm making this an int, then back to str so it prints on one line...
    weight = weightFile.readlines()
    values = valuesFile.readlines()

    print('Knapsack capacity = ' + str(cap) + '.', end=' ')
    print('Total number of items = ' + str(len(values)))

    # Everything from here down just prints, nothing else for now.

    print('Traditional Dynamic Programming Optimal value: ')
    print('Traditional Dynamic Programming Optimal subset: ')
    print('Traditional Dynamic Programming Time Taken: ')

    print('Space-efficient Dynamic Programming Optimal value: ')
    print('Space-efficient Dynamic Programming Optimal subset: ')
    print('Space-efficient Dynamic Programming Time taken: ')

    print('Greedy Approach Optimal value: ')
    print('Greedy Approach Optimal subset: ')
    print('Greedy Approach Time taken: ')

    print('Heap-based Greedy Approach Optimal value: ')
    print('Heap-based Greedy Approach Optimal subset: ')
    print('Heap-based Greedy Approach Time taken: ')

    #Do some graphing


main()
