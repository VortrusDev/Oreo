#!/usr/bin/env python3

# Implements speech recognition

# TODO: implement a way to check inside the strings
# for the necessary info
# TODO: add noise reduction
import pyaudio
from speechfuncs import *
from settings import dev_index

def main():
    setup() # Creates recognizer and gets mic, then starts
            # execution

def setup():
    mic = sr.Microphone(device_index=dev_index)
    recognizer = getrecognizer()
    with mic as source:
        while 1:
            listen(mic, recognizer)

if __name__ == "__main__":
    main()