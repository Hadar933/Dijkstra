# represents infinity:
INFINITY = float('inf')

# game frame/sec
FPS = 30

# MOUSE CLICKS
LEFT_MOUSE_CLICK = 1
MID_MOUSE_CLICK = 2
RIGHT_MOUSE_CLICK = 3

# RESOLUTION
BLOCK_SIZE = 60
WIDTH = 600
HEIGHT = 600
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE
BUTTON_WIDTH = 70
BUTTON_HEIGHT = 20

# COLORS (R,G,B):
BARRIER_COLOR = (0, 0, 0)  # represents node that were drawn with the mouse, cannot walk on those (black)
WHITE = (255, 255, 255)  # for the background (white)
GREY = (160, 160, 160)  # for grid lines and buttons (grey)
PATH_COLOR = (255, 0, 0)  # the final minimum path (red)
VISITED_COLOR = (255, 128, 0)  # all the visited nodes (orange)
START_COLOR = (0, 255, 0)  # color or source node (green)
END_COLOR = (0, 0, 255)  # color of destination node (blue)
