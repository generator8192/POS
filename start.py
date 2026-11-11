import sys
import os
import marshal
import struct
import random
from pathlib import Path

if os.name != "posix":
    print("i dont like your system")
    sys.exit()

root = Path(".")

def load(filepath: Path):
    data = filepath.read_bytes()
    if len(data) < 8 or data[:4] != b"EPP\x01":
        print("bad binary")
        sys.exit()
    
    codeseed = struct.unpack(">I", data[4:8])[0]
    progbytes = data[8:]

    random.seed(codeseed)
    program = list(range(256))
    random.shuffle(program)

    rbytes = bytes(program.index(b) for b in progbytes)
    code = marshal.loads(rbytes)
    exec(code, {"__name__": "__main__", "load": load})

try:
    mainfile = next(root.rglob("main.epp"))
    load(mainfile)
except StopIteration:
    print("main.epp not found")
    sys.exit()

