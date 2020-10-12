from Dijkstra.ProgramLogic.Graph import Graph
from Dijkstra.GUI.Visuals import *
from Dijkstra.Utills.HelperFunctions import *


def main():
    """
    main runner of the program
    :return:
    """
    print("ROWS=", ROWS, " COLS=", COLS)
    edges = generate_edge_from_screen()
    graph = Graph(edges)
    #source_node = graph.get_vertexes()["(0,0)"]
    #dest_node = graph.get_vertexes()["(3,3)"]
    visuals = Visuals(graph)
    visuals.run_visuals()


if __name__ == '__main__':
    main()
