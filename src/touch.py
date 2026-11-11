import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("missing file")
    sys.exit()

for name in sys.argv[1:]:
    Path(name).touch()

