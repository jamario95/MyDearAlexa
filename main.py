import sys

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import subprocess
#from gtts import gTTS
import requests
import json
import os
import webbrowser



r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#function to make alexa speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

#function that take user command
def take_command():
    with sr.Microphone() as source:

        audio = r.listen(source)
        said = ""
        try:

            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))

    return said

#replays of Alexa
def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:   #play on youtube
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'go to hell' in command:
        talk(' No, fuck you!')

    elif 'time' in command: #what time is it?
        hour = datetime.datetime.now().strftime('%I:%M %p')
        print(hour)
        talk(hour)

    elif 'search' in command: #Search in wikipedia
        person = command.replace('search', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command: #tells a joke
        talk(pyjokes.get_joke())

    elif "where is" in command: #search in google maps
        command = command.replace("where is", "")
        location = command
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.pl/maps/search/" + location + "")

    # elif "what is the weather in" in command:
    #
    #     api_key = "AIzaSyBIv95OO5tLTXiNPe8q05yB1lFCVGyBirQ"
    #     base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
    #     talk(" City name ")
    #     print("City name : ")
    #     city_name = take_command()
    #     print(city_name)
    #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
    #     response = requests.get(complete_url)
    #     x = response.json()
    #
    #     if x["cod"] != "404":
    #         y = x["main"]
    #         current_temperature = y["temp"]
    #         current_pressure = y["pressure"]
    #         current_humidiy = y["humidity"]
    #         z = x["weather"]
    #         weather_description = z[0]["description"]
    #         print(" Temperature (in kelvin unit) = " + str(
    #             current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
    #             current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(
    #             weather_description))


    elif "don't listen" in command or "stop listening" in command:  #Stops listening
        talk("for how much time you want to stop me from listening commands")
        a = int(take_command())
        time.sleep(a)
        talk('I am back baby')


    elif 'hello' in command:
        talk('Hello! I am Alexa. How can I help you?')

    elif 'shutdown' in command: #shutdown aplication
        talk('Later Nerd!')
        sys.exit(0)


    else:
        print('Sorry I dont understand')
        talk('Sorry I dont understand')


while True:
    run_alexa()
