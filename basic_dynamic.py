import sys

def basicDynamicMethod(weights, values, cap):

    # This is required to make the formula in the for loops to work
    weights.insert(0,0)
    values.insert(0,0)
    m = cap+1
    n = len(values)
    val = 0

    # initalize table
    dynProgTable = [[-1] * m for i in range(n)]


    # populate dynamic programing table with the max values at each stage
    for j in range(m):
        for i in range(n):
            if(i == 0 or j == 0):
                dynProgTable[i][j] = 0
            else:
                if(j-weights[i] >= 0):
                    dynProgTable[i][j] = max(dynProgTable[i-1][j] , values[i] + dynProgTable[i-1][j-weights[i] ] )
                else:
                    dynProgTable[i][j] = dynProgTable[i-1][j]
            val = dynProgTable[i][j]

    ## backtrace portion ##

    optimalSubset = []

    x = n - 1 # our items
    y = m - 1 # our capacity

    while(x>0 and y>0):
        current = dynProgTable[x][y]
        previous = dynProgTable[x-1][y]
        if(current > previous):
            optimalSubset.append(x)
            y = y - weights[x]
            x = x - 1
        else:
            x = x - 1

    # print("Optimal subset is: ", optimalSubset)
    optimalSubset.sort()
    weights.pop(0)
    values.pop(0)
    #size = sys.getsizeof(dynProgTable)
    return optimalSubset, val, m*n
