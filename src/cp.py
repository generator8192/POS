import sys
import shutil
from pathlib import Path

if len(sys.argv) < 3:
    print("missing file operand")
    sys.exit()

src = Path(sys.argv)
dst = Path(sys.argv)

if not src.exists():
    print("no such file or directory")
    sys.exit()

if src.is_dir():
    shutil.copytree(src, dst, dirs_exist_ok=True)
else:
    shutil.copy2(src, dst)

