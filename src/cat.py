import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("missing file")
    sys.exit()

target = Path(sys.argv[1])
if not target.is_file():
    print("file not found")
    sys.exit()

print(target.read_text(encoding="utf-8", errors="replace"))

