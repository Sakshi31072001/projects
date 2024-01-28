import datetime
import os
import smtplib
import webbrowser
import cv2
import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import requests
import json
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')



def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am vision master. Please tell me how may I help you")



def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 3
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query









if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        if 'joke' in query:
             joke = pyjokes.get_joke()
             speak(joke)
             print()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Administrator\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
           strTime = datetime.datetime.now().strftime("% H:% M:% S")
           speak(f"Sir, the time is {strTime}")

        elif 'power point presentation' in query:
           speak("opening Power Point presentation")
           power = r"C:\\Users\\Administrator\\Downloads\\vision desktop assistant ppt2.pptx"
           os.startfile(power)

        elif "Temperature" in query:
            search = "temperature in pune"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"The temperature outside is {temperature} celcius")

        elif 'open notepad' in query:
            speak("okay master")
            npath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            os.startfile(npath)

        elif 'open command prompt' in query:
            speak("okay master")
            os.system("start cmd")

        elif 'open camera' in query:
            speak("okay master")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            datetime.time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'news' in query:
                api_dict = {
                    "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=55bd4e4e3be443d298791ab74afe3758",
                    "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=55bd4e4e3be443d298791ab74afe3758",
                    "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=55bd4e4e3be443d298791ab74afe3758",
                    "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=55bd4e4e3be443d298791ab74afe3758",
                    "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=55bd4e4e3be443d298791ab74afe3758",
                    "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=55bd4e4e3be443d298791ab74afe3758"
                    }

                content = None
                url = None
                speak(
                    "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
                field = input("Type field news that you want: ")
                for key, value in api_dict.items():
                    if key.lower() in field.lower():
                        url = value
                        print(url)
                        print("url was found")
                        break
                    else:
                        url = True
                if url is True:
                    print("url not found")

                news = requests.get(url).text
                news = json.loads(news)
                speak("Here is the first news.")

                arts = news["articles"]
                for articles in arts:
                    article = articles["title"]
                    print(article)
                    speak(article)
                    news_url = articles["url"]
                    print(f"for more info visit: {news_url}")

                    a = input("[press 1 to cont] and [press 2 to stop]")
                    if str(a) == "1":
                        pass
                    elif str(a) == "2":
                        break

                speak("thats all")

        elif "temperature" in query:
            search = "temperature in pune"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")







