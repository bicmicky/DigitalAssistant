import speech_recognition as sr
import time
import os
from gtts import gTTS
import playsound
import webbrowser
import requests,json
import datetime
from datetime import datetime
import re
import wikipedia


def speak(text):
    tts = gTTS(text=text,lang="en")
    date = datetime.now()
    filename = "D:\Python Practise\Speech Recognition Project\Audio/voice"+ str(date).replace(":","-") +".mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))

    return said

listening = True
while listening == True:

    text = get_audio()

    if text.count("python") > 0:
        speak("I am ready")
        text = get_audio()

        if "hello" in text:
            speak("hello, how are you?")

        if "what is your name" in text:
            speak("My name is Shipra Seth!")

        if "where is" in text:
            data = text.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(data[2])
            speak("Hold on Soumik, I will show you where " + data[2] + " is.")
            webbrowser.open(location_url, new=2)

        if "what is the weather in" in text:
            listening = True
            api_key = "974aa629c7d9a032f585232d79ef8d6c"
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            data = text.split(" ")
            location = str(data[5])
            url = weather_url + "appid=" + api_key + "&q=" + location + "&units=metric"
            js = requests.get(url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temp = weather["temp"]
                hum = weather["humidity"]
                desc = js["weather"][0]["description"]
                resp_string = "Here is the weather in " + str(data[5]) +": The temperature is " + str(temp) + "° Celsius, the humidity is " + str(hum) + "% ,and the weather description is "+ str(desc) + "."
                print(resp_string)
                speak(resp_string)
                webbrowser.open(url, new=2)
            else:
                speak("City Not Found")
        if "bye bye" in text:
            listening = False

        if "what is the time" in text:
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %h:%M:%S")
            speak("The time is " + str(current_time))

        if "play" in text:
            data = text.split(" ")
            url = "https://www.youtube.com/results?search_query=" + "+".join(data[1:])
            r = requests.get(url).text
            match = re.findall('watch\?v\=(\S{11})',r)
            video_url = "https://www.youtube.com/watch?v=" + match[0]
            webbrowser.open(video_url, new=2)

        if "who is" in text:
            data = text.split(" ")
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
            url = "https://www.google.com/search?q=" + "+".join(data[2:])
            r = requests.get(url,headers=headers).text
            match = re.findall('Uo8X3b\"\>Description\<\/h2\>\<span\>([^<]+)',r)
            speak("According to wikipedia " + match[0])
<<<<<<< HEAD
=======
print('Hello')
>>>>>>> parent of c25ee78... Latest commit to add useless print statement
