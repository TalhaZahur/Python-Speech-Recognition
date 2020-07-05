import speech_recognition as sr
import webbrowser
import time
import os
import playsound
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()
 
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:    
            voice_data= r.recognize_google(audio)
            
        except sr.UnknownValurError:
            alexa_speak('Sorry, Can you please repeat again.In didn't get that')
        except sr.RequestError:
            alexa_speak('Sorry, my speech assistance is down')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text = audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'What is your name' in voice_data:
        alexa_speak('My name is Alexa')
    if 'what time is it' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for on the Web?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        alexa_speak('here is what I found for' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        alexa_speak('here is the location of' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
alexa_speak('How can I help you !')
while 1:
    voice_data = record_audio()
    respond(voice_data)

