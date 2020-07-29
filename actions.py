#!/usr/bin/env python3
from settings import *
from command import *
from gtts import gTTS
from io import BytesIO
from command_list import *

import os
import webbrowser

if __name__ == "__main__":
    print("The actions module is not meant to be run as main.")
    print("It is simply a function library to help " + name + " run Google speech recognition.")
    print("Run 'main.py' to start up " + name + ".")

def handleYoutubeSearch(input, search_commands):
    # Hey oreo search youtube for .....
    query = input[5:len(input)]
    print("Querying...")
    print(query)
    search_query = ""
    for word in query:
        if word != query[-1]:
            search_query += word+"+"
        else:
            search_query += word
    search_commands.doAction("https://www.youtube.com/results?search_query=" + search_query)

# This is where we will do behaviors we want the bot to do
    
def takeinput(input):
    low = input.lower().split() # Cutting down on size

    "This will decide what to do with the input based upon what is given"
    """if low in greeting_commands.getCommandArray():
        greeting_commands.doAction(None)
    elif low in code_editor_commands.getCommandArray():
        code_editor_commands.doAction(preferred_code_environment)
    elif low in terminal_commands.getCommandArray():
        terminal_commands.doAction(terminal_open_command)
        """
    for list in website_commands.getCommandArray():

        if low == list and list[-1] == "youtube":
            website_commands.doAction("https://www.youtube.com")
        elif low == list and list[-1] == "wikipedia":
            website_commands.doAction("https://www.wikipedia.org")
    for list in search_commands.getCommandArray():
        print(list)
        print(low[0:3])
        print(list[0:3])
        if low[0:3] == list[0:3] and low[2] == "search":
            if low[3] == "youtube":
                handleYoutubeSearch(low, search_commands)
            elif low[3] == "wikipedia":
                pass