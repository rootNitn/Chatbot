import threading
from tkinter import *
import pyttsx3
import string
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from internet import *
import os
from numpy import random
engine=pyttsx3.init ('sapi5')
voices=engine.getProperty ('voices')
rate=engine.getProperty ('rate')
if len(voices) == 3:
    engine.setProperty ('voice', voices[2].id)
elif len(voices) == 2:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty ('voice', voices[0].id)
engine.setProperty ('rate', rate)

#for voice change
def voice():
    speak ("male or female voice")
    quray=takecommand ().lower ()
    if 'male' in quray:
        engine.setProperty ('voice', voices[0].id)
    elif 'female' in quray:
        engine.setProperty ('voice', voices[1].id)

def speak(audio):
    megs.insert (END, audio)
    #megs.configure (justify = RIGHT)
    megs.see (END)
    #print (audio)
    engine.say (audio)
    engine.runAndWait ()

def wishme():
    hour=int (datetime.datetime.now ().hour)
    if hour >= 5 and hour < 12:
        speak ("Good Morning")

    elif hour >= 12 and hour < 18:
        speak ("Good Afternoon")

    else:
        speak ("Good Evening")

    speak ("My name is angel. how can i help you")
def cmd():
    speak ("opened cmd tell me command")
    while True:
        qurey=takecommand ().lower ()
        if 'exit' in qurey:
            break
        else:
            os.system (qurey)

def note():
    speak ("tell me what you take note")
    qurey=takecommand ().lower ()
    file1=open ("file//nitin.txt", "a")
    L=[qurey]
    file1.writelines (L+"/n")
    file1.close ()  # to change file access modes
def longnote():
    speak ("tell me what you take note")
    file1=open ("file//longnote.txt", "a")
    while True:
        qurey=takecommand ().lower ()
        L=[qurey]
        file1.writelines (L)
        file1.close ()  # to change file access modes

# user information like father
def infor(qw):
    ko=list (string.ascii_lowercase)
    file1=open ("file//"+qw+".txt", "r+")
    kk=file1.read ()
    file1.seek (0)
    km=file1.read (1)
    file1.seek (0)
    if km in ko:
        file1=open ("file//"+qw+".txt", "r+")
        kk=file1.read ()
        speak ("your "+qw+" name is "+ kk)
        #speak (kk)
    else:
        file1=open ("file//"+qw+".txt", "w")
        speak ("i don't know your "+qw+" name please tell me your father name")
        qurey=takecommand ().lower ()
        file1.write (qurey)
        file1.close ()
        speak ("name is save for future")




def gf():
    ko=list (string.ascii_lowercase)
    file1=open ("file//gf.txt", "r+")
    kk=file1.read ()
    file1.seek (0)
    km=file1.read (1)
    file1.seek (0)
    if km in ko:
        file1=open ("file//gf.txt", "r+")
        kk=file1.read ()
        speak ("your girl friend name is ")
        speak (kk)
    else:
        file1=open ("file//gf.txt", "w")
        speak (
            "i don't know your girl friend name i thnik i am your girl friend but please tell me your girl friend name")
        qurey=takecommand ().lower ()

        if "my girl friend name" in qurey:
            qurey=qurey.replace ("my girl friend", "")

        file1.write (qurey)
        file1.close ()
        speak ("name is save for future but angel is best for you")
        qurey=takecommand ().lower ()
        if 'why angel is best for me' in qurey or 'why you best for me' in qurey:
            speak ("i never break your trust ")
        else:
            return


def rmuser(x):
    file1=open (x, "w")
    file1.write ("")
    file1.close ()
    speak ("your name has been removed")


def hello(x):
    my_file=open (x, "r")
    content=my_file.read ()
    content_list=content.split (",")
    my_file.close ()
    random.shuffle (content_list)
    speak (content_list[0])


def find_files(filename, search_path):
    list=[]

    # Wlaking top-down from the root
    for dirpath, dirnames, filenames in os.walk (search_path):
        y=map (str.lower, filenames)
        for filename in [f for f in y if f.endswith (filename)]:
            x=os.path.join (dirpath, filename)
            print (x)
            list=x


def takecommand():
    r=sr.Recognizer ()
    with sr.Microphone () as source:
        print ("Listening.....")
        megs.insert (END, "Listening.....")
        r.adjust_for_ambient_noise (source)
        r.pause_threshold=1
        audio=r.listen (source)

    try:
        print ("Recognizering")
        while True:
            if check_internet ():
                break
            else:
                speak ("please connect internet otherwise code will not run properly")
        qurey=r.recognize_google (audio, language="en-IN")
        megs.insert (END, qurey)
        megs.see (END)
        print (f"User said: {qurey}\n")
    except Exception as e:
        print ("say that again pleage...")
        megs.insert (END, "say that again pleage...")
        megs.see (END)
        return "None"
    return qurey

def takeinput():
    qurey = input()
    return qurey

