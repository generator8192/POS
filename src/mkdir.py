import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("missing operand")
    sys.exit()

for name in sys.argv[1:]:
    Path(name).mkdir(parents=True, exist_ok=True)

