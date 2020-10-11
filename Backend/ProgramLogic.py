import networkx as nx
import matplotlib.pyplot as plt


from Dijkstra.Frontend.Block import Block
from Dijkstra.Utills.Constants import *


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


def node_name(row, col):
    """
    a helper method that returns the name of a node positioned in row,col (as given by get_nodes_names() )
    """
    return "({},{})".format(row, col)


def generate_edge_from_screen():
    """
    this method generates a list of edges, where each edges corresponds to a connection of pixels on the screen,
    and each pixel is a node in the graph
    :return:
    """
    weight = 1  # all edges have weight of 1
    edges_lst = []
    for row in range(ROWS):
        for col in range(COLS):
            # 4 edges:
            set_four_edges(col, row, edges_lst, weight)
            # 2 edge rows or 2 edge columns without the 4 edges:
            set_edge_rows_cols(col, edges_lst, row, weight)
            # else - general case:
            if 0 < row < ROWS - 1 and 0 < col < COLS - 1:
                edges_lst.append((node_name(row, col), node_name(row, col - 1), weight))
                edges_lst.append((node_name(row, col), node_name(row, col + 1), weight))
                edges_lst.append((node_name(row, col), node_name(row - 1, col), weight))
                edges_lst.append((node_name(row, col), node_name(row + 1, col), weight))
    return edges_lst


def set_edge_rows_cols(col, edges_lst, row, weight):
    """
    a helper method that adds the relevant edges for either one of the two edge rows or two edge columns
    :param col: current column
    :param edges_lst: lst of edges to append to
    :param row: current row
    :param weight: =1 by default
    """
    if row == 0 and (col != 0 and col != COLS - 1):  # first row but not the edges
        edges_lst.append((node_name(0, col), node_name(0, col - 1), weight))
        edges_lst.append((node_name(0, col), node_name(1, col), weight))
        edges_lst.append((node_name(0, col), node_name(0, col + 1), weight))
    elif row == ROWS - 1 and (col != 0 and col != COLS - 1):  # last row but not the edges
        edges_lst.append((node_name(ROWS - 1, col), node_name(ROWS - 1, col - 1), weight))
        edges_lst.append((node_name(ROWS - 1, col), node_name(ROWS - 2, col), weight))
        edges_lst.append((node_name(ROWS - 1, col), node_name(ROWS - 1, col + 1), weight))
    elif col == 0 and (row != 0 and row != ROWS - 1):  # first col but not edges
        edges_lst.append((node_name(row, 0), node_name(row - 1, 0), weight))
        edges_lst.append((node_name(row, 0), node_name(row, 1), weight))
        edges_lst.append((node_name(row, 0), node_name(row + 1, 0), weight))
    elif col == COLS - 1 and (row != 0 and row != ROWS - 1):  # last col but not edges
        edges_lst.append((node_name(row, COLS - 1), node_name(row - 1, COLS - 1), weight))
        edges_lst.append((node_name(row, COLS - 1), node_name(row, COLS - 2), weight))
        edges_lst.append((node_name(row, COLS - 1), node_name(row + 1, COLS - 1), weight))


def set_four_edges(col, row, edges_lst, weight):
    """
    a helper method that adds the relevant edges for either one of the 4 edges of the graph
    :param col: current column
    :param edges_lst: lst of edges to append to
    :param row: current row
    :param weight: =1 by default
    """
    if row == 0 and col == 0:  # node (0,0)
        edges_lst.append((node_name(0, 0), node_name(1, 0), weight))
        edges_lst.append((node_name(0, 0), node_name(0, 1), weight))
    elif row == 0 and col == COLS - 1:  # node (0,COLS-1)
        edges_lst.append((node_name(0, COLS - 1), node_name(0, COLS - 2), weight))
        edges_lst.append((node_name(0, COLS - 1), node_name(1, COLS - 1), weight))
    elif row == ROWS - 1 and col == 0:  # node (ROWS-1,0)
        edges_lst.append((node_name(ROWS - 1, 0), node_name(ROWS - 2, 0), weight))
        edges_lst.append((node_name(ROWS - 1, 0), node_name(ROWS - 1, 1), weight))
    elif row == ROWS - 1 and col == COLS - 1:  # node (ROWS-1,COLS-1)
        edges_lst.append((node_name(ROWS - 1, COLS - 1), node_name(ROWS - 2, COLS - 1), weight))
        edges_lst.append((node_name(ROWS - 1, COLS - 1), node_name(ROWS - 1, COLS - 2), weight))


def get_block_from_node(node):
    """
    generates an instance of a Block from a given node
    """
    coords = node.name.split(",") # name format is '(x,y)'
    x = int(coords[0][1])*BLOCK_SIZE
    y = int(coords[1][0])*BLOCK_SIZE
    return Block(x, y)

# edges = [("A", "B", 1), ("A", "C", 1),
#          ("B", "A", 1), ("B", "C", 2), ("B", "D", 3), ("B", "E", 4),
#          ("C", "A", 1), ("C", "B", 2), ("C", "D", 1),
#          ("D", "C", 1), ("D", "B", 3), ("D", "E", 2), ("D", "F", 2),
#          ("E", "B", 4), ("E", "D", 2), ("E", "F", 1),
#          ("F", "E", 1), ("F", "D", 2)]