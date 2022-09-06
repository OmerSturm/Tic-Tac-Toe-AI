""" A file for most supporting functions
    Please add tests for functions added in the testing.py file """

from turtle import pos
from numpy import array

player_x_pos = 0b000000000
player_o_pos = 0b000000000
positions = [0b100000000, 0b010000000, 0b001000000, 0b000100000, 0b000010000, 0b000001000,0b000000100,0b000000010,0b000000001]
wining_positions =  [0b111000000,0b000111000,0b000000111,0b100100100,0b010010010,0b001001001,0b001010100]

def print_board(board: array):
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array

def take_move(data: array, player: int, move: int):
    global player_x_pos, player_o_pos
    """ Get user input, check if valid and update data if True
    Args: Data of board, which players move (1 == 'X', 2 == 'O'),
    Return: Updated board data """
    if data[move-1] == 0:
        #checking for player whanted position and using bitwise to mark the position
        if player == 1:
            player_x_pos = bin(player_x_pos | positions[move-1])
        elif player == 2:
            player_o_pos = bin(player_o_pos | positions[move-1])
        data[move-1] = player
    return data

def update(data: array):
    """ Makes visual board off of data
    Args: Data to update
    Return: New Visual Board """
    # TODO Update better visual board
    
    visual_board = []
    for i in data:
        if i == 1:
            visual_board.append('X')
        elif i == 2:
            visual_board.append('O')
        else:
            visual_board.append('_')

    return visual_board



def menuGraphic():
    """ Print a main menu graphic
    Args: None
    Return: Main menu graphic """
    print()
    print("                                           WELCOME TO...                                          ")
    print(" ______   __     ______         ______   ______     ______          ______   ______     ______.   ")
    print("/\__  _\ /\ \   /\  ___\       /\__  _\ /\  __ \   /\  ___\        /\__  _\ /\  __ \   /\  ___\   ")
    print("\/_/\ \/ \ \ \  \ \ \____  ---  \/_/\ \/ \ \  __ \  \ \ \____ ---  \/_/\ \/ \ \ \/\ \  \ \  __\.  ")
    print("   \ \_\  \ \_\  \ \_____\         \ \_\  \ \_\ \_\  \ \_____\        \ \_\  \ \_____\  \ \_____\ ")
    print("    \/_/   \/_/   \/_____/          \/_/   \/_/\/_/   \/_____/         \/_/   \/_____/   \/_____/ ")
    print()
    print("------------------------------------------------------------------------------------------------- ")

def menuNav():
    """ Ask for user input for main menu navigation 
    Args: None
    Return: None """
    flag = True
    while flag == True:
        choice = input("What would you like to do? ")
        if choice == "play":
            pass
            #game()
            flag = False
        elif choice == "settings":
            pass
            #settings()
            flag = False
        else:
            print("Please choose something from the menu")


def win_check(player_o_pos,player_x_pos):
    #checks for a winer, if 'x' wins the function return 1, if 'o' wins reutn 2, if there is no winer, return 0
    global wining_positions
    for position in wining_positions:
        if player_o_pos & position == position:
            return 2
        elif player_x_pos & position == position: return 1
    return 0


