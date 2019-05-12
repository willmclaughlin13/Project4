# William McLaughlin
# Evan LeValley


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        edge = []
        for u, v, weight in result:

            newList = [u, v,weight]
            edge.append(newList)
            newList = [v, u, weight]
            edge.append(newList)

        return find_eulerian_tour(edge)


def next_node(edge, current):
    return edge[0] if current == edge[1] else edge[1]


def remove_edge(raw_list, discard):
    return [item for item in raw_list if item != discard]


def find_eulerian_tour(graph):
    search = [[[], graph[0][0], graph]]
    while search:
        path, node, unexplore = search.pop()
        path += [node]

        if not unexplore:
            return path

        for edge in unexplore:
            if node in edge:
                search += [[path, next_node(edge, node), remove_edge(unexplore, edge)]]


def trimPath(eucPath):
    unique = []

    for i in eucPath:
        if i not in unique:
            unique.append(i)

    unique.append(unique[0])
    return unique


def getWeight(eucPath, matrix):
    sum = 0
    for i in range(len(eucPath)-2):
        j = eucPath[i]
        k = eucPath[i+1]
        sum += matrix[j][k]
    return sum


def main():
    matrix = [[]]
    count = 0

    with open('in.txt', 'r') as f:
        for line in f:
            matrix.append([])
            for word in line.split():
                string = word.strip()
                integer = int(string, 10)
                matrix[count].append(integer)
            count += 1

    g = Graph(len(matrix)-1)
    for i in range(len(matrix)-1):
        for j in range(len(matrix)-1):
            g.addEdge(i, j, matrix[i][j])


    eucPath = g.KruskalMST()
    eucPath = trimPath(eucPath)
    weight = getWeight(eucPath, matrix)
    print("sum: ", weight)

    for u in eucPath:
        # if u == 0:
        #     u = 'Aa'
        # if u == 1:
        #     u = 'Ba'
        # if u == 2:
        #     u = 'Be'
        # if u == 3:
        #     u = 'Du'
        # if u == 4:
        #     u = 'Fr'
        # if u == 5:
        #     u = 'Ha'
        # if u == 6:
        #     u = 'Mu'
        # if u == 7:
        #     u = 'Nu'
        # if u == 8:
        #     u = 'St'
        print(u, end=' -- ')


main()
