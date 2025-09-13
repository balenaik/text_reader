import subprocess

def speak(text):
    # HDMIに出力する場合
    subprocess.run(['espeak', '-v', 'en-us', '-w', '/tmp/tmp.wav', text])
    subprocess.run(['aplay', '-D', 'plughw:0,0', '/tmp/tmp.wav'])

while True:
    user_input = input("Type something (or 'exit' to quit): ")
    
    if user_input.lower() in ['exit', 'quit']:
        break

    if user_input.strip() != "":
        speak(user_input)