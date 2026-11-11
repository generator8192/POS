import os
import sys
import subprocess
from pathlib import Path

root = Path(".").resolve()
loader = Path("start.py").resolve()

while True:
    raw = input(f"{os.getcwd()}> ").strip()
    if not raw:
        continue
    parts = raw.split()
    command = parts[0]
    args = parts[1:]

    if command == "exit":
        sys.exit()
    if command == "main":
        continue
    if command == "cd":
        try:
            os.chdir(args[0] if args else root)
        except Exception:
            print("no such directory")
        continue

    try:
        target = next(root.rglob(f"{command}.epp"))
        subprocess.run([sys.executable, str(loader), str(target)] + args)
    except StopIteration:
        print("bad command")
    except Exception:
        print("crash")

