import math

N = 0
W = 0
K = 0
WEIGHTS = []
VALUES = []
FINAL_IDX = []


class Node(object):

    def __init__(self, data=None, next_node=None, i=None, j=None):
        self.data = data
        self.next_node = next_node
        self.i = i
        self.j = j

    def get_data(self):
        return self.data

    def get_i(self):
        return self.i

    def get_j(self):
        return self.j

    def get_next(self):
        return self.next_node

    def set_i(self, new_data):
        self.i = new_data

    def set_j(self, new_data):
        self.j = new_data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data, i, j):
        new_node = Node(data)
        new_node.set_i(i)
        new_node.set_j(j)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next_node:
            last = last.next_node
        last.next_node = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def searchData(self, i, j):
        current = self.head
        found = False
        while current and found is False:
            if current.get_i() == i and current.get_j() == j:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def printHash(self):
        current = self.head
        count = 0
        while current is not None:

            if count % (N+1) == 0:
                print()
            count += 1

            print(current.get_data(), end=' ')
            current = current.get_next()


hash_table = []


def MFKnapsack(i, j):
    if i < 0:
        return 0
    hash_val = myHash(i, j)

    currentNode = hash_table[hash_val].searchData(i, j)

    if currentNode.get_data() < 0:
        if j < WEIGHTS[i]:
            value = MFKnapsack(i - 1, j)
        else:
            value = max(MFKnapsack(i - 1, j),
                        VALUES[i] + MFKnapsack(i - 1, j - WEIGHTS[i]))

        currentNode.set_data(value)
    return currentNode.get_data()


def getSubset(i, j):

    if i == 0:
        FINAL_IDX.append(i+1)
        return

    if i < 1:
        return

    hash_val = myHash(i, j)
    hash_valAbove = myHash(i-1, j)

    currentNode = hash_table[hash_val].searchData(i, j)
    nextNode = hash_table[hash_valAbove].searchData(i-1, j)

    if currentNode.get_data() > nextNode.get_data():
        FINAL_IDX.append(i+1)
        getSubset(i, j - WEIGHTS[i])
    else:
        getSubset(i-1, j)


def dec_to_bin(x):
    return '{:04b}'.format(x)


def hashInsert(i, j, val):
    hash_key = myHash(i, j)
    global hash_table
    if hash_table[hash_key] is None:
        newList = LinkedList()
        hash_table[hash_key] = newList
        hash_table[hash_key].insert(val, i, j)
    else:
        hash_table[hash_key].insert(val, i, j)


def insertZeros(rI, rJ, lenA, lenB):
    rI = rI[::-1]
    rJ = rJ[::-1]

    rIZeros = lenA - len(rI)
    rJZeros = lenB - len(rJ)
    if rIZeros < 0:
        rIZeros = 0
    if rJZeros < 0:
        rJZeros = 0

    for i in range(rIZeros):
        rI += '0'

    for i in range(rJZeros):
        rJ += '0'

    rI = rI[::-1]
    rJ = rJ[::-1]

    return rI, rJ


def myHash(i, j):
    bN = math.log(N+1, 2)
    bW = math.log(W+1, 2)
    bN = math.ceil(bN)
    bW = math.ceil(bW)

    rI = str(dec_to_bin(i))
    rJ = str(dec_to_bin(j))

    rI, rJ = insertZeros(rI, rJ, bN, bW)
    rIJ = [1]

    for i in range(len(rI)):
        rIJ.append(int(rI[i]))
    for i in range(len(rJ)):
        rIJ.append(int(rJ[i]))

    s = ''.join(map(str, rIJ))
    rIJ = int(s, 2)
    # print("rIJ: ", rIJ)
    # print("K: ", K)
    # print(rIJ % K)
    # print()
    return rIJ % K


def unique(list1):
    uniqueList = []

    for i in list1:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList


def dynamicSort(cap, weight, values):
    global N
    N = cap
    global W
    W = len(values)
    global WEIGHTS
    WEIGHTS = weight
    global VALUES
    VALUES = values
    global K
    K = int(W/2)
    global hash_table
    hash_table = [None] * K
    global FINAL_IDX


    for i in range(len(values)):
        for j in range(cap + 1):
            if j == 0:
                hashInsert(i, j, 0)
            else:
                hashInsert(i, j, -1)


    retVal = MFKnapsack(len(values) - 1, cap)
    getSubset(len(values) - 1, cap)
    FINAL_IDX = FINAL_IDX[::-1]

    # for i in hash_table:
    #     if i is not None:
    #         i.printHash()

    FINAL_IDX = unique(FINAL_IDX)

    sum = 0
    for i in FINAL_IDX:
        sum += values[i-1]

    print(FINAL_IDX)
    print(retVal)
    if retVal == sum:
        print("OPTIMAL!")
    else:
        print("NOT OPTIMAL!!")
    return FINAL_IDX, retVal
