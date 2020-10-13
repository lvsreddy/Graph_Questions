# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:25:17 2020

@author: Sudharshan.Reddy
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        
        self.adjlist = defaultdict(list)
        
        self.reacbalitity_matrix = [[0 for j in range(self.v)] for i in range(self.v)]
        
    def addEdge(self, s, d):
        self.adjlist[s].append(d)
        
    def findReachabilityMatrix(self, s, d):
    
        
        self.reacbalitity_matrix[s][d] = 1
        
        for adjItem in self.adjlist[d]:
            if self.reacbalitity_matrix[s][adjItem] == 0:
                self.findReachabilityMatrix(s, adjItem)
            
        
        
        
    def findMother(self):
        print ("Mother Vertices :")

        for i in range(self.v):
            if self.reacbalitity_matrix[i][i] == False:
                self.findReachabilityMatrix(i, i)
            count = 0
            for j in range(self.v):
                if self.reacbalitity_matrix[i][j] == 1:
                    count += 1
                if count == self.v:
                    print(i)
        






g = Graph(7) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0)
  
g.findMother()