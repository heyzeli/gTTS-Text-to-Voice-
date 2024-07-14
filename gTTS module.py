#gTTS is the external module which help to convert text into speech
from gtts import gTTS
import os

text = "Hey bro what do you do? Ahnnnnnn"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
os.system("open output.mp3")  

