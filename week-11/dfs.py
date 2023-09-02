#!/usr/bin/env python3

class DFSPaths(object):

   def __init__(self, g, s):
      self.g = g
      self.s = s
      self.visited = [False for _ in range(g.V)]
      self.parent = [False for _ in range(g.V)]
      self.dfs(s)

   def dfs(self, v):
      self.visited[v] = True
      for w in self.g.adj[v]:
         if not self.visited[w]:
            self.parent[w] = v
            self.dfs(w)

   # Return True if there is a path from s to v
   def hasPathTo(self, v):
      # This is for you to write

      pass

   # Return path from s to v (or None should one not exist)
   def pathTo(self, v):
      # This is for you to write
      pass


with open('graph01.txt') as f:

   V = int(f.readline())

   g = Graph(V)

   for line in f:

       v, w = [int(t) for t in line.strip().split()]
       g.addEdge(v, w)

   paths = DFSPaths(g, 0)

   print(paths.hasPathTo(6))

   print(paths.pathTo(6))
