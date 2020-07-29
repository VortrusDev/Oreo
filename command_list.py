#!/usr/bin/env python3

from command import *
from settings import *
import os
import webbrowser

def sayHello():
    "Says hello to the user"
    print("Hello!")
"""
greeting_commands = Command(["hello " + name.lower(),
                             "hey " + name.lower()], sayHello)

# Opens the preferred code editor
code_editor_commands = Command(["hey " + name.lower() + " open ide",
                                "hey " + name.lower() + " open code editor",
                                "hey " + name.lower() + " open notepad"],
                               os.system)

# Opens a new terminal instance
terminal_commands = Command(["hey " + name.lower() + " open terminal",
                             "hey " + name.lower() + " open command prompt"],
                            os.system)
"""
# Should do an array of arrays for command name so that
# I can parse for if it's youtube or wikipedia, etc
website_commands = Command([["hey", name.lower(),"open", "youtube"],
                            ["hey", name.lower(),"open", "wikipedia"]], webbrowser.open)

search_commands = Command([["hey", name.lower(),"search", "youtube"]],
                          webbrowser.open)