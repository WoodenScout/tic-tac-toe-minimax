import pygame
from board import Board
from game import Game


def main():
    palyers = int(input('1 or 2 players? '))
    size = (600, 600)
    screen = pygame.display.set_mode(size)
    board = Board(screen, size[0], size[1], 'X')
    game = Game(board)


    if palyers == 2:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    board.handle_click(*pos)
                if event.type == pygame.KEYDOWN:
                    print(game.minimax(player = board.turn, depth = 9))
                    print(game.alphabeta(player = board.turn, depth = 9))

            if game.check_winner() is not None:
                if (winner := game.check_winner()) in ['O', 'X']:
                    print(f'Winner: {winner}')
                else:
                    print('Tie')
                running = False

            board.draw()
            pygame.display.update()
    elif palyers == 1:
        running = True
        while running:
            if board.turn == 'X':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        board.handle_click(*pos)
            else:
                move = game.alphabeta(player = 'O', depth = 9)
                game.make_move(move[0], move[1], 'O')
                board.turn = 'X'

            if game.check_winner() is not None:
                if (winner := game.check_winner()) in ['O', 'X']:
                    print(f'Winner: {winner}')
                else:
                    print('Tie')
                running = False

            board.draw()
            pygame.display.update()

if __name__ == '__main__':
    main()