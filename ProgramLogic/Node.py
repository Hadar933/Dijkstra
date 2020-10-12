from Dijkstra.Utills.Constants import INFINITY


class Node:
    """
    this class represents a node that has some relevant data members
    """

    def __init__(self, name, dist_from_source=INFINITY):
        """
        constructor for a node instance
        :param name: a name represented as string : '(row,col)'
        :param dist_from_source: distance from source node
        """
        self.name = name
        self.dist_from_source = dist_from_source
        self.prev = None
        self.is_colored = False  # is the pixel that corresponds to the given node is colored already?
        # (avoids blocking)

    def set_prev(self, prev):
        self.prev = prev

    def set_dist_from_source(self, dist):
        self.dist_from_source = dist

    def get_dist_from_source(self):
        return self.dist_from_source

    def __lt__(self, other):
        """
        comparator (called when pushing to the heap)
        :param other: some node
        :return: true if self node is closer to source than other node. false otherwise
        """
        return self.dist_from_source < other.dist_from_source
