import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Tile:
    def __init__(self, row: int, col: int, tile_size: int, screen: pygame.Surface):
        self.tile_size = tile_size
        self.row = row
        self.col = col
        self.screen = screen

        self.piece = None
        
        self.rect = pygame.Rect(
            self.col * self.tile_size,
            self.row * self.tile_size,
            self.tile_size,
            self.tile_size
        )


    def draw(self):
        pygame.draw.rect(self.screen, WHITE, self.rect, 0, 5)
        pygame.draw.rect(self.screen, BLACK, self.rect, 1, 5)
        if self.piece is not None:
            if self.piece == 'O':
                pygame.draw.circle(self.screen, BLACK, self.rect.center, self.tile_size // 2, 5)
            elif self.piece == 'X':
                pygame.draw.line(self.screen, BLACK, self.rect.topleft, self.rect.bottomright, 5)
                pygame.draw.line(self.screen, BLACK, self.rect.topright, self.rect.bottomleft, 5)