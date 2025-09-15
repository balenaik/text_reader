import subprocess
import pyfiglet
import os
import shutil

def speak(text):
    subprocess.run([
        "edge-tts",
        "--text", text,
        "--write-media", "/tmp/tmp.mp3"
    ])

    subprocess.run(["mpg123", "-a", "plughw:0,0", "/tmp/tmp.mp3"])

def show_big_text(text):
    os.system("clear")  # clear the terminal
    term_width = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format(text, font="big")
    for line in banner.splitlines():
        print(line.center(term_width))

while True:
    user_input = input("Type something (or 'exit' to quit): ")
    
    if user_input.lower() in ['exit', 'quit']:
        break

    if user_input.strip() != "":
        show_big_text(user_input)
        speak(user_input)
