import numpy as np
from gameData import GameData
from defines.gameDefines import PlayerId


class Connect4Game:

    def __init__(self, gameData: GameData):
        self.nb_of_column = gameData.numberColumns
        self.nb_of_line = gameData.numberLines
        self.numberPiecesToWin = gameData.numberPiecesToWin
        self.player0board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.player1board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.winning_player = PlayerId.NO_PLAYER
        self._current_player = PlayerId.PLAYER1
        self.last_move_i = -1
        self.last_move_j = -1

    def update(self):
        self.check_for_player_win(PlayerId.PLAYER1, self.player0board)
        self.check_for_player_win(PlayerId.PLAYER2, self.player1board)

    def isFinished(self) -> bool:
        return self.winning_player != PlayerId.NO_PLAYER

    def getWinningPlayerId(self) -> PlayerId:
        return self.winning_player

    def check_for_player_win(self, player, board) -> bool:
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

        self.__changeCurrentPlayer()

    def add_move_column(self, column: int) -> (PlayerId, int):
        currentPlayerId = self._current_player
        playedRow = -1

        if self._current_player == PlayerId.PLAYER1:
            board = self.player0board
            opponent_board = self.player1board
        elif self._current_player == PlayerId.PLAYER2:
            board = self.player1board
            opponent_board = self.player0board
        else:
            print("Invalid player choice")
            return PlayerId.NO_PLAYER, -1

        column_player = board[:, column]
        column_opponent = opponent_board[:, column]

        for i in range(self.nb_of_line - 1, -1, -1):
            if column_player[i] == 1:
                continue
            elif column_opponent[i] == 1:
                continue
            else:
                self.last_move_i = i
                self.last_move_j = column
                board[i, column] = 1
                playedRow = i
                break

        self.__changeCurrentPlayer()

        return currentPlayerId, playedRow

    def reset_boards(self):
        self.player1board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.player0board = np.zeros((self.nb_of_line, self.nb_of_column))

    def __changeCurrentPlayer(self):
        if self._current_player == PlayerId.PLAYER1:
            self._current_player = PlayerId.PLAYER2
        elif self._current_player == PlayerId.PLAYER2:
            self._current_player = PlayerId.PLAYER1
        else:
            print("Invalid player current player")

    def __getPlayerBoard(self, playerId : PlayerId):
        board = None

        if playerId == PlayerId.PLAYER1:
            board = self.player0board
        elif playerId == PlayerId.PLAYER2:
            board = self.player1board
        else:
            print("Invalid player Id")

        return board
