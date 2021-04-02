import pyttsx3
import speech_recognition as sp
import smtplib
import datetime
import webbrowser
import os
import shutil
import warnings
import calendar
import random
import wikipedia
from gtts import gTTS


print('Initializing eve')

eg = pyttsx3.init()
v = eg.getProperty('voices')
eg.setProperty('voice', v[0].id)
Sentence = "Hello there"

#the function that helps eve speak
def speak(something):
    eg.say(something)
    eg.runAndWait()

speak(Sentence)



def takecmd():
    
    rec = sp.Recognizer()

    with sp.Microphone() as source:    
    
        print("Listening the fuck up")
        rec.pause_threshold = 1 
        something = rec.listen(source)

        try:
            print("Please wait a minute, I am authenticating your voice")
            query = rec.recognize_google(something, language = 'en-in')
            print(f"User said: {query}\n") 

        except Exception as error: 
            print(error)     
            print("Unable to Recognizing your voice.")   
            return "None"

        return query


def username(): 
    speak("What should i call you sir") 
    global uname 
    uname = takecmd()
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("#####################".center(columns)) 
      
    speak("How can i Help you, Sir") 


def wish():
    
    username()
    h = int(datetime.datetime.now().hour)
    print(h)



    if h >=0 and h <12:
        speak("Good Morning" + uname)
        speak(username)

    elif h >=12 and h <18:
        speak('Good Afternoon' + uname)
        speak(username)

    else: 
        speak("Good Evening" + uname)
        speak(username)

speak("Initializing Eve...")






if __name__ == '__main__': 
    clear = lambda: os.system('clear') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear()
    wish() 
    
    while True: 
          
        query = takecmd().lower() 


    if 'copy spotify' in query: 
            speak("Copying spotify material\n") 
            webbrowser.open("youtube.com") 

    
