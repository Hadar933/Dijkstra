from Dijkstra.ProgramLogic.Algorithm import dijkstra
from Dijkstra.GUI.Block import *
from Dijkstra.ProgramLogic.Node import Node
from Dijkstra.Utills.Constants import *
from Dijkstra.Utills.HelperFunctions import get_node_name, get_block_from_node


class Visuals:

    def __init__(self, graph, color=WHITE, screen_width=WIDTH, screen_height=HEIGHT):
        self.fps = FPS
        self.clock = pygame.time.Clock()

        self.graph = graph

        self.dest_node = None
        self.source_node = None

        self.bad_nodes = dict()  # un-usable pixels (generated from mouse click). key = node name, val = node instance

        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dijkstra")
        self.color = color  # screen color
        self.window.fill(color)

        self.height = screen_height
        self.width = screen_width

        self.rows = self.height // BLOCK_SIZE
        self.cols = self.width // BLOCK_SIZE

        self.is_src_button_init = False
        self.is_dest_button_init = False

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
                bad_node.draw(self.window, BARRIER_COLOR)
        pygame.display.update()

    def run_visuals(self):
        """
        runs the visuals in a loop
        """
        run = True
        self.draw_grid()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse click
                    x, y = event.pos
                    row = y // BLOCK_SIZE
                    col = x // BLOCK_SIZE
                    if event.button == RIGHT_MOUSE_CLICK:  # right click - source and dest
                        if not self.is_src_button_init:
                            source_block = Block(row, col, color=START_COLOR)
                            source_block.draw(self.window, START_COLOR)
                            self.source_node = Node(get_node_name(row, col))
                            self.is_src_button_init = True
                        elif not self.is_dest_button_init:
                            dest_block = Block(row, col, color=END_COLOR)
                            dest_block.draw(self.window, END_COLOR)
                            self.dest_node = Node(get_node_name(row, col))
                            self.is_dest_button_init = True

                    elif event.button == LEFT_MOUSE_CLICK:  # left click - bad nodes
                        self.add_bad_nodes_with_mouse()
                        self.draw_nodes("bad")
                        self.graph.remove_edges_of_bad_nodes(self.bad_nodes)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # pressed enter - run algorithm
                        dijkstra(self.graph, self.source_node, self.window, self.dest_node)

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
