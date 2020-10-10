INFINITY = float('inf')


class Node:
    """
    this class represents a node that has some relevant data members
    """
    def __init__(self, name, dist_from_source=INFINITY):
        self.name = name
        self.dist_from_source = dist_from_source

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
