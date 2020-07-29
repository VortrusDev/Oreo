#!/usr/bin/env python3
from settings import *
# The commands that the bot will use to evaluate
# what action to take

if __name__ == "__main__":
    print("The commands module is not meant to be run as main.")
    print("It is simply a Command class.")
    print("Run 'main.py' to start up " + name + ".")
    
class Command:
    'The base class for all commands.'
    def __init__ (self, command_array, action):
        self.command_array = command_array  # If input matches array
                                            # then do action
        self.action = action
    def doAction(self, argument):
        if argument != None:
            self.action(argument)
        else:
            self.action()
    def getCommandArray(self):
        return self.command_array