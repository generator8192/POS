import sys
import shutil
from pathlib import Path

if len(sys.argv) < 2:
    print("missing operand")
    sys.exit()

for name in sys.argv[1:]:
    target = Path(name)
    if target.is_dir():
        shutil.rmtree(target)
    elif target.exists():
        target.unlink()
    else:
        print(f"cannot remove '{name}'")

