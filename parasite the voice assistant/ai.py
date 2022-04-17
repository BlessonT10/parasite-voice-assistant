import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import pywhatkit as kit
import requests 
from playsound import playsound
from googletrans import Translator
import time as t
from gtts import gTTS
import PIL.ImageGrab
import pyautogui
from cv2 import cv2
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searcho(trsd):
    kit.playonyt(trsd)

def trans(transhi):   
    if 'translate in hindi' in transhi:  
        translator = Translator() 
        from_lang = 'en'
        to_lang = 'hi'
    print("Phase to be Translated :"+ transhi)  
    text_to_translate = translator.translate(transhi,  
                                                     src= from_lang, 
                                                     dest= to_lang) 
    text = text_to_translate.text  
    speak = gTTS(text=text, lang=to_lang, slow= False)   
    speak.save("captured_voice.mp3")      
    os.system("start captured_voice.mp3") 

def searchg(sear):
    kit.search(sear)

def time1():
    Time = datetime.datetime.now().strftime("%I:%M")
    speak(Time)

def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query1 = r.recognize_google(audio,language='en-in')
        print(query1)

    except Exception as e:
        print(e)
        return "None"
    return query1


def camera41():
    cap=cv2.VideoCapture(0)
    while True:
        ret,img=cap.read()
        cv2.imshow('webcam',img)
        k=cv2.waitKey(10)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows() 

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def greet():
    speak("initializing parasite")
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        playsound('E:\\Desktop\\aisounds\\zapsplat_science_fiction_robot_power_up_initiate_ascend_60616.wav')
    #elif hour >=12 and hour < 22:
        #playsound('E:\\Desktop\\aisounds\\zapsplat_science_fiction_robot_power_up_initiate_ascend_60616.wav')
    speak("setting up everything")
    t.sleep(2)
    r=random.randint(1,100)
    speak("{} percent initialized".format(r))
    if hour >= 6 and hour < 12:
        speak("good morning sir")
    elif hour >=12 and hour < 18:
        speak("good afternoon sir ")
    elif hour >=18 and hour < 24:
        speak("good evening sir")
    else:
        speak("time for the sleep.")
        speak("good night!")
        exit(0)
    speak("welcome back")
    speak("you can call my name for any help sir")
    

def weather1():
    api_key="9b7ed6f34aec3aac99d23345277188cc"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    city_name=takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]-273.15
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in celsius is " +
                str(current_temperature) +
                "\n humidity in percentage is " +
                str(current_humidiy) +
                "\n description  " +
                str(weather_description))
        print(" Temperature in celsius unit = " +
                str(current_temperature) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                str(weather_description))
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("reapeat once again")
        return "none"
    return query

def main():
    n=0
    #greet()
    while True:
        call1=takeCommand1().lower()
        if 'parasite' in call1:
            speak("yes sir")
            while True:
                query=takeCommand().lower()
                if(('wikipedia' in query) or ('search' in query)) :
                    speak("searching wikipedia.....")
                    results=wikipedia.summary(query,sentences=2)
                    playsound('E:\\Desktop\\aisounds\\processing.wav')
                    speak("according to wikipedia")
                    speak(results)
                elif 'open youtube' in query:
                    playsound('E:\\Desktop\\aisounds\\processing.wav')
                    speak("opening youtube")
                    webbrowser.open("youtube.com")
                elif 'open google' in query:
                    playsound('E:\\Desktop\\aisounds\\processing.wav')
                    speak("opening google")
                    webbrowser.open("google.com")
                elif 'the time' in query:
                    time1()
                elif 'the date' in query:
                    date()
                elif 'open steam' in query:
                    playsound('E:\\Desktop\\aisounds\\processing.wav')
                    speak("opening steam")
                    steampath="C:\\Program Files (x86)\\Steam\\Steam.exe"
                    os.startfile(steampath)
                elif 'what is your name' in query:
                    if n<1:
                        list1=["my name is parasite","i'm parasite","parasite","my creator call me parasite"]
                        speak(random.choice(list1))
                        n=n+1
                        print(n)
                    else:
                        speak(random.choice(list(open('E:\\Desktop\\aisounds\\name.txt'))))
                        speak("you already know my name")
                        speak("your just playing with me i know")
                        speak("i won't tell my name")
                elif 'camera' in query:
                    speak("opening camera")
                    t.sleep(1)
                    camera41()
                elif 'who made you' in query:
                    speak("a lazy developer created me ")
                elif 'you robot' in query:
                    speak("do your work you child")
                elif 'open bible'in query:
                    webbrowser.open('https://www.bible.com/')
                elif ' in google' in query:
                    searchg(query)
                elif 'your qualification' in query:
                    speak("LKG")
                elif 'in youtube' in query:
                    searcho(query)
                elif 'my birthday' in query:
                    speak('10 feb 2000')
                elif 'shutdown' in query:
                    os.system("shutdown /s /t 5")
                elif 'weather' in query:
                    weather1()
                elif 'translate' in query:
                    trans(query)
                elif 'make a note' in query:
                    speak("what should i take down sir")
                    f=open('E:\\Desktop\\aisounds\\note.txt','w')
                    writ=takeCommand1().lower()
                    f.write('writ')
                elif 'no' in query:
                    speak("it was my pleasure to serve you")
                    break
                elif 'stop' in query or 'rest' in query:
                    speak('okay sir')
                    print('okay sir')
                    speak('have a nice day')
                    print('have a nice day')
                    exit(0)
                elif 'song' in query:
                    f=open('E:\\Desktop\\aisounds\\song.txt','r')
                    speak(f.read())
                elif 'Nitin' in query:
                    if 'who is Nitin' in query:
                        speak("he is a professional gamer and developer")
                    else:
                        f=open('E:\\Desktop\\aisounds\\nithin.txt','r')
                        speak(f.read())
                elif 'screenshot' in query:
                    speak("what would be the photo name sir")
                    name=takeCommand().lower()
                    s=pyautogui.screenshot()
                    speak("taking screenshot")
                    s.save(f'E:\\Desktop\\screen\\{name}.png')
                speak("any commands for me sir")            
                       
main()