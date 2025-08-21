import pyttsx3
import random 
import speech_recognition
import pyautogui
import webbrowser
import datetime
import time
import os

# initialize the speech engine

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    # Takes voice from the user and return the query
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 100)

    try:
        print("Understanding........")
        query = r.recognize_google(audio, language = "en-in")
        print(f"You said : {query}")

    except Exception as e:
        speak("say that again, please.....")  
        return "none"
    return query

if __name__ == "__main__":
    speak("Hello I am your virtual assistent. How can i help you")       

    while True:
        query = TakeCommand().lower()

        if "hello" in query:
            speak("Hello sir, How are you?")

        elif "open notepad" in query:
            speak("Opening Notepad, sir")
            os.system("notepad")

        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "").replace("jarvis", "")
            speak("You told me " + rememberMessage)
            with open("Remember.txt", "a") as remember:
                remember.write(rememberMessage)   

        elif "what do you remember" in query:
            with open("Remember.txt", "r") as remember:
                speak("You told me " + remember.read())        

                
        elif "open youtube"  in query: 
            webbrowser.open("https://www.youtube.com")



