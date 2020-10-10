import pygame
from Dijkstra.Frontend.Block import *

LEFT_MOUSE_CLICK = 0
MID_MOUSE_CLICK = 1
RIGHT_MOUSE_CLICK = 2
WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra")
BLACK = (0, 0, 0)


class RunVisuals:
    def __init__(self, window, blocks):
        self.win = window
        self.blocks = blocks

    def draw_grid(self):
        pass

    def draw_all(self):
        self.draw_grid()
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
            if pygame.mouse.get_pressed()[RIGHT_MOUSE_CLICK]:
                pos = pygame.mouse.get_pos()
                # TODO: add block to block list in the position of the mouse click


if __name__ == "__main__":
    blocks = [Block(i, i) for i in range(20)]
    rv = RunVisuals(WIN, blocks)
    rv.main()
