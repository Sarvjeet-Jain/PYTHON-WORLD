import os
import datetime
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import speech_recognition as sr
from datetime import date


converter= pyttsx3.init('sapi5')
converter.setProperty('rate',150)
#converter.setProperty('volume',0.7)
voices= converter.getProperty('voices')
converter.setProperty('voice', voices[0].id)


def speak(command):
    converter.say(command)
    converter.runAndWait()


def command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Catching....!!")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Getting, Please Wait....!!")
            req= r.recognize_google(audio)
            print(f"Your Requirement : {req} \n")

    except Exception as e:
        print(e)
        speak("Sorry But I could not understand your voice")
        print("Couldn't Get your Voice!!!")
        speak("Can you please tell me your requirement again")
        return "None"
    
    return req

def Welcome():
    print()
    print()
    print("|||||||||||      |||||    |||||      ||||||||||      ||||    ||||       ||||||||          ||||      ||||")
    print("||||    ||||       ||||| ||||           ||||         ||||    ||||      ||||  ||||         ||||||    ||||")
    print("||||     ||||        ||||||             ||||         ||||    ||||      ||||  ||||         |||| ||   ||||")
    print("||||    ||||          ||||              ||||         ||||||||||||      ||||  ||||         ||||  ||  ||||")
    print("|||||||||||           ||||              ||||         ||||    ||||      ||||  ||||         ||||   || ||||")
    print("||||                  ||||              ||||         ||||    ||||      ||||  ||||         ||||    ||||||")
    print("||||                  ||||              ||||         ||||    ||||       ||||||||          ||||      ||||")
    speak("Welcome to the Python World")
    print("\n\n\n                                  Welcome! to the Python World                                          \n\n")
    speak("To move to the LOG IN page press ENTER")
    Enter = input("\n\nPress Enter-")

def wishMe():
    speak("Please log in to the python world")
    speak("Enter your name")
    name = input("Enter your name-")
    speak("Enter your Email")
    email= input("Enter your email address-")
    speak("Enter your password")
    password= input("Enter your password-")
    time= int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good Morning")
        print("\nGood Morning!!")
    elif time>=12 and time<18:
        speak(f"Good Afternoon {name}")
        print(f"\nGood Afternoon!! {name}")
    else:
        speak(f"Good Evening {name}")
        print(f"\nGood Evening!! {name}")
    speak("Here I am Zara for you as your Virtual Assistant.")

def browser():
    speak("Here we have two Browsers for you")
    print("Here we have two Browsers for you-")
    speak("Chrome and Firefox")
    print("1- Chrome\n2- Firefox")
    speak("Enter which Browser may I open for you")
    print("Enter which Browser may I open for you")
    input2 = command()
    if (("chrome" in input2)):
        os.system("chrome")
    else:
        speak("Opening Firefox For you, please wait")
        print("Opening Firefox For you, please wait..")
        os.system("firefox")

def wiki():
    speak("Welcome to the Wikipedia")
    print("Welcome to the Wikipedia!!")
    speak("What you want to search in wikipedia, tell me")
    print("What you want to search in wikipedia, tell me")
    input3= command()
    #speak("Okay, how many sentences you want about")
    #print("Okay, how many sentences you want about "+ input3)
    print("Searching "+ input3 + " in Wikipedia, please wait")
    result = wikipedia.summary(input3, sentences = 2)
    speak("According to Wikipedia ")
    print(f"According to Wikipedia: {result}\n")
    speak(result)

def editor():
    speak("Welcome to the Text Editor world")
    print("Welcome to the Text Editor world")
    speak("Here we have two Text Editors for you-")
    print("Here we have two Text Editors for you-")
    print("1- Notepad\n2- Sublime Text")
    speak("Notepad and Sublime Text")
    speak("Please tell me your Requirement-")
    input5 = command()
    if ("notepad" in input5):
        speak("Opening Notepad for you")
        print("Opening Notepad for you, please wait")
        os.system("notepad")
    else:
        speak("Opening Sublime Text for you")
        print("Opening Sublime Text for you, please wait")
        os.system("sublimetext")

