import marshal
import sys
from pathlib import Path
import struct
import time
import random

if len(sys.argv) < 2:
    print("fatal error: no input files")
    sys.exit(1)

codepath = Path(sys.argv[1])
if not codepath.is_file():
    print(f"error: {codepath}: No such file or directory")
    sys.exit(1)

if "-o" in sys.argv:
    o_index = sys.argv.index("-o")
    if o_index + 1 >= len(sys.argv):
        print("error: missing filename after '-o'")
        sys.exit(1)
    out = Path(sys.argv[o_index + 1])
else:
    out = Path(codepath.stem + ".epp")

codeseed = int(time.time())
random.seed(codeseed)
number = struct.pack(">I", codeseed)

code = compile(codepath.read_text(encoding="utf-8"), codepath.stem, "exec")
rbytes = marshal.dumps(code)

program = list(range(256))
random.shuffle(program)
progbytes = bytes(program[b] for b in rbytes)

out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(b"EPP\x01" + number + progbytes)

