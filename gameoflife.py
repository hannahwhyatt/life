import time
import copy
import os

import numpy as np


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gameOfLife(size):
    board = np.zeros((size, size))
    
    # "Blinker"
    board[3, 2] = 1
    board[4, 2] = 1
    board[5, 2] = 1

    # "Light-weight Spaceship"
    board[10, 6] = 1
    board[10, 9] = 1
    board[11, 10] = 1
    board[12, 6] = 1
    board[12, 10] = 1
    board[13, 7] = 1
    board[13, 8] = 1
    board[13, 9] = 1
    board[13, 10] = 1

    print(board)

    while(True):
        x, y = 0, 0
        nextBoard = copy.copy(board)
        
        for x in range(size):
            for y in range(size):
                cell = nextBoard[x,y]  
                neighbours = [board[(x + 1)%size, y%size], board[(x + 1)%size, (y - 1)%size], board[(x + 1)%size, (y + 1)%size], 
                                board[(x - 1)%size, y%size], board[(x - 1)%size, (y + 1)%size], board[(x - 1)%size, (y - 1)%size], 
                                board[x%size, (y - 1)%size], board[x%size, (y + 1)%size]]
                # Rules
                if cell == 1:
                    if sum(neighbours) == 2 or sum(neighbours) == 3:
                        nextBoard[x, y ] = 1
                    else:
                        nextBoard[x, y] = 0
                        
                elif cell == 0:
                    if sum(neighbours) == 3:
                        nextBoard[x, y] = 1
                    else:
                        nextBoard[x, y] = 0
        
        time.sleep(0.3)
        clear()
        print(nextBoard)
        board = nextBoard

clear()
gameOfLife(24)