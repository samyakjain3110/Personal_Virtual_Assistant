import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import urllib

def setup():
    global engine 
    engine = pyttsx3.init('sapi5')
    global voices 
    voices = engine.getProperty('voices')

def internet_on():
    print('entered internet_on')
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except Exception: 
        return False    

'''
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice') 
print(rate)
print(volume)
print (voice)
'''

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")   
    else:
        speak("good evening")

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.energy_threshold = 10
    
    print(r.energy_threshold)
    with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source,duration=1)
         print("listening...")
         audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("user said:",query)
    except Exception:
        print("pardon") 
        speak("pardon")  
        return "None" 
    return query

if __name__ == "__main__":
    internet_check = internet_on()      #checks whether internet is running or not
    if internet_check == False:
        print('please check the internet connection') 
        exit()
    setup()
    wish()
    while True :
        query = takeCommand().lower()
 
        if 'hey siri' in query:                               #just removing the unnecessary words 
            query = query.replace("hey siri","")
        if 'bye siri' in query :                              #exitting the application
            exit()

        if 'search wikipedia' in query:                       #function for wikipedia search
            speak("searching...")
            query = query.replace("search wikipedia","")
            print(query)
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
        elif 'open code' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
