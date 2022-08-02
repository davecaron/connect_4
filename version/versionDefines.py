APPLICATION_NAME = "Connect4"

VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_BUILD = 0


def getVersion():
    return f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_BUILD}"


def getNameAndVersion():
    return f"{APPLICATION_NAME} v.{getVersion()}"


if __name__ == "__main__":
    print("versionDefines")
