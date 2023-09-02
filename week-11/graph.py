#!/usr/bin/env python3

class Graph(object):

    def __init__(self, v):
        # record the number of vertices in our graph
        self.v = v
        self.adj = {}
        # initialise self.adj so all vertices map to empty list
        for v in range(self.v):
            self.adj[v] = list() # []

    def addEdge(self, v, w):
        # w is adjacent to v
        self.adj[v].append(w)
        # v  is adjacent to w
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degree(v) for v in range(self.v)])

    def avgDegree(self):
        # put all the degrees into a list.
        # sum them.
        # divide by the number of vertices.
        return sum([self.degree(v) for v in range(self.v)]) / self.v


with open('graph01.txt', 'r') as f:
    v = int(f.readline().strip())
    #print(v)
    g = Graph(v)
    print(g.v)
    print(g.adj)

    for line in f:
        v, w = [int(t) for t in line.strip().split()] # '0 1' --> [0, 1]
        g.addEdge(v, w)

    print(g.adj)
    print(g.degree(3))
    print(g.degree(0))

    print(g.maxDegree())
    print(g.avgDegree())
    print("{:.2f}".format(g.avgDegree()))
