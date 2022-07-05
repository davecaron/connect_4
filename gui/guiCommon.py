from PyQt6.QtGui import QColor

from enum import Enum
from defines.gameDefines import OpponentType


class LabelAlignFlag(Enum):
    AlignLeft = 0x0001
    AlignRight = 0x0002
    AlignHCenter = 0x0004
    AlignJustify = 0x0008
    AlignAbsolute = 0x0010
    AlignTop = 0x0020
    AlignBottom = 0x0040
    AlignVCenter = 0x0080
    AlignCenter = AlignVCenter | AlignHCenter
    AlignBaseline = 0x0100


def getOpponentName(opponentType: OpponentType) -> str:
    name = "Invalid"

    if opponentType == OpponentType.HUMAN:
        name = "Human"
    elif opponentType == OpponentType.AI:
        name = "Ai"

    return name


def setLabelFontSize(widget, fontSize):
    labelFont = widget.font()
    labelFont.setPointSize(fontSize)
    widget.setFont(labelFont)


def getQColor(rgba: tuple):
    color = QColor()

    if len(rgba) > 2:
        r = rgba[0]
        g = rgba[1]
        b = rgba[2]
        color.setRgb(r, g, b)

    if len(rgba) > 3:
        alpha = rgba[3]
        color.setAlpha(alpha)

    return color
