# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:14:21 2020

@author: Sudharshan.Reddy
"""
from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.v = vertices
        
        self.adjlist = defaultdict(list)
        
    def addEdge(self, s, d):
        self.adjlist[s].append(d)
        
    def printAllPathsUtil(self, s, d, visited, path):
        
        visited[s] = True
        
        path.append(s)
        
        if s == d:
            print(path)
        
        for item in self.adjlist[s]:
            if visited[item] == False:
                self.printAllPathsUtil(item,d, visited, path)
            
        path.pop()
        visited[s] = False
        
        
    def printAllPaths(self, s, d):
        
        visited = [False] * self.v
        
        path = []
        
        self.printAllPathsUtil(s,d, visited, path)
            
    





g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 
   
s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.printAllPaths(s, d) 