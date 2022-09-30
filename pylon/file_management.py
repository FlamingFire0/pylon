import os
from pylon.logging import *

def write(path, line, text):
     if os.exists(path):
          file = open(path, "r")
          lines = file.readlines()
          lines[line] = text
          lines = open(file, "w")
          file.writelines(lines)
          file.close()
     else:
          error("File Not Found", file)


def read(path, line):
     if os.exists(path):
          file = open(path, "r")
          lines = file.readlines()
          file.close()
          return (lines[line])
     else:
          error("File Not Found", file)
