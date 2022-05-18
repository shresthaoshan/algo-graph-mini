import sys
from graph import Edge, Graph, Node, printGraph

if __name__ == '__main__':
    # input products
    products = [
        Node(0), #V1
        Node(1), #V2
        Node(2), #V3
        Node(3), #V4
        Node(4), #V5
        Node(5), #V6
    ]
    
    edges = []
    edges.append(Edge(products[0], products[1], 2))
    edges.append(Edge(products[0], products[4], 3))
    edges.append(Edge(products[0], products[2], 2))
    edges.append(Edge(products[1], products[2], 4))
    edges.append(Edge(products[1], products[4], 1))
    edges.append(Edge(products[1], products[3], 4))
    edges.append(Edge(products[2], products[3], 2))
    edges.append(Edge(products[2], products[5], 1))
    edges.append(Edge(products[3], products[4], 4))
    edges.append(Edge(products[3], products[5], 5))
    edges.append(Edge(products[4], products[5], 2))

    # construct graph from given list of edges
    graph = Graph(edges, len(products))

    # print adjacency list representation of the graph
    printGraph(graph=graph)

    # buy action
    graph.buy( [products[3], products[5], products[1]])
    graph.buy( [products[3], products[5], products[1]])
    graph.buy( [products[3], products[5], products[1]]) 

    printGraph(graph=graph)

    # start reco
    # prodForReco = int(input("Enter product for recommendation: "))
    graph.recommendProducts(products[(int(sys.argv[1]) - 1) if len(sys.argv) == 2 else 2])