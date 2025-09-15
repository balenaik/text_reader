import subprocess

def speak(text):
    subprocess.run([
        "edge-tts",
        "--text", text,
        "--write-media", "/tmp/tmp.mp3"
    ])

    subprocess.run(["mpg123", "-a", "plughw:0,0", "/tmp/tmp.mp3"])

while True:
    user_input = input("Type something (or 'exit' to quit): ")
    
    if user_input.lower() in ['exit', 'quit']:
        break

    if user_input.strip() != "":
        speak(user_input)
