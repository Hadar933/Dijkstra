from Dijkstra.ProgramLogic.Graph import Graph
from Dijkstra.GUI.Visuals import *
from Dijkstra.Utills.HelperFunctions import *


def main():
    """
    main runner of the program
    :return:
    """
    edges = generate_edge_from_screen()
    graph = Graph(edges)
    source_node = graph.get_vertexes()["(0,1)"]
    dest_node = graph.get_vertexes()["(5,5)"]
    visuals = Visuals(graph, source_node,dest_node)
    visuals.run_visuals()


if __name__ == '__main__':
    main()
