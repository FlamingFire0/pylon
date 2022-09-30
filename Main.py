import os
import time
import getpass as gt
import socket
import sys

from pylon import *
from pylon import color


license = open("core/lib/license.txt").read()
help = open("core/lib/help.txt").read()
user = os.getlogin()
host = socket.gethostname()

path = os.getcwd()
path_preview = path
home = path
os.chdir(home)
path = os.getcwd()
home = path
path_preview = path
if path == home:
    path_preview = "~"         

def start():
    home = path
    os.chdir(home)

def update():
     path = os.getcwd()
     path_preview = path
     if path == home:
          path_preview = "~"



start()

print(license)

while True:
     update()
     cmd = input("\n" + col["cyan"] + user + "@" + host + col["white"] + " - " + col["mag"] + "[" + path_preview + "]" + col["white"] + "\n> ")
     cmdsplit = cmd.split()
     if cmd == "" or cmd.startswith(" "):
          continue
   
     elif cmd.startswith("help"):
          print(help)
     
     elif cmd == "clear" or cmd == "cls":
          os.system('cmd /c "cls"')
          
     elif cmd.startswith("exit"):
          sys.exit()
     
     elif cmd.startswith("cd"):
          print ("a")
     
     elif cmd.startswith("run") and cmd.endswith(""):
          _run = cmd.split()
          exec(_run[1])
     
     elif cmd.startswith("print") and cmd.endswith(""):
          print(cmdsplit.remove(cmdsplit[0]))
          
     elif cmd.startswith("path"):
          print(path)
          
     elif cmd.startswith("flask"):
          startFlask()


     else:
         error("Command not found or invalid syntax", cmd)
