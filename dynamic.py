import math

F = [[]]
N = 0
W = 0
K = 0
WEIGHTS = []
VALUES = []

class Node(object):

    def __init__(self, data=None, next_node=None, key=None):
        self.data = data
        self.next_node = next_node
        self.key = key

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_key(self):
        return self.key

    def set_data(self, new_data):
        self.data = new_data

    def set_key(self, new_key):
        self.key = new_key

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data, key):
        new_node = Node(data)
        new_node.set_key(key)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def searchData(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def searchKey(self, key):
        current = self.head
        found = False
        while current and found is False:
            if current.get_key() == key:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Key not in list")
        return current

    def setZeros(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if count % N == 0:
                current.set_data(0)

            current = current.get_next()

    def printHash(self):
        current = self.head
        count = 0
        while current is not None:
            if count % (N+1) == 0:
                print()
            print(current.get_data(), end=' ')
            current = current.get_next()
            count += 1
        print()
        print()



hash_table = LinkedList()


def MFKnapsack(i, j):
    if i < 0:
        return 0
    hash_val = myHash(i, j)

    if hash_table.searchKey(hash_val).get_data() < 0:
        if j < WEIGHTS[i]:
            value = MFKnapsack(i - 1, j)
        else:
            value = max(MFKnapsack(i - 1, j),
                        VALUES[i] + MFKnapsack(i - 1, j - WEIGHTS[i]))

        hash_table.searchKey(hash_val).set_data(value)
    return hash_table.searchKey(hash_val).get_data()


def MFKnapsack2(i, j):
    if i < 0:
        return 0
    if F[i][j] < 0:
        if j < WEIGHTS[i]:
            value = MFKnapsack2(i - 1, j)
        else:
            value = max(MFKnapsack2(i - 1, j),
                        VALUES[i] + MFKnapsack2(i - 1, j - WEIGHTS[i]))
        F[i][j] = value
    return F[i][j]


def dec_to_bin(x):
    return '{:04b}'.format(x)


def hashInsert(i, j, val):
    hash_key = myHash(i, j)
    global hash_table
    hash_table.insert(val, hash_key)


def myHash(i, j):
    bN = math.log(N+1, 2)
    bW = math.log(W+1, 2)
    bN = math.ceil(bN)
    bW = math.ceil(bW) # Use these two values + 1 for total length of binary string?

    rI = dec_to_bin(i)
    rJ = dec_to_bin(j)

    rIJ = [1]

    # Figure out what the padding deal is...

    for i in range(len(rI)):
        rIJ.append(int(rI[i]))
    for i in range(len(rJ)):
        rIJ.append(int(rJ[i]))

    s = ''.join(map(str, rIJ))
    rIJ = int(s)

    return rIJ % K


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
    K = int((N*W) / 2)
    global hash_table

    for i in range(len(values)):
        F.append([])

        for j in range(cap + 1):
            F[i].append(-1)
            if j == 0:
                hashInsert(i, j, 0)
            else:
                hashInsert(i, j, -1)

        F[i][0] = 0
        #F[0][i] = 0

    #hash_table.setZeros()

    retVal = MFKnapsack(len(values) - 1, cap)
    retVal2 = MFKnapsack2(len(values) - 1, cap)

    hash_table.printHash()
    print()

    for i in range(len(F)):
        print()
        for j in range(len(F[i])):
            print(F[i][j], end=' ')



    print()
    print()
    print("Here's the value: ", retVal)
    print("Here's the value: ", retVal2)