def call(qurey):

        #qurey=takecommand ().lower ()
        # qurey = input_take().lower()
        if 'wikipedia' in qurey:
            speak ('Searching wikipedia...')
            qurey=qurey.replace ("wikipedia", "")
            results=wikipedia.summary (qurey, sentences=3)
            speak ("According to wikipedia")
            speak (results)
        elif 'open website' in qurey:
            speak("tell me website website name")
            qurey=takecommand().lower()
            x = qurey
            speak("tell me subdomain name")
            qurey=takecommand().lower()
            if 'no subdomain name' in qurey:
                y = 'none'
            else:
                y=qurey
            speak ("tell me domain name")
            qurey=takecommand().lower ()
            z=qurey
            if y == 'none':
                webbrowser.open (x + "." + z)
            else:
                webbrowser.open(x+"."+y+"."+z)
        elif 'open google' in qurey:
            webbrowser.open ("google.com/")
            input("please press the enter key to continuous")

        elif 'google' in qurey:
            qurey=qurey.replace ("google", "")
            webbrowser.open ("https://www.google.com/search?q=" + qurey + "&start=")
            input ("please press the enter key to continuous")
        # for hello like database
        elif 'good morning' in qurey:
            hour=int (datetime.datetime.now ().hour)
            if hour >= 5 and hour < 12:
                speak ("Good Morning")
            elif hour >= 12 and hour < 18:
                speak ("no it is morning not Afternoon")
            else:
                speak ("no it is morning not Good Evening")
        elif 'good afternoon' in qurey:
            hour=int (datetime.datetime.now ().hour)
            if hour >= 5 and hour < 12:
                speak ("no it is afternoon not Morning")
            elif hour >= 12 and hour < 18:
                speak ("good Afternoon")
            else:
                speak ("no it is afternoon not Evening")
        elif 'good evening' in qurey:
            hour=int (datetime.datetime.now ().hour)
            if hour >= 5 and hour < 12:
                speak ("no it is evening not Good morning")
            elif hour >= 12 and hour < 18:
                speak ("no it is evening not Afternoon")
            else:
                speak ("Good Evening")
        elif 'hello how are you' in qurey:
            speak ("i am fine sir")
        elif 'hello' in qurey or 'hi' in qurey:
            # print("hello sir how can i help you")
            hello ("file//hello.txt")
        elif 'how are you' in qurey or 'aap kaise hai' in qurey:
            hello ("file//how.txt")
            # speak("i am fine sir and you sir ")
        elif 'i am fine' in qurey or 'm tik hu' in qurey:
            hello ("file//fine.txt")
            # speak("well how can i help you")
        elif 'thank you' in qurey or 'welldone' in qurey or 'smart' in qurey:
            hello ("file//thank.txt")
            # speak("welcome sir i am ever ready for helping you")
        # for about the author
        elif 'who are you' in qurey or 'kaun ho tum' in qurey or 'tum kaun ho' in qurey or 'who the hell are you' in qurey or 'tell me youself' in qurey or 'what is ypur name' in qurey:
            hello("file//who.txt")
            #speak ("i am ai base software and my name is angel. what can i do for you")
        elif 'what you do for me' in qurey or 'tell me feature' in qurey:
            # hello("dome.txt")
            speak (
                "i can tell a joke. i can open any software which you install your computer.i play music. i can serach in wikipedia. you can run command pormt command with me.i can search any file on local computer. i can open any any file any foler.for all of these things read the command text file for open command text tell 'help' ")
        # something other
        elif 'fuck you' in qurey or 'asshole' in qurey:
            hello ("file//abuse.txt")
            # speak("sir please don't abuse")
        elif 'i love you' in qurey or 'love you' in qurey:
            hello ("file//love.txt")
            # speak("love you too sir. i fell in love with you")
        elif 'i hate you' in qurey or 'hate you' in qurey:
            hello ("file//hate.txt")
            # speak("but sir i love you. you are the nice human")
        # computer function
        elif 'write note' in qurey or 'take note' in qurey or 'take short note' in qurey:
            note ()
        elif 'read note' in qurey or 'open note' in qurey:
            file1=open ("file//nitin.txt", "r+")
            kk=file1.read ()
            print ("Output of Read function is ")
            print (kk)
            speak (kk)
        elif 'open youtube' in qurey:
            webbrowser.open ("youtube.com")
            input ("please press the enter key to contious")

        elif 'open github' in qurey:
            webbrowser.open ("github.com")
            input ("please press the enter key to contious")

        # app setteing
        elif 'change voice' in qurey:
            voice ()
        # MUSIC


        elif 'time' in qurey:
            strtime=datetime.datetime.now ().strftime ("%H:%M:%S")
            print (strtime)
            speak (f"sir, time is {strtime}")
        elif 'online play song' in qurey:
            speak("tell me song name")
            po = takecommand().lower()
            import urllib.request

            from bs4 import BeautifulSoup
            def nitin (textToSearch):
                query = urllib.parse.quote (textToSearch)
                urlq = "https://gaana.com/search/" + query
                response = urllib.request.urlopen (urlq)
                html = response.read ()
                return html
                #soup = BeautifulSoup (html, 'html.parser')
            out = nitin(po)
            soup = BeautifulSoup (out, 'html.parser')
            for link in soup.find_all (attrs = {'media': 'handheld'}):
                q = (link.get ('href'))
                print (q)
                urlq = q
                response = urllib.request.urlopen (urlq)
                html = response.read ()
                soup = BeautifulSoup (html, 'html.parser')
            v = soup.findAll (attrs = {'class': 'imghover'})
            list = []
            for link in v:
                a = (link.get ('href'))
                list.append ("www.gaana.com" + a)
            matching = [s for s in list if "song" in s]
            print (matching)
            webbrowser.open (matching[0])



        elif 'open chrome' in qurey:
            path='C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile (path)
        elif 'quit' in qurey:
            speak ("bye sir have you nice day see you soon")
            os._exit (0)
        elif 'close chrome' in qurey:
            os.system ('cmd /c "TASKKILL /IM chrome.exe"')
        elif 'shutdown computer' in qurey:
            os.system ('cmd /c "shutdown/s"')
            os._exit (0)
        elif 'open cmd' in qurey or 'cmd' in qurey:
            while True:
                cmd ()
                if 'exit cmd' in qurey or 'close cmd' in qurey:
                    break

            # personal information
        elif 'what is my father name' in qurey or 'my father name' in qurey:
            infor("father")
        elif 'what is my mother name' in qurey or 'my mother name' in qurey:
            infor("mother")
        elif 'what is my sister name' in qurey or 'my sister name' in qurey:
            infor("sister")
        elif 'what is my brother name' in qurey or 'my brother name' in qurey:
            infor ("brother")
        elif 'what is my girlfriend name' in qurey or 'my girlfriend name' in qurey:
            gf ()
        elif 'remove my father name' in qurey or 'delete my father name' in qurey or 'remove father name' in qurey:
            rmuser ("father.txt")
        elif 'remove my mother name' in qurey or 'delete my mother name' in qurey or 'remove mother name' in qurey:
            rmuser ("mother.txt")
        elif 'remove my sister name' in qurey or 'delete my sister name' in qurey or 'remove sister name' in qurey:
            rmuser ("sister.txt")
        elif 'remove my girl friend name' in qurey or 'delete my girl friend name' in qurey or 'remove girl friend name' in qurey:
            rmuser ("gf.txt")


        elif 'bye' in qurey or 'close' in qurey:
            hour=int (datetime.datetime.now ().hour)
            if hour >= 0 and hour < 5:
                speak ("good night sir.bye sir have you nice day see you soon")
            else:
                speak ("bye sir have you nice day see you soon")
            os._exit (0)
        else:
            if "none" in qurey:
                speak("i can't understand what you want to say you can write it.")
                #qurey = input("YOU -")
                #continue

            else:
                results=wikipedia.summary (qurey, sentences=1)
                speak (results)
