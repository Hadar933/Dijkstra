from Dijkstra.ProgramLogic.Graph import Graph
from Dijkstra.GUI.Visuals import *
from Dijkstra.Utills.HelperFunctions import *


def main():
    """
    main runner of the program
    :return:
    """
    print("Screen resolution:\n",
          "rows =", ROWS, "\n",
          "cols =", COLS, '\n',
          'block size =', BLOCK_SIZE)
    edges = generate_edge_from_screen()
    graph = Graph(edges)
    visuals = Visuals(graph)
    visuals.run_visuals()


if __name__ == '__main__':
    main()
