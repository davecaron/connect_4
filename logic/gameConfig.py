from dataclasses import dataclass
from defines.gameDefines import BoardConfig, OpponentType


@dataclass
class GameConfig:
    opponentType: OpponentType = OpponentType.HUMAN
    numberColumns: int = BoardConfig.DEFAULT_NUMBER_COLUMNS
    numberLines: int = BoardConfig.DEFAULT_NUMBER_LINES
    numberPiecesToWin: int = BoardConfig.DEFAULT_NUMBER_PIECES_TO_WIN
