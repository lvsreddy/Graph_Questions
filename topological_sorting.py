# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:21:12 2020

@author: Sudharshan.Reddy
"""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        
        self.adjlist = defaultdict(list)
        
    def addEdge(self, s, d):
        self.adjlist[s].append(d)
        
    def topologicalSortUtil(self, s, visited, stack):
        
        visited[s] = True
        
        for adjitem in self.adjlist[s]:
            if visited[adjitem] == False:
                self.topologicalSortUtil(adjitem, visited, stack)
        
        stack.append(s)
        
    def topologicalSort(self):
        
        visited = [False] * self.v
        
        stack = []
        
        for i in range(self.v):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack[::-1])


g = Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
  
print("Following is a Topological Sort of the given graph")
  
# Function Call 
g.topologicalSort()