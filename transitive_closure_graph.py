# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:24 2020

@author: Sudharshan.Reddy
"""



from collections import defaultdict


class Graph:
    
    def __init__(self, vertices):
        #Num of Vertices
        self.v = vertices
        #  Dictonary of lists to store adjacent elaments
        self.adjlist = defaultdict(list)
        
        # To store transitive closure 
        self.tc = [[0 for j in range(self.v)] for i in range(self.v)] 
        
    def addEdge(self,s,d):
        self.adjlist[s].append(d)
        
    def DFSUtil(self, s, d):
        
        self.tc[s][d] = 1
        
        for i in self.adjlist[d]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s,i)
            
        
    def transitiveClosure(self):
        
        for i in range(self.v):
            self.DFSUtil(i,i)
        print (self.tc)
        
        
        
        
        
        
        
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

  
print ("Transitive closure matrix is")
g.transitiveClosure(); 