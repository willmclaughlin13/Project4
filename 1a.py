def max(a,b):
    return a if a>b else b

capFileName = "p01_c.txt"
weightFileName = "p01_w.txt"
valuesFileName = "p01_v.txt"

capFile = open('knapsack/' + capFileName, "r")
weightFile = open('knapsack/' + weightFileName, "r")
valuesFile = open('knapsack/' + valuesFileName, "r")

cap = int(capFile.readline())       # I'm making this an int, then back to str so it prints on one line...

weights = weightFile.readlines()
for i in range(len(weights)):
    string = weights[i].strip()
    integer = int(string, 10)
    weights[i] = integer

values = valuesFile.readlines()
for i in range(len(values)):
    string = values[i].strip()
    integer = int(string, 10)
    values[i] = integer

# This is required to make the formula in the for loops to work
weights.insert(0,0)
values.insert(0,0)
m = cap+1
n = len(values)

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

## backtrace portion ##

optimalSubset = []

x = n-1 # our items
y = m-1 # our capacity

while(x>0 or y>0):
    current = dynProgTable[x][y]
    previous = dynProgTable[x-1][y]
    if(current > previous):
        optimalSubset.append(x)
        y = y - weights[x]
        x = x - 1
    else:
        x = x - 1

print("Optimal subset is: ", optimalSubset)
