# Oreo
A small personal assistant I wrote for Raspberry Pi OS. Can hear voice commands and interpret them. 

## Functionality
Oreo is in development right now to be a "Google Home" for my house on my Raspberry Pi 2. As a result, it cannot do much at the time of writing this, but it has a slew of features planned.

## Planned Features
- Functional voice recognition for searching the web and playing music
- Will act as a media center upon command
- Will display weather on command
- Will have a "sleep mode" which can do various behaviors, including ASMR
- Will be able to tell really funny dad jokes
- Will be able to "talk" with Text-To-Speech
- Will be able to interface with lights using breadboards and manipulate the lights to the tune of music

## How To Run Oreo
Since this project is very early in development, it requires some technical knowledge to run.

Oreo is intended to run on Raspberry Pi OS, and as a result will likely work on Debian and other Linux distros with minimal effort but will not work on Windows (yet). 

To get Oreo started: 
- Download a valid Python installation (I used Python3 for development)
- Edit Settings.py to have your device index for your mic as well as your command to open the terminal and the names of your favorite code editors (this will be automated in the future)
- Navigate to the directory of the main.py file and then run it with "python3 main.py"
