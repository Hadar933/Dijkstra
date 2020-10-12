from Dijkstra.ProgramLogic.Algorithm import dijkstra
from Dijkstra.GUI.Block import *
from Dijkstra.Utills.Constants import *


class Visuals:

    def __init__(self, graph, source_node, dest_node, color=WHITE, screen_width=WIDTH, screen_height=HEIGHT):
        self.graph = graph

        self.dest_node = dest_node
        self.source_node = source_node
        self.good_nodes = []  # all the possible pixels that are reachable
        self.bad_nodes = []  # the pixels that we cannot use (generated from mouse click)

        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dijkstra")
        self.color = color  # screen color
        self.window.fill(color)

        self.height = screen_height
        self.width = screen_width

        self.rows = self.height // BLOCK_SIZE
        self.cols = self.width // BLOCK_SIZE

        self.run_button = pygame.Rect(WIDTH - BUTTON_WIDTH, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

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
            for bad_node in self.bad_nodes:
                bad_node.draw_block(self.window, BARRIER_COLOR)
        elif node_type == "good":
            for good_node in self.good_nodes:
                good_node.draw_block(self.window, GREY)
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
                        dijkstra(self.graph, self.source_node, self.window, self.dest_node)
            self.draw_nodes("bad")
            self.draw_nodes("good")
            self.add_bad_nodes_with_mouse()

    def add_bad_nodes_with_mouse(self):
        """
        add blocks to the game when left mouse is clicked. these blocks represent an unreachable node in the graph
        (i.e, an unreachable pixel that the dijkstra algorithm should not use when looking for path from src to dest)
        """
        if pygame.mouse.get_pressed()[LEFT_MOUSE_CLICK]:
            x, y = pygame.mouse.get_pos()
            self.bad_nodes.append(Block(x, y))
