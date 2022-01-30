import numpy as np
from enum import Enum


class PlayerId(Enum):
    NO_PLAYER = -1
    PLAYER1 = 0
    PLAYER2 = 1


class connect4Game:
    DEFAULT_NUMBER_COLUMNS = 7
    DEFAULT_NUMBER_LINES = 6
    DEFAULT_NUMBER_PIECES_TO_WIN = 4

    def __init__(self, nb_of_column=DEFAULT_NUMBER_COLUMNS, nb_of_line=DEFAULT_NUMBER_LINES,
                 _numberPiecesToWin=DEFAULT_NUMBER_PIECES_TO_WIN):
        self.nb_of_column = nb_of_column
        self.nb_of_line = nb_of_line
        self.numberPiecesToWin = _numberPiecesToWin
        self.player0board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.player1board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.winning_player = PlayerId.NO_PLAYER.value
        self._current_player = PlayerId.PLAYER1.value
        self.last_move_i = -1
        self.last_move_j = -1

    def update(self):
        self.check_for_player_win(PlayerId.PLAYER1.value, self.player0board)
        self.check_for_player_win(PlayerId.PLAYER2.value, self.player1board)

    def isFinished(self):
        return self.winning_player != PlayerId.NO_PLAYER.value

    def getWinningPlayerId(self):
        return self.winning_player

    def check_for_player_win(self, player, board):

        # horizontal lines
        for i in range(self.nb_of_line):
            for j in range(self.nb_of_column - (self.numberPiecesToWin - 1)):
                total = 0
                # print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.numberPiecesToWin):
                    total += board[i][j + k]

                if total >= self.numberPiecesToWin:
                    self.winning_player = player
                    return True

        # vertical lines
        for j in range(self.nb_of_column):
            for i in range(self.nb_of_line - (self.numberPiecesToWin - 1)):
                total = 0
                # print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.numberPiecesToWin):
                    total += board[i + k][j]

                if total >= self.numberPiecesToWin:
                    self.winning_player = player
                    return True

        # diagonal positive slope
        for i in range(self.numberPiecesToWin - 1, self.nb_of_line):
            for j in range(self.nb_of_column - (self.numberPiecesToWin - 1)):
                total = 0
                # print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.numberPiecesToWin):
                    total += board[i - k][j + k]

                if total >= self.numberPiecesToWin:
                    self.winning_player = player
                    return True

        # diagonal negative slope
        for i in range(self.nb_of_line - (self.numberPiecesToWin - 1)):
            for j in range(self.nb_of_column - (self.numberPiecesToWin - 1)):
                total = 0
                # print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.numberPiecesToWin):
                    total += board[i + k][j + k]

                if total >= self.numberPiecesToWin:
                    self.winning_player = player
                    return True
        return False

    def add_move(self, i, j):

        board = self.__getPlayerBoard(self._current_player)

        self.last_move_i = i
        self.last_move_j = j
        board[i, j] = 1
        print("player 0 board: ")
        print(self.player0board)
        print("player 1 board: ")
        print(self.player1board)

        self.__changeCurrentPlayer()

    def add_move_column(self, player, j):
        if player == 0:
            board = self.player0board
            opponent_board = self.player1board
        elif player == 1:
            board = self.player1board
            opponent_board = self.player0board
        else:
            print("Invalid player choice")
            return None
        column_player = board[:, j]
        column_opponent = opponent_board[:, j]
        for i in range(5, -1, -1):
            if column_player[i] == 1:
                continue
            elif column_opponent[i] == 1:
                continue
            else:
                self.last_move_i = i
                self.last_move_j = j
                board[i, j] = 1
                break

        print("player 1 board: ")
        print(self.player0board)
        print("player 2 board: ")
        print(self.player1board)

    def reset_boards(self):
        self.player1board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.player0board = np.zeros((self.nb_of_line, self.nb_of_column))

    def __changeCurrentPlayer(self):
        if self._current_player == PlayerId.PLAYER1.value:
            self._current_player = PlayerId.PLAYER2.value
        elif self._current_player == PlayerId.PLAYER2.value:
            self._current_player = PlayerId.PLAYER1.value
        else:
            print("Invalid player current player")

    def __getPlayerBoard(self, playerId):
        board = None

        if playerId == PlayerId.PLAYER1.value:
            board = self.player0board
        elif playerId == PlayerId.PLAYER2.value:
            board = self.player1board
        else:
            print("Invalid player Id")

        return board
