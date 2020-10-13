# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:24 2020

@author: Sudharshan.Reddy
"""

from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.v = vertices
        
        self.adjlist = defaultdict(list)
        
    def addEdge(self, s, d):
        self.adjlist[s].append(d)

        
    def isCyclicUtil(self, s, visited, instack):
        
        visited[s] = 1
        instack[s] = 1
        
        for adjitem in self.adjlist[s]:
            
            if visited[adjitem] == -1:
                if(self.isCyclicUtil(adjitem,visited,instack)):
                    return True
            elif(instack[adjitem] == 1):
                return True
            
            instack[s] = -1
            return False
        
        
    def isCyclic(self):
        
        visited = [-1]*self.v
        instack = [0]*self.v
        
        for i in range(self.v):
            if visited[i] == -1:
                if(self.isCyclicUtil(i,visited,instack)):
                    return True
        return False
        
        

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic() == 1: 
    print ("Graph has a cycle")
else: 
    print ("Graph has no cycle")