#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degree(v) for v in range(self.V)])

with open('graph01.txt', 'r') as f:
    V = int(f.readline())
    g = Graph(V)

    for line in f:
        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

for k, v in sorted(g.adj.items()):
    print('{} --> {}'.format(k, v))

print(g.degree(1))
print(g.maxDegree())
