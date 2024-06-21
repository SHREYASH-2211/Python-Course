from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    # os.system("start output.mp3")  # For Windows, use "start"
    os.system("afplay output.mp3")  # For macOS, use "afplay"
    # os.system("mpg321 output.mp3")  # For Linux, use "mpg321"

if __name__ == "__main__":
    text = "Hello World"
    text_to_speech(text)