if __name__ == "__main__":
    Welcome()
    wishMe()
    while True:
        speak("Please tell me your Requirement")
        print("Please tell me your Requirement- ")
        req= command().lower()
        if (("dont" in req) or ("don't" in req) or ("do not" in req)):
            print("Okay, I didn't open it!!")
            speak("Okay I didn't open it")
            speak("Press Enter to Continue")
            print("Press Enter to Continue")
            wait = input()

        elif (("browser" in req) or ("internet" in req)):
            browser()
            speak("Press Enter to Continue")
            print("Press Enter to Continue")
            wait = input()

        elif (("wikipedia" in req)):
            wiki()
            speak("Press Enter to Continue")
            print("Press Enter to Continue")
            wait = input()
        
        elif (("editor" in req) or ("text" in req)):
            if (("notepad" in req)):
                speak("Opening Notepad for you")
                print("Opening Notepad for you, please wait")
                os.system("notepad")
            elif (("sublime" in req)):
                speak("Opening Sublime Text for you")
                print("Opening Sublime Text for you, please wait")
                os.system("sublimetext")
            else:
                editor()
            speak("Press Enter to Continue")
            print("Press Enter to Continue")
            wait = input()
            
        elif (("settings" in req)):
            speak("Opening windows Settings for you")
            print("Opening windows Settings for you")
            os.system("start ms-settings:")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("virtual box" in req) or ("oracle" in req)):
            speak("Opening Virtual Box For you, please wait")
            print("Opening Virtual Box For you, please wait")
            os.system("Virtual Box")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("panel" in req)):
            speak("Opening Control Panel for you, please wait")
            print("Opening Control Panel for you, please wait")
            os.system("Control Panel")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif ("terraform" in req):
            speak("Opening Terraform Terminal For you, please wait")
            print("Opening Terraform Terminal For you, please wait")
            os.system("terraform")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()
        
        elif (("eclipse" in req) or ("java editor" in req)):
            speak("Opening Eclipse for you, please wait")
            print("Opening Eclipse For you, please wait")
            os.system("eclipse")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("python" in req)):
            if ("pycharm" in req):
                speak("Opening Pycharm Community for you, please wait")
                print("Opening Pycharm Community for you, please wait")
                os.system("pycharm")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif ("git" in req) or ("bash" in req):
            speak("Opening Git Bash For you, please wait")
            print("Opening Git Bash For you, please wait")
            os.system("git-bash")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("music" in req) or ("windows player" in req)):
            speak("Opening Windows Music Player for you, please wait")
            print("Opening Windows Music Player for you, please wait")
            os.system("wmplayer")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif ("the time" in req):
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            print(f"The time is {time}")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif ("the date" in req):
            today = date.today()
            dt = today.strftime("%B %D, %Y")
            speak(f"The Date is {dt}\n")
            print(f"The date is {dt}")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("visual studio" in req) or ("flutter" in req) or ("dart" in req)):
            speak("Opening Visual Studio Code for you, please wait")
            print("Opening Visual Studio Code for you, please wait")
            os.system("code")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()
        
        elif (("youtube" in req) or ("you tube" in req )):
            speak("Opening You Tube for you, please wait")
            print("Opening You Tube for you, please wait")
            webbrowser.open("youtube.com")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("google" in req)):
            speak("Opening Google for you, please wait")
            print("Opening Google for you, please wait")
            webbrowser.open("google.com")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        elif (("email" in req) or ("gmail" in req )):
            speak("Opening Gmail for you, please wait")
            print("Opening Gmail for you, please wait")
            webbrowser.open("gmail.com")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()

        
        elif (("quit" in req) or ("exit" in req) or ("thank you" in req)):
            print("Exiting...")
            speak("Thank you so much, I would like to help you again, Hope you enjoy the journey in Python World")
            print("Thank you so much,\nI would like to help you again,\nHope you enjoy the journey in Python World...")
            break

        else:
            speak("Sorry but I didn't understand your Requirement")
            print("Sorry but I didn't understand your Requirement")
            speak("Press Enter to Continue")
            print("Press Enter to Continue-")
            wait = input()




        

        
        
        

