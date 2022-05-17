from typing import List, Tuple

class Node:
    def __init__(self, name: int):
        self.name = name

class Edge:
    def __init__(self, nodeA: Node, nodeB: Node, weight: int):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.weight = weight

class AdjacencyItem:
    def __init__(self, node: Node, weight: int):
        self.node = node
        self.weight = weight

class Graph:
   # Constructor to construct graph
    def __init__(self, edges: List[Edge], N: int):
        self.edges = edges
        # A list of lists to represent adjacency list
        self.adjacentMatrix: List[List[AdjacencyItem]] = [[]]*N

        # allocate memory for adjacency list
        for i in range(N):
            self.adjacentMatrix[i] = []
 
        # add edges to the undirected graph
        for e in edges:
            # allocate node in adjacency List from src to dest
            self.adjacentMatrix[e.nodeA.name].append(AdjacencyItem(e.nodeB, e.weight))
            self.adjacentMatrix[e.nodeB.name].append(AdjacencyItem(e.nodeA, e.weight))

    def addNewEdge(self, edge: Edge):
        self.edges.append(edge)
        self.adjacentMatrix[edge.nodeA.name].append(AdjacencyItem(edge.nodeB, edge.weight))
        self.adjacentMatrix[edge.nodeB.name].append(AdjacencyItem(edge.nodeA, edge.weight))

    def buy(self, products: List[Node]):
        print("\nBuy Products:", [x.name for x in products])
        for i in range(len(products)):
            for j in range(i, len(products)):
                if i != j:
                    # if already has edge -> increase weight by 1
                    hasAlreadyEdge = False
                    for edge in self.edges:
                        if ((edge.nodeA == products[i]) and (edge.nodeB == products[j])):
                            hasAlreadyEdge = True                           
                            for index, adjB in enumerate(self.adjacentMatrix[edge.nodeA.name]):
                                if adjB.node == edge.nodeB:
                                    self.adjacentMatrix[edge.nodeA.name][index].weight += 1
                            
                            for index, adjB in enumerate(self.adjacentMatrix[edge.nodeB.name]):
                                if adjB.node == edge.nodeA:
                                    self.adjacentMatrix[edge.nodeB.name][index].weight += 1
                                   
                        if((edge.nodeA == products[j]) and (edge.nodeB == products[i])):
                            hasAlreadyEdge = True                  
                            for index, adjA in enumerate(self.adjacentMatrix[edge.nodeB.name]):
                                if adjA.node == edge.nodeA:
                                    self.adjacentMatrix[edge.nodeB.name][index].weight += 1

                            for index, adjA in enumerate(self.adjacentMatrix[edge.nodeA.name]):
                                if adjA.node == edge.nodeB:
                                    self.adjacentMatrix[edge.nodeA.name][index].weight += 1
                    # if not add new edge
                    if not hasAlreadyEdge:
                        self.addNewEdge(Edge(products[i], products[j], 1))

    def recommendProducts(self, product: Node):   
        recommendation: List[Tuple[int, int]] = []

        for reco in self.adjacentMatrix[product.name]:
            recommendation.append((reco.node.name + 1, reco.weight))
        
        # sort in descending order on the basis of edge weight
        recommendations = sorted(recommendation, key=lambda x:x[1], reverse= True)
        
        print("\nRecommending for: Product " + str(product.name + 1))
        print("\nRecommeded Products:\nProduct\t: Score")
        for item in recommendations:
            print("   {}\t:   {}".format(item[0], item[1]))