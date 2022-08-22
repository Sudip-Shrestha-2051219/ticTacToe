"""
Created on Thu Apr 14 06:51:43 2022
@author: sudip with a lot of help from the book "Automate the Boring stuff with python"
"""

import sys
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                   'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                   'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space(top-L or R or M) or (mid-L or R or M) or (low-L or R or M)?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
         turn = 'O'
    else:
        turn = 'X'
    #These are the conditions for X to win.
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X'\
        or theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X'\
           or theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X'\
               or theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X'\
                   or theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X'\
                       or theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X'\
                           or theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X'\
                               or theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
        printBoard(theBoard)
        print('X is the winner of the game')
        sys.exit()
    #These are the conditinos for O to win.
    elif theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O'\
        or theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O'\
            or theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O'\
                or theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O'\
                    or theBoard['top-R'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-L'] == 'O'\
                        or theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O'\
                            or theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O'\
                                or theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O':
            printBoard(theBoard)
            print('O is the winner of the game')
            sys.exit()
print('The game ends in a draw!!! Well played.')
