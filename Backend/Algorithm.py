"""
Project algorithm based on a min-heap
@see: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/ (pseudo)
"""
import heapq
from Dijkstra.Backend.ProgramLogic import get_block_from_node, RED, print_min_distances


def build_min_heap(graph):
    """
    initializes a min-heap with all vertexes from the graph
    :param graph: a dictionary that represents a graph
    """
    Q = []  # python min-heap can be represented in an array
    for v in graph.get_vertexes().values():
        heapq.heappush(Q, v)
    return Q


def dijkstra(graph, source, window):
    """
    dijkstra algorithm
    :param window: pygame window, on which we draw the path
    :param graph: a representation of a graph (set)
    :param source: a node to start from
    """
    source.set_dist_from_source(0)
    Q = build_min_heap(graph)  # O(V)
    while Q:  # O(V)
        u = heapq.heappop(Q)  # pops the min val based on dist from source (get value and remove from heap) O(logV)
        neighbors_of_u = graph.get_neighbors()[u.name]
        for v in neighbors_of_u:  # O(E)
            weight_u_v = graph.get_edge_weight(u.name, v.name)
            v_dist = v.dist_from_source
            u_dist = u.dist_from_source
            if v_dist > u_dist + weight_u_v:
                v.set_dist_from_source(u_dist + weight_u_v)
                heapq.heappush(Q, v)  # O(logV)
                # drawing:
                block = get_block_from_node(u)
                block.draw_block(window, RED)
    print_min_distances(graph, source)