class Task(threading.Thread):
    def __init__(self, master, task):
        threading.Thread.__init__(self, target=task, args=(master,))

        if not hasattr(master, 'thread_enviar') or not master.thread_enviar.is_alive():
            master.thread_enviar = self
            self.start()

def nitin(*args):
        name1 = a.get ()
        # apps.append (name1)
        # tk.append (name1)
        megs.insert (END, name1)
        #megs.configure (justify = LEFT)

        megs.see (END)
        textf.delete (0, 'end')
        call(name1)
def script():
    quray = takecommand ().lower ()
    call (quray)
    stop.set ()


def fecth():
    t1 = threading.Thread (target = script)
    t1.daemon = True
    t1.start ()



main = Tk()
a = StringVar()
main.geometry ("500x650")
#main.maxsize(500,650)
main.resizable(0,0)
main.title ("Angel")
stop = threading.Event()
frame = Frame (main)
sc = Scrollbar (frame)
sk = Scrollbar(frame, orient=HORIZONTAL)


from tkinter import font
sf= font.Font(family='times', size=16, weight='bold')
megs = Listbox (frame,bg="#ffffff", width = 80, height = 20,font=sf,  yscrollcommand = sc.set, xscrollcommand = sk.set, selectbackground="Red",highlightcolor="Red")
sc.pack (side = RIGHT, fill = Y)
sc.config( command = megs.yview )
sk.pack(side = BOTTOM, fill = X)
sk.config( command = megs.xview )
megs.pack (side = LEFT, fill = BOTH, pady = 10)
frame.pack ()
textf = Entry (main, font = ("verdana", 20), textvariable = a)
textf.pack (fill = X, pady = 10)
textf.bind('<Return>', nitin)




btn = Button (main, text = "speak", font = ("verdana", 20), command=fecth)
btn.pack ()

main.mainloop ()

