import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# taking voice from my system
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)

engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 100)

#speak function

def speak(text):
    """this function takes text and returns voice

Args:
    text (_type_): string
"""
    engine.say(text)
    engine.runAndWait()
    

# speech recognition function
def takecommand():
    """this function will recognize voice and return text
    """  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")  
        r.pause_threshold = 1
        audio = r.listen(source)
    
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}/n")
    
        except Exception as e:
            print("say it again...")
            return "None"
        return query
    
text = takecommand()
speak(text)
