import pygame
import Dijkstra.Frontend.Block


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    break
            left_mouse = 0
            mid_mouse = 1
            right_mouse = 2
            if pygame.mouse.get_pressed()[left_mouse]:
                pos = pygame.mouse.get_pos()
if __name__ == "__main__":
