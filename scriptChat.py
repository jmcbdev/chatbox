import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
from threading import Thread
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]



if r.recognize_google(audio) in greetings:
       random_greeting = random.choice(greetings)
       print(random_greeting)
       engine.say(random_greeting)
       engine.runAndWait()
elif r.recognize_google(audio) in question:
       engine.say('I am fine')
       engine.runAndWait()
       print('I am fine')
else:
    # engine.say('I do not understand the question')
    # engine.runAndWait()
    # print('I do not understand the question')

   engine.say("please wait")
   engine.runAndWait()
   print(wikipedia.summary(r.recognize_google(audio)))
   engine.say(wikipedia.summary(r.recognize_google(audio)))
   engine.runAndWait()
   userInput3 = input("or else search in google")
   webbrowser.open_new('www.google.com/search?q=' + userInput3)


def user_input():
    global query
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something..")
        audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")

        except LookupError:
            print("Sorry could not recognize your voice.")

def main_windon():
      global query
      while True:
          if query != None:
              if 'shutdown' in query or 'quit' in query or 'stop' in query or 'goodbye' in query:
                  shut_down()
              else:
                  web_scraping(query)
                  query = None
