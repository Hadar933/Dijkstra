import networkx as nx
import matplotlib.pyplot as plt

from Dijkstra.Backend.Algorithm import dijkstra
from Dijkstra.Backend.Graph import Graph


def print_min_distances(graph, source_name):
    """
    prints the return value of dijkstra
    :param graph:
    :param source_name:
    :return:
    """
    print("Source Node is: ", source_name)
    for node in graph.get_vertexes().values():
        print("Node=", node.name, ", dist from source =", node.dist_from_source)


def visualize_graph(edges_lst):
    """
    plots a visualization of the graph
    :param edges_lst: list of tuples that represents edges, such as: [("A", "B", 1), ("A", "C", 1),...]
    """
    G = nx.Graph()
    for edge in edges_lst:
        start = edge[0]
        end = edge[1]
        weight = edge[2]
        G.add_edge(start, end, weight=weight)
    pos = nx.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


if __name__ == "__main__":
    edges = [("A", "B", 1), ("A", "C", 1),
             ("B", "A", 1), ("B", "C", 2), ("B", "D", 3), ("B", "E", 4),
             ("C", "A", 1), ("C", "B", 2), ("C", "D", 1),
             ("D", "C", 1), ("D", "B", 3), ("D", "E", 2), ("D", "F", 2),
             ("E", "B", 4), ("E", "D", 2), ("E", "F", 1),
             ("F", "E", 1), ("F", "D", 2)]

    graph = Graph(edges)
    source_node = graph.get_vertexes()["A"]
    visualize_graph(edges)
    dijkstra(graph, source_node)
    print_min_distances(graph, source_node.name)
