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
        term_width = shutil.get_terminal_size().columns
        
        # Display the current input as big text
        if input_text:
            banner = pyfiglet.figlet_format(input_text, font="doh")
            for idx, line in enumerate(banner.splitlines()):
                stdscr.addstr(idx, max((term_width - len(line)) // 2, 0), line)
        
        stdscr.addstr(shutil.get_terminal_size().lines - 1, 0, "> " + input_text)
        stdscr.refresh()
        
        ch = stdscr.get_wch()  # get a wide character
        
        if ch == '\n':  # Enter pressed
            if input_text.strip():
                speak(input_text)
            input_text = ""
        elif ch in ('\x7f', '\b', curses.KEY_BACKSPACE):  # handle backspace
            input_text = input_text[:-1]
        elif ch == '\x1b':  # ESC to quit
            break
        else:
            if isinstance(ch, str) and ch.isprintable():
                input_text += str(ch)

curses.wrapper(main)
