import math
import time


def basicDynamicMethod(weights, values, cap):

    # This is required to make the formula in the for loops to work
    weights.insert(0,0)
    values.insert(0,0)
    m = cap+1
    n = len(values)

    # initalize table
    dynProgTable = [[-1] * m for i in range(n)]

    # populate dynamic programing table with the max values at each stage
    start = time.time()
    for j in range(m):
        for i in range(n):
            if(i == 0 or j == 0):
                dynProgTable[i][j] = 0
            else:
                if(j-weights[i] >= 0):
                    dynProgTable[i][j] = max(dynProgTable[i-1][j] , values[i] + dynProgTable[i-1][j-weights[i] ] )
                else:
                    dynProgTable[i][j] = dynProgTable[i-1][j]
    end = time.time()
    print("Time taken to build the table with basic dynamic programing approach: %.5f" % end - start)

    ## backtrace portion ##

    optimalSubset = []

    x = n-1 # our items
    y = m-1 # our capacity

    start = time.time()
    while(x>0 or y>0):
        current = dynProgTable[x][y]
        previous = dynProgTable[x-1][y]
        if(current > previous):
            optimalSubset.append(x)
            y = y - weights[x]
            x = x - 1
        else:
            x = x - 1
    end = time.time()

    print("Time taken to backtrace with basic dynamic programing approach: %.5f" % end-start)
    print("Optimal subset is: ", optimalSubset)
