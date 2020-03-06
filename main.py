from graph import Graph
from latexgraphs import latexgraphs


def main():
  G = Graph(['a','b','c','d','e','f','g','h','i','j'],True)
  G.addEdge('a','b',1)
  G.addEdge('c','d',3)
  G.addEdge('e','f',5)
  G.addEdge('g','h',7)
  G.addEdge('i','j',9)
  G.addVertexLabel('k')
  G.addVertexLabel('l')
  G.addEdge('k','l',11)
  LatGraph = latexgraphs(G).generateGraph("directed.tex")


if __name__ == '__main__':
  main()