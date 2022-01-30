APPLICATION_NAME = "Connect4"

VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_BUILD = 0


def getVersion():
    return str(VERSION_MAJOR) + "." + str(VERSION_MINOR) + "." + str(VERSION_BUILD)


def getNameAndVersion():
    return APPLICATION_NAME + " v." + getVersion()


if __name__ == "__main__":
    print("versionDefines")
