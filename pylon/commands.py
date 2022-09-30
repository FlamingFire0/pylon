import os
from pylon.logging import *



def getargs(cmd):
    cmd = cmd.split()
    cmd.remove(cmd[0])
    return " ".join(cmd)

def cd(dir):
    if os.path.exists(str(dir)):
        os.chdir(dir)
    else:
        error("Path does not exist!", dir)