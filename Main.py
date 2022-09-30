import os
import time
import getpass as gt
import socket
import sys

from pylon import *

motd = open("core/lib/motd.txt").read()
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
    
cursor = ">"
inputline = "\n" + col["cyan"] + user + "@" + host + col["white"] + " - " + col["mag"] + "[" + path_preview + "]" + col["white"] + "\n" + cursor + " "


def start():
    home = path
    os.chdir(home)

def update():
     inputline = "\n" + col["cyan"] + user + "@" + host + col["white"] + " - " + col["mag"] + "[" + path_preview + "]" + col["white"] + "\n" + cursor + " "
     path = os.getcwd().replace("\\", "/")
     path_preview = path
     if path == home:
          path_preview = "~"





start()

print(motd)

while True:
     update()
     cmd = input(inputline)
     cmdsplit = cmd.split()
     if cmd == "" or cmd.startswith(" "):
          continue
   
     elif cmd.startswith("help"):
          print(help)
     
     elif cmd.startswith("clear") or cmd.startswith("cls"):
          os.system("cls")
          
     elif cmd.startswith("exit"):
          sys.exit()
     
     elif cmd.startswith("cd"):
         cd(getargs(cmd))
     
     elif cmd.startswith("run") and cmd.endswith(""):
          exec(getargs(cmd))
     
     elif cmd.startswith("print"):
          print(getargs(cmd))
          
     elif cmd.startswith("path"):
          print(path)
          
          
     elif cmd.startswith("flask"):
          startFlask()

     elif cmd.startswith("setcursor"):
         cursor = getargs(cmd)


     else:
         error("Command not found or invalid syntax", cmd)
