import pygame
from Dijkstra.Frontend.Block import *

LEFT_MOUSE_CLICK = 0
MID_MOUSE_CLICK = 1
RIGHT_MOUSE_CLICK = 2
WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra")


class RunVisuals:
    def __init__(self, window, blocks):
        self.win = window
        self.blocks = blocks

    def draw_grid(self):
        pass

    def draw_all(self):
        self.draw_grid()
        for b in self.blocks:
            b.draw_block()
        pygame.display.update()

    def main(self):
        while True:
            self.draw_all()
            if pygame.mouse.get_pressed()[RIGHT_MOUSE_CLICK]:
                pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    break


if __name__ == "__main__":
    blocks = [Block(i, i) for i in range(20)]
    rv = RunVisuals(WIN,blocks)
