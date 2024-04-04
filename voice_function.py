import pyttsx3 
from voice_settings import requirements


def voice_speak(phrase=["This is a default text"]):
    try:
        engine = pyttsx3.init()
        for text in phrase:
            print(f">> Says: {text}")
            engine.say(text)
            engine.runAndWait()
    except ImportError:
        requirements(True)
        voice_speak(phrase)


def voice_list():
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Id: {voice.id} - Name: {voice.name} - Languages: {voice.languages}")