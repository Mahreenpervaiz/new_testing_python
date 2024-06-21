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
engine.setProperty('rate', 150)

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
    
# the function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>-8 and hour<12:
        speak("good morning mehreen. how are you doing")
        
    elif hour>-12 and hour<18:
        speak("good afternoon mehreen. how are you doing")
        
    else:
        speak("good evening mehreen. how are you doing")
        
    speak("i am hania. tell me mama how can i help you")
    

    


if __name__ == '__main__':
    
    wish_me()
    while True:
    
        query = takecommand().lower()

    
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia, ')
            print(query)
            result = wikipedia.summary(query, sentence = 2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        
        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("http://www.youtube.com")
    
    