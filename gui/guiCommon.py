from enum import Enum


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


class OpponentType(Enum):
    Invalid = -1
    Human = 0
    Ai    = 1


def getOpponentName(opponentType):
    name = "Invalid"

    if opponentType == OpponentType.Human.value:
        name = "Human"
    elif opponentType == OpponentType.Ai.value:
        name = "Ai"

    return name


def setLabelFontSize(widget, fontSize):
    labelFont = widget.font()
    labelFont.setPointSize(fontSize)
    widget.setFont(labelFont)


if __name__ == "__main__":
    print("guiCommon")
