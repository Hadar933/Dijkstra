import pygame

BLOCK_SIZE = 10


class Block:
    """
    a class that represents a block in a grid
    """

    def __init__(self, x, y, size=BLOCK_SIZE):
        self.x = x
        self.y = y
        self.size = size

    def draw_block(self, window, color):
        """
        draws the block with the given colour
        :param color: a colour, represented with three digits (x1,x2,x3), where 0<=x_i<=255
        :return:
        """
        pygame.draw.rect(window, color, (self.x, self.y, self.size, self.size))
