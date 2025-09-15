import curses
import subprocess
import pyfiglet
import shutil

def speak(text):
    subprocess.run([
        "edge-tts",
        "--text", text,
        "--write-media", "/tmp/tmp.mp3"
    ])
    subprocess.run(["mpg123", "-a", "plughw:0,0", "/tmp/tmp.mp3"])

def main(stdscr):
    curses.curs_set(1)  # show the cursor
    input_text = ""

    while True:
        stdscr.clear()
        term_width, term_height = shutil.get_terminal_size()
        
        # Display big text
        if input_text:
            try:
                banner = pyfiglet.figlet_format(input_text, font="doh", width=240)
                lines = banner.splitlines()
                start_line = max((term_height - len(lines)) // 2, 0)
                for idx, line in enumerate(lines):
                    if idx + start_line >= term_height - 1:
                        break  # don't go past screen
                    stdscr.addstr(idx + start_line, max((term_width - len(line)) // 2, 0), line)
            except Exception:
                pass  # prevent crash if input too long for font

        # Show the input line at bottom
        stdscr.addstr(term_height - 1, 0, "> " + input_text[:term_width - 2])
        stdscr.refresh()

        try:
            ch = stdscr.get_wch()  # get a wide character
        except curses.error:
            continue  # ignore resize or unexpected input

        if isinstance(ch, str) and ch.isprintable():
            input_text += ch
        elif ch == '\n':  # Enter
            if input_text.strip():
                speak(input_text)
            input_text = ""
        elif ch in ('\x7f', '\b', curses.KEY_BACKSPACE):
            input_text = input_text[:-1]
        elif ch == '\x1b':  # ESC to quit
            break

curses.wrapper(main)
