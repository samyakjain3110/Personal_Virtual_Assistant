import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import urllib
import web_browser_automation ,json_control
import pyautogui




def setup():                                        # basic setup for text to speech
    global engine 
    engine = pyttsx3.init('sapi5')
    global voices 
    voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
    
'''
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice') 
print(rate)
print(volume)
print (voice)
'''
def internet_on():                                  # checks whether internet is running or not
    print('entered internet_on')
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except Exception: 
        return False    

def wish():                                         # wishes the user according to the current time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")   
    else:
        speak("good evening")    

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 1                   # voice input properties can be adjusted 
    r.energy_threshold = 10                 # as per the environment
    
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source,duration=1)
         print("listening...")
         audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        json_control.write_data(query)
        print("user said:",query)
    except Exception:
        print("pardon") 
        speak("pardon")  
        return "None" 
    return query        