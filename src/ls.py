import os
import sys
from pathlib import Path

target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

if not target.is_dir():
    print("not a directory")
    sys.exit()

for item in sorted(target.iterdir(), key=lambda x: (not x.is_dir(), x.name)):
    print(f"{item.name}/" if item.is_dir() else item.name)

