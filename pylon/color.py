col = {
    #color
    "white": "\033[0m",
    "black": "\033[2m",
    "black2": "\033[30m",
    "strike": "\033[9m",
    "gray": "\033[1;30m",
    "grey": "\033[1;30m",
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "yel": "\033[1;33m",
    "blue": "\033[1;34m",
    "magenta": "\033[1;35m",
    "mag": "\033[1;35m",
    "cyan": "\033[1;36m",
    #style
    "blink": "\033[1;5m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    #BG
    "redBG": "\033[41m",
    "greenBG": "\033[42",
    "yellowBG": "\033[43",
    "yelBG": "\033[43",
    "blueBG": "\033[44",
    "magentaBG": "\033[45",
    "magBG": "\033[45",
    "cyanBG": "\033[46",
    "greyBG": "\033[47",
    "grayBG": "\033[47",
    "whiteBG": "\033[7m",
    "blackBG": "\033[8m"
}

if __name__ == "__main__":
    print(col["mag"] + col["italic"] + "TestMessage")