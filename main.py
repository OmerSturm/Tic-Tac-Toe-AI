""" Main file to be run and play game in terminal so far """
from functions import print_board
from functions import take_move



def main() -> None:
    data_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    visual_board = [['1', ' ', ' ', ' ', ' ', '|', '2', ' ', ' ', ' ', ' ', '|', '3', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                ['4', ' ', ' ', ' ', ' ', '|', '5', ' ', ' ', ' ', ' ', '|', '6', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
                ['7', ' ', ' ', ' ', ' ', '|', '8', ' ', ' ', ' ', ' ', '|', '9', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']]

    print_board(visual_board)
    player = 1 # X's
    move = int(input("Move: "))
    take_move(data_board, player, move)
    
    '''Loop this... Include above as well
    # Update visual Board
    # Switch players and take next move
    ''' # Check for win (Only needs to be done after 4th move)


if __name__ == "__main__":
    main()
