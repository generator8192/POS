import sys
import curses
from pathlib import Path

if len(sys.argv) < 2:
    print("missing file")
    sys.exit()

filepath = Path(sys.argv[1])
lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines() if filepath.exists() else [""]
if not lines:
    lines = [""]

def editor(stdscr):
    curses.raw()
    stdscr.keypad(True)
    y, x = 0, 0
    status = f" {filepath.name} | Ctrl+S: save | Ctrl+X: exit "

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, line in enumerate(lines[:h - 1]):
            stdscr.addstr(idx, 0, line[:w - 1])
        stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(h - 1, 0, status.ljust(w - 1)[:w - 1])
        stdscr.attroff(curses.A_REVERSE)
        stdscr.move(min(y, h - 2), min(x, w - 1))
        stdscr.refresh()

        key = stdscr.getch()
        if key == 24:
            break
        elif key == 19:
            filepath.write_text("\n".join(lines) + "\n", encoding="utf-8")
            status = f" saved {filepath.name} "
        elif key == curses.KEY_UP and y > 0:
            y -= 1
            x = min(x, len(lines[y]))
        elif key == curses.KEY_DOWN and y < len(lines) - 1:
            y += 1
            x = min(x, len(lines[y]))
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < len(lines[y]):
            x += 1
        elif key in (10, 13, curses.KEY_ENTER):
            rest = lines[y][x:]
            lines[y] = lines[y][:x]
            lines.insert(y + 1, rest)
            y += 1
            x = 0
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if x > 0:
                lines[y] = lines[y][:x - 1] + lines[y][x:]
                x -= 1
            elif y > 0:
                prev_len = len(lines[y - 1])
                lines[y - 1] += lines.pop(y)
                y -= 1
                x = prev_len
        elif 32 <= key <= 126 or key >= 160:
            lines[y] = lines[y][:x] + chr(key) + lines[y][x:]
            x += 1

curses.wrapper(editor)

