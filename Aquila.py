import random
import json
import torch
import tkinter as tk
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import datetime
import wolframalpha

import weathercom
import pywhatkit
from AttendanceProject import DetectFace 
import weathercom
from whatsapp import send_msg
import requests


wfApi = wolframalpha.Client("4T29P8-8YG5X68HE4")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145 )

# rishi = '+91 8961502488'
# mom = '+91 8582941433'
# me = '+91 9831169844'
# hour = datetime.datetime.now().hour
# timeMin = datetime.datetime.now().minute+1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.energy_threshold = 300 
        # print('listening...')
        audio = r.listen(source)
    try:
        # print("Recongnizing...")
        query = r.recognize_google(audio, language= 'en-US')
        print(query)
    except Exception:
        pass
        return 'None'
    return query

def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase

# def alarmClock():

#     import time
#     from playsound import playsound
#     from datetime import datetime
#     alarmtime = '05:35'
#     while True:
#         lclTime = datetime.now().strftime('%H:%M')
#         if lclTime == alarmtime:
#             playsound("alarm.mp3")
#             # if query == 'stop':
#             break

#         else:
#             break

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        # alarmClock()
        speak("good morning")
        print("good morning")
        # humidity, temp, phrase = weatherReport('patna')
    # if hour >= 0 and hour < 7:
    #         print(f'currently in patna temperature is {temp} degree celsius, humidity is {humidity} percent and sky is {phrase}')
    #         speak(f'Currently in patna temperature is {temp} degree celsius, humidity is {humidity} percent and sky is {phrase}')
    #         speak("Looks like I have got some latest news, shall I start the day with it")
    elif hour >= 12 and hour < 16:
        speak("good afternoon")
        print("good afternoon")
    else:
        speak("good evening")
        print("good evening")

def searchInt(sen, tagEquals):
    import nltk
    global results
    ignore = ['when', 'calculate', 'did', 'who', 'which', 'what', 'how', 'is', 'was', 'are', 'why', 'where', 'i', 'you', 'me', "youtube", "on", "play", "online", "search", "send", "message", "to", "whatsapp"]
    # print(ignore)
    words_for_search = []

    sentokenize = nltk.word_tokenize(sen)
    for s in sentokenize:
        if s not in ignore:
            words_for_search.append(s)
    results = " ".join(words_for_search).replace(', ', " ")

def actions(no):
    global e 
    running = True
    while running:
        # query = take_command().lower()
        if no == 1:
            command = take_command().lower()
        elif no == 2:
            command = input("YOU: ")
        sentence = tokenize(command)
        # sentence = tokenize(query)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]
        
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    resp = f" {random.choice(intent['responses'])}"
                    print(f"{bot_name}: {resp}")
                    speak(resp)

            # if tag == 'offmusic':
            #     music_dir = 'C:\\Users\\maaza\\Music'
            #     songs = os.listdir(music_dir)
            #     rd = random.choice(songs)
            #     print(rd)
            #     speak(rd)
            #     os.startfile(os.path.join(music_dir, rd))

            if tag == "openYT":
                webbrowser.open("youtube.com")
            
            elif tag == "openWhatsapp":
                webbrowser.open("web.whatsapp.com")

            elif tag == 'time':
                strTime = datetime.datetime.now().strftime("%H:%M")
                print(strTime)
                speak(strTime)

            elif tag == 'openedge':
                edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edgePath)

            elif tag == 'playYT':
                searchInt(command, 'playYT')
                pywhatkit.playonyt(results)

            elif tag == 'wikipedia':
                try:
                    answers = wikipedia.summary(command, sentences=2)
                    print(answers)
                    speak(answers)
                except Exception:
                    pywhatkit.search(command)

            elif tag == "temperature":
                # searchInt(command, 'search')
                try:
                    res = wfApi.query(command)
                    print(next(res.command).text)
                    speak(next(res.command).text)
                except Exception:
                        pywhatkit.search(command)

            elif tag == "webImage":
                try:
                    pywhatkit.search(command)
                except Exception:
                    print("something went wrong")
                    speak("something went wrong")
                    

            elif tag == 'search':
                searchInt(command, 'search')
                try:
                    res = wfApi.query(results)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except Exception:
                    try:
                        answers = wikipedia.summary(command, sentences=2)
                        print(answers)
                        speak(answers)
                    except Exception:
                        pywhatkit.search(command)

            elif tag == 'sendWhatsapp':
                searchInt(command, 'sendWhatsapp')
                send_msg(results)

            elif tag == 'myLoc':
                # try:
                ipAdd = requests.get('https://api.ipify.org').text
                # print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # city = geo_data['city']
                country = geo_data['country']
                # print(f"I think, we are at city {city} in {country}")
                # speak(f"I think, we are at city {city} in {country}")
                print(f"I think, we are at city Patna in {country}")
                speak(f"I think, we are at city Patna in {country}")
                # except:
                #     print("I think some error occured")

            elif tag == "closeEdge":
                try:
                    os.system('TASKKILL /F /IM msedge.exe')

                except:
                    print("Error while closing program")
            
            elif tag == "shutdownPC":
                import time
                print("please wait...")
                time.sleep(20)
                # print("shut down")
                try:
                    os.system('shutdown /s')

                except:
                    print("Error while shutting down")
            
            elif tag=='detectFace':
                DetectFace()

            elif tag=='chatInTerminal':
                e = 'notexit'
                running = False

            elif tag=='speakChat':
                e ='notexit'
                running = False

            elif tag == 'quit':
                running = False
                mainRun = False
                e = 'exit'
                

        else:
            print(f"{bot_name}: I do not understand...")


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Aquila"
wishme()
# mainRun = True
while True:
    actions(2)

    if e == 'notexit':
        actions(2)

    if e == 'exit':
        print("closing")
        break

    

    # names = ["aquila", "koyla", "akola", "akila", "kola"]
    # for name in names:
    #     if name in query:
    #     # if name in Input:
    #         print("listening")
 
    #         actions()
            