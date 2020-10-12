import pygame
from Dijkstra.Utills.Constants import BLACK, BLOCK_SIZE


class Block:
    """
    a class that represents a block in a grid (sized BLOCK_SIZE*BLOCK_SIZE)
    """

    def __init__(self, x, y, size=BLOCK_SIZE, color=BLACK):
        self.row = y // BLOCK_SIZE * BLOCK_SIZE   # ROUNDING SO WE WILL ONLY DRAW INSIDE GRID
        self.col = x // BLOCK_SIZE * BLOCK_SIZE
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw_block(self, window, color):
        """
        draws the block with the given colour
        :param window:
        :param color: a colour, represented with three digits (x1,x2,x3), where 0<=x_i<=255
        :return:
        """
        rect = (self.x, self.y, self.size, self.size)
        pygame.draw.rect(window, color, rect)
