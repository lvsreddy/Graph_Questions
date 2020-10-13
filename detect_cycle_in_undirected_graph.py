# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:25:21 2020

@author: Sudharshan.Reddy
"""

from collections import defaultdict
class Graph:
    
    def __init__(self, vertices):
        self.v = vertices
        
        self.adjlist = defaultdict(list)
        
    def addEdge(self, s, d):
        self.adjlist[s].append(d)
        self.adjlist[d].append(s)
        
    def isCyclicUtil(self,s, visited, parent):
        
        visited[s] = 1
        
        for adj in self.adjlist[s]:
            if visited[adj] == -1:
                if(self.isCyclicUtil(adj, visited, s)):
                    return True
            elif(parent != adj ):
                return True
        return False
    
    def isCyclic(self):
        
        visited = [-1] * self.v
        
        for i in range(self.v):
            if visited[i] == -1:
                if(self.isCyclicUtil(i, visited, -1)):
                    return True
        return False
    



g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 
  
if g.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
  
  
if g1.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")