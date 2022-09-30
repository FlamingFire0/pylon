import os
from pylon.color import *

commands = {
    "help": "print(help)",
    "print": "",
    
    
    
    
    
    
}



def cd(dir):
    if os.path.exists(str(dir)):
        os.chdir(dir)
        return
    else:
        print(col["red"] + "Error: Path is invalid: \"" + str(dir) + "\"")