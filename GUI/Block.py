import pygame
from Dijkstra.Utills.Constants import BARRIER_COLOR, BLOCK_SIZE


class Block:
    """
    a class that represents a block in a grid (sized BLOCK_SIZE*BLOCK_SIZE)
    """

    def __init__(self, row, col, size=BLOCK_SIZE, color=BARRIER_COLOR):
        self.row = row
        self.col = col
        self.color = color
        self.size = size

    def draw_block(self, window, color):
        """
        draws the block with the given colour
        :param window:
        :param color: a colour, represented with three digits (x1,x2,x3), where 0<=x_i<=255
        :return:
        """
        rect = (self.row*self.size, self.col*self.size, self.size, self.size)
        pygame.draw.rect(window, color, rect)
