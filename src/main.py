import sys
from pathlib import Path

root = Path(".")

while True:
    command = input("> ").strip()
    if not command:
        continue
    if command == "exit":
        sys.exit()
    try:
        target = next(root.rglob(f"{command}.epp"))
        load(target)
    except StopIteration:
        print("bad command")
    except Exception:
        print("crash")

