""" Add a test for notable functions bellow """

import unittest
import functions as f
import json

class FunctionTesting(unittest.TestCase):
    
    def test_take_move(self):
        old = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        new = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(f.take_move(old, 1, 2), new)

    def test_update(self):
        data = [1, 1, 2, 0, 2, 0, 0, 0, 0]
        visual = ['X', 'X', 'O', '_', 'O', '_', '_', '_', '_']
        self.assertEqual(f.update(data), visual)

    def test_win_check(self):
        with open(r"Tic-Tac-Toe-AI/data/test_data.json") as json_file:
            data = json.load(json_file)
        for situation in data['test_win_check']:
            player_o_pos = int(situation['player_o_pos'],2)
            player_x_pos = int(situation['player_x_pos'],2)
            self.assertTrue(f.win_check(player_o_pos =player_o_pos,player_x_pos=player_x_pos) == situation['winer'])

if __name__ == '__main__':  
    unittest.main()

FunctionTesting.test_win_check()


