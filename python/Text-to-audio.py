from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
# language = 'pt-br'
language = 'en'

sp = gTTS(
    text='my very first audio generated with Python',
    lang=language
)

sp.save(audio)
playsound(audio)
