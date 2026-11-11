import sys
import time
import os
import subprocess

if os.name != "posix":
    print("i dont like your system")
    sys.exit()

#print(os.name)
#print(os.getlogin())
#print(os.uname())

while True:
    command = input("> ")
    if command == "exit":
        sys.exit()
    
