import speech_recognition as op
import  pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener =op.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine. runAndWait()

def take_command():
    try:
        with op.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sara' in command:
                command = command.replace('sara','')
                print(command)

    except:
        pass
    return command


def run_sara():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+time)

    elif 'search for 'in command:
        person = command.replace('search for','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'tushar 'in command :
        talk(" one of the handsome man in the world")
    elif 'prakash' in command:
        talk("father of . tushar thorat")
    elif ' rohit' in command:
        talk('brother of tushar thorat')
    elif 'vivek' in command :
        talk("happy birthday to you vivek")
    elif 'hello' in command:
        talk('hi tushar how i can help you  ')
    else:
        talk('sorry can you say    it again.')

run_sara()




