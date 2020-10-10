from Dijkstra.Frontend.Block import *
from Dijkstra.Utills.Constants import *


class RunVisuals:

    def __init__(self, color=WHITE, screen_width=WIDTH, screen_height=HEIGHT):
        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Dijkstra")
        self.window.fill(WHITE)
        self.blocks = []
        self.height = screen_height
        self.width = screen_width
        self.color = color  # screen color
        self.rows = self.height // BLOCK_SIZE
        self.cols = self.width // BLOCK_SIZE

    def draw_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                line_width = 1
                pygame.draw.rect(self.window, GREY, rect, line_width)

    def draw_all(self):
        for b in self.blocks:
            b.draw_block(self.window, BLACK)
        pygame.display.update()

    def run(self):
        run = True
        self.draw_grid()
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
    rv.run()
