"""
Project algorithm based on a min-heap
@see: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/ (pseudo)
"""
import heapq
import pygame
from Dijkstra.Utills.HelperFunctions import print_path, get_block_from_node
from Dijkstra.Utills.Constants import *


def build_min_heap(graph):
    """
    initializes a min-heap with all vertexes from the graph
    :param graph: a dictionary that represents a graph
    """
    Q = []  # python min-heap can be represented in an array
    for v in graph.get_nodes().values():
        heapq.heappush(Q, v)
    return Q


def dijkstra(graph, source, window, dest, clock):
    """
    dijkstra algorithm
    :param clock: pygame time clock
    :param dest: destination node
    :param window: pygame window, on which we draw the path
    :param graph: a representation of a graph (set)
    :param source: a node to start from
    """
    source.set_dist_from_source(0)
    Q = build_min_heap(graph)  # O(V)
    while Q:  # O(V)
        u = heapq.heappop(Q)  # pops the min val based on dist from source (get value and remove from heap) O(logV)
        if u == dest:
            break
        neighbors_of_u = graph.get_neighbors()[u.name]
        for v in neighbors_of_u:  # O(E)
            # drawing neighbors:
            if not v.is_colored:
                draw_on_screen(clock, v, window)
            # checking min path:
            weight_u_v = graph.get_edge_weight(u.name, v.name)
            v_dist = v.dist_from_source
            u_dist = u.dist_from_source
            if v_dist > u_dist + weight_u_v:
                v.set_dist_from_source(u_dist + weight_u_v)
                v.set_prev(u)  # updating prev is done to reconstruct the path itself
                heapq.heappush(Q, v)  # O(logV)
    print_path(window, source, dest)


def draw_on_screen(clock, v, window):
    """
    this method performs the drawings on the screen
    :param clock: pygame clock
    :param v: node to draw
    :param window: pygame window
    """
    block = get_block_from_node(v)
    block.draw(window, VISITED_COLOR)
    pygame.display.flip()
    pygame.event.pump()
    clock.tick(FPS)
