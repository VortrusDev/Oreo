#!/usr/bin/env python3
import speech_recognition as sr
from googlerecognition import *
from settings import timeout_seconds

if __name__ == "__main__":
    print("The speech functions module is not meant to be run as main.")
    print("It is simply a function library to help " + name + " run speech recognition.")
    print("Run 'main.py' to start up " + name + ".")


def getrecognizer():
    "This function gets the recognizer for speech recognition and returns it."
    print("Getting recognizer.")
    return sr.Recognizer();

def listen(m, r):
    "This function listens to the actual audio on loop."
    audio = r.listen(m, None, timeout_seconds)
    recognize_google(audio, r)
    return