# Author: Jesse Zelaya
# Date: 5/29/2021
# Description: Classic builder game using Python3 console

class BuildersGame:
    def __init__(self):

        self._board = [[(0,''),(0,''),(0,''),(0,''),(0,'')],
                       [(0,''),(0,''),(0,''),(0,''),(0,'')],
                       [(0,''),(0,''),(0,''),(0,''),(0,'')],
                       [(0,''),(0,''),(0,''),(0,''),(0,'')],
                       [(0,''),(0,''),(0,''),(0,''),(0,'')]]
        self._current_state = "UNFINISHED"
        self._player_turn = 'x'
        self._first_move_x = True

    def print_board(self):
        """ prints board out for gameplay"""
        print('\n')
        print('----Board-----')
        for i in range(len(self._board)-1, -1, -1):
            print(self._board[i], '\n')

        print('----Board----\n')

    def initial_placement(self, row1, col1, row2, col2, piece):
        """initial move for player"""

        # # sets initial gameplay of player turn
        # if self._player_turn is None:
        #     self._player_turn = piece
        # # wrong player

        if piece != 'x' and self._first_move_x is True:
            return False
        else:
            if piece == 'x':
                self._first_move_x = False
                self._player_turn = 'o'
            elif piece == 'o':
                self._player_turn = 'x'
            # not valid piece
            else:
                return False

        # set initial first piece, and keeps building height
        # spot taken
        if self._board[row2][col2][1] != '':
            return False
        else:
            self._board[row1][col1] = (self._board[row1][col1][0],piece)

        # check for overlap on initial piece setting
        if self._board[row2][col2][1] != '':
            return False
        else:
            self._board[row2][col2] = (self._board[row2][col2][0],piece)

        if piece == 'o':
            self._player_turn = 'x'
        else:
            self._player_turn = 'o'

        return True

    def get_current_state(self):
        """returns the state of game"""
        return self._current_state

    def make_move(self, row_from, col_from, row_to, col_to, row_build, col_build):
        """makes move and build on an adjacent square"""

        if self._first_move_x is True:
            return False

        # check if move is valid
        if abs(row_to - row_from) > 1 or abs(col_to - col_from) > 1:
            return False

        if (row_build - row_to) > 1 or (col_build - col_to) > 1:
            return False

        if self._board[row_from][col_from][1] != self._player_turn:
            return False

        # check if game is already won
        if self.check_win():
            return False

        if self._board[row_from][col_from][1] != self._player_turn:
            return False

        if (self._board[row_to][col_to][0] - self._board[row_from][col_from][0]) > 1:
            return False

        if (self._board[row_build][col_build][0]) >= 4:
            return False

        # if all tests pass then make move and update state and check if won
        piece = self._board[row_from][col_from][1]

        self._board[row_from][col_from] = (self._board[row_from][col_from][0], '')
        self._board[row_to][col_to] = (self._board[row_to][col_to][0], piece)
        self._board[row_build][col_build] = (self._board[row_build][col_build][0] + 1,
                                             self._board[row_build][col_build][1])
        if self._player_turn == 'x':
            self._player_turn = 'o'
        else:
            self._player_turn = 'x'

        #check if won
        if self.check_win():
            print(self._current_state)

        return True



    def check_win(self):
        """checks for win
            returns true if won and false if not"""

        for i in range(0, len(self._board)):
            for k in range(0, len(self._board[i])):
                if self._board[i][k][0] >= 3 and self._board[i][k][1] != '':
                    if self._board[i][k][1] == 'x':
                        self._current_state = 'X_WON'
                        return True
                    else:
                        self._current_state = 'O_WON'
                        return True
        return False


# game testing
# game = BuildersGame()
# print(game.initial_placement(0,1,4,2,'o'))
# print(game.initial_placement(2,2,1,2,'x'))
# print(game.initial_placement(0,1,4,2,'o'))
# print(game.make_move(2,2,1,1,1,0))
# print(game.make_move(0,1,1,0,2,0))
# print(game.get_current_state())
