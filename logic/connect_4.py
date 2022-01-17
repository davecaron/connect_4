import numpy as np

class connect4Game:

    def __init__(self, nb_of_column=7, nb_of_line=6, win_condition=4):
        self.nb_of_column = nb_of_column
        self.nb_of_line = nb_of_line
        self.winCondition = win_condition
        self.player0board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.player1board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.board = np.zeros((self.nb_of_line, self.nb_of_column))
        self.winning_player = -1
        self.last_move_i = -1
        self.last_move_j = -1


    def check_for_player_win(self, player):

        if player == 0:
            board = self.player0board
        elif player == 1:
            board = self.player1board
        else:
            print("Invalid player choice")
            return None

        #horizontal lines
        for i in range(self.nb_of_line):
            for j in range(self.nb_of_column - (self.winCondition - 1)):
                total = 0
                #print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.winCondition):
                    total += board[i][j + k]

                if total >= self.winCondition:
                    self.winning_player = player
                    return True

        #vertical lines
        for j in range(self.nb_of_column):
            for i in range(self.nb_of_line - (self.winCondition - 1)):
                total = 0
                #print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.winCondition):
                    total += board[i + k][j]

                if total >= self.winCondition:
                    self.winning_player = player
                    return True

        #diagonal positive slope
        for i in range(self.winCondition - 1 ,self.nb_of_line):
            for j in range(self.nb_of_column - (self.winCondition - 1)):
                total = 0
                #print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.winCondition):
                    total += board[i - k][j + k]

                if total >= self.winCondition:
                    self.winning_player = player
                    return True

        # diagonal negative slope
        for i in range(self.nb_of_line - (self.winCondition - 1)):
            for j in range(self.nb_of_column - (self.winCondition - 1)):
                total = 0
                #print("i = " + str(i) + "     j = " + str(j))
                for k in range(self.winCondition):
                    total += board[i + k][j + k]

                if total >= self.winCondition:
                    self.winning_player = player
                    return True
        return False


    def add_move(self, player, i, j):

        if player == 0:
            board = self.player0board
        elif player == 1:
            board = self.player1board
        else:
            print("Invalid player choice")
            return None

        self.last_move_i = i
        self.last_move_j = j
        board[i, j] = 1
        print("player 0 board: ")
        print(self.player0board)
        print("player 1 board: ")
        print(self.player1board)

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