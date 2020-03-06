import numpy as np
from  collections import OrderedDict
class Graph(object):
    def __init__(self, labels , directed = False):
      
        self.labels = list(OrderedDict.fromkeys(labels))
        self.size = len(self.labels)
        self.adjMatrix = []
        self.directed = directed
        for i in range(self.size):
            self.adjMatrix.append([0 for i in range(self.size)])
        

    def addEdge(self, label_1, label_2, weight):
        v1 = self.labels.index(label_1)
        v2 = self.labels.index(label_2)
        self.adjMatrix[v1][v2] = weight
        if(self.directed == False): self.adjMatrix[v2][v1] = weight

    def removeEdge(self, label_1, label_2):
        v1 = self.labels.index(label_1)
        v2 = self.labels.index(label_2)
        if self.adjMatrix[v1][v2] == 0:
            return
        self.adjMatrix[v1][v2] = 0

    def containsEdge(self, label_1, label_2):
        v1 = self.labels.index(label_1)
        v2 = self.labels.index(label_2)
        return True if self.adjMatrix[v1][v2] != 0 else False

    def addVertexLabel(self,label):
      if(label in self.labels): return
      else:
        self.labels = (self.labels + [label])
        self.size = len(self.labels)
        self.adjMatrix.append([0 for i in range(self.size - 1)])
        for i in range(self.size): self.adjMatrix[i].append(0) 
    
    def removeVertexLabel(self,label):
      try:
        self.labels.remove(label)
        self.size = len(self.labels)
        self.adjMatrix.remove(self.adjMatrix[-1])
        for i in range(self.size): self.adjMatrix[i].remove(self.adjMatrix[i][self.size])
      except:
        print("WTF are you removing something which doesn't exist?")

    def __len__(self):
        return self.size

    def __edges__(self):
        return np.count_nonzero(self.adjMatrix)
        
    def DisplayAdjMatrix(self):
        label_str = ' '.join(map(str, self.labels ))
        adj_repr  = '%  ' + label_str 
        i = 0;
        for row in self.adjMatrix:
            adj_repr += '\n%' + self.labels[i] + ' ' + ' '.join(map(str, row ))
            i+=1;
        return(adj_repr)
