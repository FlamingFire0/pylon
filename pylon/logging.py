from pylon.color import *

def error(msg, input):
    print(col["red"] + "Error: " + msg + ": \"" + input + "\"" + col["white"])