class Logger:

    @staticmethod
    def __log(text: str, colorCode: str) -> None:
        resetCode = "\x1b[0m"
        print(f"{colorCode}{text}{resetCode}")

    @staticmethod
    def logRed(text: str) -> None:
        redCode = "\x1b[38;5;196m"
        Logger.__log(text, redCode)

    @staticmethod
    def logBlue(text: str) -> None:
        blueCode = "\x1b[38;5;39m"
        Logger.__log(text, blueCode)

    @staticmethod
    def logYellow(text: str) -> None:
        yellowCode = "\x1b[38;5;226m"
        Logger.__log(text, yellowCode)
