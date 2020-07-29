#!/usr/bin/env python3
from actions import *
import speech_recognition as sr

if __name__ == "__main__":
    print("The Google recognition module is not meant to be run as main.")
    print("It is simply a function library to help " + name + " run Google speech recognition.")
    print("Run 'main.py' to start up " + name + ".")

def recognize_google(audio, r):
    try:
        result = r.recognize_google(audio)
        print("Google: \"" + result + "\"")
        takeinput(result)
    except sr.UnknownValueError:
        print("No input heard.")
    except sr.RequestError as e:
        print("Google had an oopsie. {0}".format(e))
    