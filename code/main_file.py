import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import urllib
import pyautogui

import web_browser_automation ,json_control,basic_funcs,browser_funcs



if __name__ == "__main__":              # main function
    basic_funcs.internet_check = basic_funcs.internet_on()      # checks whether internet is running or not
    if basic_funcs.internet_check == False:
        print('please check the internet connection') 
        exit()
    basic_funcs.setup()
    basic_funcs.wish()
    while True :
        query = basic_funcs.takeCommand().lower()
 
        if 'hey siri' in query:                               #just removing the unnecessary words 
            query = query.replace("hey siri","")
        if 'bye siri' in query :                              #exitting the application
            exit()

        if 'search wikipedia' in query:                       #function for wikipedia search
            basic_funcs.speak("searching...")
            query = query.replace("search wikipedia","")
            print(query)
            result = wikipedia.summary(query,sentences=2)
            basic_funcs.speak(result)
        elif 'open youtube' in query:
            browser_funcs.youtube_search()
        elif 'open google' in query:
            browser_funcs.google_search()
        elif 'open stackoverflow' in query:
            browser_funcs.stackoverflow_search()   
        elif 'open code' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
