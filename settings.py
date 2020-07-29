#!/usr/bin/env python3

# Holds settings for the bot

name = "Oreo"
timeout_seconds = 3
preferred_code_environment = "thonny"
explorer_open_command = "xdg-open ."
terminal_open_command = "lxterminal"
dev_index = 0 # Device index of mic

if __name__ == "__main__":
    print("The settings module is not meant to be run as main.")
    print("It is simply variable to help " + name + " know what to do.")
    print("Run 'main.py' to start up " + name + ".")