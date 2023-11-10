import numpy as np
from tile import Tile


class Board:
    def __init__(self, screen, width, height, turn):
        self.screen = screen
        self.width = width
        self.height = height
        self.turn = turn
        self.tiles_list = self._generate_tiles()
        self.board_state = np.reshape(self.tiles_list, (3, 3))


    def _generate_tiles(self):
        tiles_list = []
        for row in range(3):
            for col in range(3):
                tile = Tile(row, col, 200, self.screen)
                tiles_list.append(tile)
        return tiles_list
    
    def get_tile_from_pos(self, x, y):
        for tile in self.tiles_list:
            if tile.rect.collidepoint(x, y):
                return tile
        return None
    
    def handle_click(self, x, y):
        tile = self.get_tile_from_pos(x, y)
        if tile is not None:
            if tile.piece is None:
                if self.turn == 'O':
                    tile.piece = 'O'
                    self.turn = 'X'
                elif self.turn == 'X':
                    tile.piece = 'X'
                    self.turn = 'O'


    def draw(self):
        for tile in self.tiles_list:
            tile.draw()