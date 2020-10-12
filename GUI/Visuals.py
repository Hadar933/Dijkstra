from Dijkstra.ProgramLogic.Algorithm import dijkstra
from Dijkstra.GUI.Block import *
from Dijkstra.Utills.Constants import *
from Dijkstra.Utills.HelperFunctions import get_node_name


class Visuals:

    def __init__(self, edges,graph, source_node, dest_node, color=WHITE, screen_width=WIDTH, screen_height=HEIGHT):
        self.fps = FPS
        self.clock = pygame.time.Clock()

        self.edges = edges
        self.graph = graph

        self.dest_node = dest_node
        self.source_node = source_node

        self.bad_nodes = dict()  # un-usable pixels (generated from mouse click). key = node name, val = node instance
        self.good_nodes = self.set_good_nodes()

        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dijkstra")
        self.color = color  # screen color
        self.window.fill(color)

        self.height = screen_height
        self.width = screen_width

        self.rows = self.height // BLOCK_SIZE
        self.cols = self.width // BLOCK_SIZE

        self.run_button = pygame.Rect(WIDTH - BUTTON_WIDTH, 0, BUTTON_WIDTH, BUTTON_HEIGHT)  # button that runs dijkstra

    def draw_grid(self):
        """
        adds a grid to the pygame window
        """
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                line_width = 1
                pygame.draw.rect(self.window, GREY, rect, line_width)

    def draw_nodes(self, node_type):
        """
        draws a good node or a bad node (a node which we can or cannot go to, respectively), depenting on a flag
        :param node_type: flag that represents which kind of node we wish to add
        """
        if node_type == "bad":
            for bad_node in self.bad_nodes.values():
                bad_node.draw_block(self.window, BARRIER_COLOR)
        pygame.display.update()

    def run_visuals(self):
        """
        runs the visuals in a loop
        """
        run = True
        self.draw_grid()
        pygame.draw.rect(self.window, GREY, self.run_button)  # run button
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.run_button.collidepoint(x, y):
                        dijkstra(self.graph, self.source_node, self.window, self.dest_node,self.clock)
            self.add_bad_nodes_with_mouse()
            self.draw_nodes("bad")
        pygame.display.update()

    def add_bad_nodes_with_mouse(self):
        """
        add blocks to the game when left mouse is clicked. these blocks represent an unreachable node in the graph
        (i.e, an unreachable pixel that the dijkstra algorithm should not use when looking for path from src to dest)
        """
        if pygame.mouse.get_pressed()[LEFT_MOUSE_CLICK]:
            x, y = pygame.mouse.get_pos()
            row = x // BLOCK_SIZE
            col = y // BLOCK_SIZE
            node_name = get_node_name(row, col)
            self.bad_nodes[node_name] = Block(row, col)

    def set_good_nodes(self):
        """
        generates notes that are usable when running the algorithm (all the screen without the pixels that were clicked
        on with the mouse and are black)
        :return:
        """
        good_nodes = {}
        for item in self.edges:
            node1_name = item[0]
            node2_name = item[1]
            if node1_name not in self.bad_nodes and node2_name not in self.bad_nodes:
                pass

