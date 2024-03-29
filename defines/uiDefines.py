

class BoardDefines:
    FINISHED_GAME_ALPHA = 140


class CellDefines:
    CELL_WIDTH_PX = 120
    CELL_HEIGHT_PX = 120
    BACKGROUND_COLOR = (1, 86, 176)
    BACKGROUND_COLOR_STR = str(BACKGROUND_COLOR)


class TokenDefines:
    TOKEN_DIAMETER_PX = int(0.85 * CellDefines.CELL_WIDTH_PX)
    EMPTY_COLOR = (1, 61, 126, 255)
    PLAYER1_COLOR = (229, 214, 64, 255)
    PLAYER2_COLOR = (235, 7, 7, 255)
    PLAYABLE_TOKEN_ALPHA = 160
    PLAYED_TOKEN_ALPHA = 255


class PlayAgainWindow:
    DEFAULT_TITLE = "Play Again"
    DEFAULT_WIDTH_PX = 200
    DEFAULT_HEIGHT_PX = 100
