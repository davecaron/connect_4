import pygame
import connect_4 as con


class connect4UI:

    def __init__(self, mode="human"):
        self.mode = mode
        self.width = 1500
        self.height = 700
        self.column_ratio = 0.14
        self.line_ratio = 0.16
        self.x_distance_circle = self.column_ratio * (self.width - 150)
        self.y_distance_circle = self.line_ratio * (self.height - 150)
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.init_screen()
        self.next_player_turn = 0
        self.connect_4 = con.connect4Game()

    def init_screen(self):

        #Background
        pygame.init()
        pygame.font.init()
        background_color = (0, 0, 255)
        self.surface.fill(background_color)

        #Rectangle with players colors
        rectangle_color = (0, 255, 0)
        rectangle_player0 = pygame.rect.Rect(50, self.height - 150, 350, 100)
        rectangle_player1 = pygame.rect.Rect(500, self.height - 150, 350, 100)
        pygame.draw.rect(self.surface, rectangle_color, rectangle_player0)
        pygame.draw.rect(self.surface, rectangle_color, rectangle_player1)

        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        font_surface0 = font.render("Player 0: ", True, (255, 255, 255))
        font_surface1 = font.render("Player 1: ", True, (255, 255, 255))
        font_surface_winner = font.render("Player 1: ", True, (255, 255, 255))

        self.surface.blit(font_surface0, (75, self.height - 125))
        self.surface.blit(font_surface1, (525, self.height - 125))

        pygame.draw.circle(self.surface, (255, 0, 0), (350, self.height - 100), 40)
        pygame.draw.circle(self.surface, (255, 255, 0), (800, self.height - 100), 40)

        pygame.display.flip()

    def update(self):
        rectangle_winner = pygame.rect.Rect(900, self.height - 150, 580, 100)
        pygame.draw.rect(self.surface, (0, 255, 0), rectangle_winner)

        font = pygame.font.Font(pygame.font.get_default_font(), 50)
        if self.connect_4.winning_player == -1:
            font_winner = font.render("Winning Player: None", True, (255, 0, 255))
        else:
            font_winner = font.render("Winning Player:", True, (255, 0, 255))
            if self.connect_4.winning_player == 0:
                pygame.draw.circle(self.surface, (255, 0, 0), (1400, self.height - 100), 40)
            elif self.connect_4.winning_player == 1:
                pygame.draw.circle(self.surface, (255, 255, 0), (1400, self.height - 100), 40)

        self.surface.blit(font_winner, (925, self.height - 125))

        for i in range(6):
            for j in range(7):
                if self.connect_4.last_move_i == i and self.connect_4.last_move_j == j:
                    pygame.draw.circle(self.surface, (125, 125, 125),
                                       (self.x_distance_circle * 0.5 + j * self.x_distance_circle,
                                        self.y_distance_circle * 0.5 + i * self.y_distance_circle), 46)
                if self.connect_4.player0board[i][j] == 1:
                    pygame.draw.circle(self.surface, (255, 0, 0),
                                       (self.x_distance_circle * 0.5 + j * self.x_distance_circle,
                                        self.y_distance_circle * 0.5 + i * self.y_distance_circle), 40)
                elif self.connect_4.player1board[i][j] == 1:
                    pygame.draw.circle(self.surface, (255, 255, 0),
                                       (self.x_distance_circle * 0.5 + j * self.x_distance_circle,
                                        self.y_distance_circle * 0.5 + i * self.y_distance_circle), 40)
                else:
                    pygame.draw.circle(self.surface, (255, 255, 255),
                                       (self.x_distance_circle * 0.5 + j * self.x_distance_circle,
                                        self.y_distance_circle * 0.5 + i * self.y_distance_circle), 40)
        pygame.display.flip()

        if self.connect_4.check_for_player_win(0):
            print("Player 0 Won")
        if self.connect_4.check_for_player_win(1):
            print("Player 1 Won")

    def check_click(self, x, y):
        print(x)
        print(y)
        j = x // self.x_distance_circle
        j = int(j)
        i = y // self.y_distance_circle
        i = int(i)
        print(i)
        print(j)

        if i < 0 or i > 5:
            i = -1
        if j < 0 or j > 6:
            j = -1

        return i, j

    def check_event(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:

                (x, y) = pygame.mouse.get_pos()
                i, j = self.check_click(x, y)
                if not (i == -1 or j == -1):
                    if self.mode == "human":
                        self.init_screen()
                        self.connect_4.add_move_column(self.next_player_turn, j)
                        if self.next_player_turn == 0:
                            self.next_player_turn = 1
                        else:
                            self.next_player_turn = 0
                    elif self.mode == "ai":
                        self.connect_4.add_move_column(0, j)
                        #mettre le mode de l'ai ici
                        self.init_screen()
                        self.connect_4.add_move_column(1, 0)