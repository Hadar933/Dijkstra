from Dijkstra.Backend.Node import Node
from Dijkstra.Utills.Constants import INFINITY


def set_connections(connections):
    """
    a static method that retrieves a dictionary that represents a graph
    :param connections: @see connection in __init__
    :return: a dictionary where the key is a Node, and the value is a list of tuples,
    where the first item is some node and the second item is the weight of the edge in-between
    """
    graph = dict()
    for item in connections:
        start_node = item[0]
        end_node = item[1]
        weight = item[2]
        neighbor = end_node, weight
        if start_node not in graph:
            graph[start_node] = [neighbor]
        else:
            graph[start_node].append((end_node, weight))
    return graph


def parse_edges(connections):
    """
    parses the input into a dictionary of edges and their respective weight. ex. (u,v):4
    :param connections: list of the form [("A", "B", 1), ("A", "C", 1),...]
    """
    edge_dict = dict()
    for edge in connections:
        key = edge[0], edge[1]  # (v,u) such that v,u in V
        value = edge[2]  # weight
        edge_dict[key] = value
    return edge_dict


class Graph:
    """
    this class represents an undirected graph
    """

    def __init__(self, edges):
        """
        :param edges:  list of vertexes of the form [(A,B,4),(B,F,3),(A,C,2),(C,B,100),...]
        where (A,B,4) means vertex A is connected to vertex B (undirected), and the weight is 4
        """
        self.__connections = set_connections(edges)
        self.__vertexes = self.__set_vertexes()
        self.__neighboring_lst = self.__set_neighboring_set()
        self.__edges = parse_edges(edges)

    def __str__(self):
        """
        returns a string representation of the graph
        """
        graph_as_str = ""
        for item in self.__connections:
            graph_as_str += item + "-> " + str(self.__connections[item]) + "\n"
        return graph_as_str

    def __set_vertexes(self):
        """
        creates a dictionary where the key is the name of the node, and the value is an instance of that node
        """
        vertex_dict = dict()
        nodes_names = self.__connections.keys()
        nodes_lst = [Node(item, INFINITY) for item in nodes_names]
        for name, node in zip(nodes_names, nodes_lst):
            vertex_dict[name] = node
        return vertex_dict

    def get_vertexes(self):
        return self.__vertexes

    def get_connections(self):
        return self.__connections

    def __set_neighboring_set(self):
        """
        initializes the set of neighbors
        """
        result = dict()
        for node in self.__connections:
            tuples = self.__connections[node]
            neighbors = [self.__vertexes[tup[0]] for tup in tuples]
            result[node] = neighbors
        return result

    def get_neighbors(self):
        """
        :return: list of all neighbors to all vertexes
        """
        return self.__neighboring_lst

    def get_edge_weight(self, node1_name, node2_name):
        """
        :param node1_name: name of first node
        :param node2_name: name of second node
        :return: weight of edge in between nodes
        """
        key = (node1_name, node2_name)
        if key in self.__edges:
            return self.__edges[key]
        return INFINITY
