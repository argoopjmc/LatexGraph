
from numpy.random import seed
from numpy.random import randint
import numpy as np

class latexgraphs():
  def __init__(self, GraphGen):
    self.graph = GraphGen;
    #print(GraphGen.labels)

  def generateGraph(self , file_name):
    directed_line = '-'
    if(self.graph.directed == True): directed_line = '->'
    seed(randint(10))
    g_2 = self.graph
    L = str(g_2.DisplayAdjMatrix())
    print(L)
    points_array = [tuple(randint(-(g_2.__len__()/2), g_2.__len__()/2, 2)) for i in range(g_2.__len__())]
    tuple_array = list(set(points_array))[:g_2.__len__()]
    i=0
    j=0
    string = "{"
    string_1 = "{"
    
    for row in tuple_array:
      if(i == g_2.__len__()-1):
        string +=  '{' + str(row) + '/' + str(g_2.labels[i]) + '}'
        
      else:
        string += '{' + str(row) + '/' + str(g_2.labels[i]) + '}' + ','
        
      i+=1
    #print(g_2.__edges__())
    j=0
    adj_helper = g_2.adjMatrix
    if(g_2.directed == False):adj_helper = np.triu(g_2.adjMatrix).tolist()
    for row in adj_helper:
        for entry in row:
          
        
          if(entry != 0):
            
             string_1+=  str(g_2.labels[row.index(entry)]) + '/' + str(g_2.labels[adj_helper.index(row)]) + '/' + str(entry) + ','
            
    
      
    string += '}'
    string_1 = string_1[:-1:] + "}"
    if(g_2.__edges__() == 0): string_1 = "{}"
    #print(string)
    #print(string_1)
    #print(g_2.__edges__())
    f = open(file_name, "w+")
    f.write("\\documentclass{article} \n")
    f.write("\\usepackage[utf8]{inputenc} \n")
    f.write("\\usepackage{tikz} \n")
    f.write("\\usetikzlibrary{arrows,shapes} \n")
    f.write("\\begin{document} \n")
    f.write("\\tikzstyle{vertex}=[circle,fill=black!25,minimum size=20pt,inner sep=0pt] \n")
    f.write("\\tikzstyle{edge} = [draw,thick," + directed_line +"] \n")
    f.write("\\tikzstyle{weight} = [font=\small] \n")
    f.write("%Adjacency Matrix representation of graph \n")
    f.write(g_2.DisplayAdjMatrix() + '\n')
    f.write("\\begin{tikzpicture}[scale=1, auto,swap] \n")
    f.write("\\foreach \pos/\\name in " + string + "\n")
    f.write("\\node[vertex] (\\name) at \\pos {$\\name$}; \n")
    f.write("\\foreach \\source/ \\dest /\\weight in" + string_1 + "\n")
    f.write("\\path[edge] (\\source) -- node[weight] {$\\weight$} (\\dest); \n")
    f.write("\\end{tikzpicture} \n")
    f.write("\\end{document} \n")
    f.close()

