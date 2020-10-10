import pygame
from Dijkstra.Frontend.Block import *

# mouse clicks
LEFT_MOUSE_CLICK = 0
MID_MOUSE_CLICK = 1
RIGHT_MOUSE_CLICK = 2

# screen resolution
WIDTH = 1000
HEIGHT = 700
BLOCK_SIZE = 10

# colors (R,B,G)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class RunVisuals:
    def __init__(self, color=WHITE, screen_width=WIDTH, screen_height=HEIGHT):
        self.win = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dijkstra")
        self.win.fill(WHITE)
        self.blocks = []
        self.height = screen_height
        self.width = screen_width
        self.color = color  # screen color
        self.rows = self.height // BLOCK_SIZE
        self.cols = self.width // BLOCK_SIZE

    def draw_grid(self):
        for row in self.rows:
            for col in self.cols:
                pygame.draw.line()

    def draw_all(self):
        #self.draw_grid()
        for b in self.blocks:
            b.draw_block(self.win, BLACK)
        pygame.display.update()

    def main(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_all()
            if pygame.mouse.get_pressed()[LEFT_MOUSE_CLICK]:
                x, y = pygame.mouse.get_pos()
                self.blocks.append(Block(x, y))


if __name__ == "__main__":
    rv = RunVisuals()
    rv.main()
