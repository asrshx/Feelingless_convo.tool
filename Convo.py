from platform import system
import sys
import os
import datetime   
from time import sleep
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()



def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   


       __________  ____  __  __
      / ____/ __ \/ __ \/ / / /
     / /_  / /_/ / /_/ / / / /
    / __/  \__, / _, _/ /_/ /
   /_/    /____/_/ |_|\____/                       
                                      """   
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mF9RM9N \033[1;97m                                    ║
\033[1;97m║\033[1;93m* \033[1;97mN1CKN9M3  \033[1;91m : \033[1;96mN9RUT0  \033[1;97m                                   ║
\033[1;97m║\033[1;93m* \033[1;97m0WN3R   \033[1;91m: \033[1;96mF9RMAN S1DDUQU3  \033[1;97m                                    ║
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/profile.php?id=61565520028828\033[1;97m         ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()


headers = {
   'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


def message_on_messenger(message):
    for i in ns:
        try:
            message = str(mn) + i
            url = "https://graph.facebook.com/v15.0/{0}/".format('t_' + str(thread_id))
            parameters = {'access_token': access_token, 'message': message}
            s = requests.post(url, data=parameters, headers=headers)
            tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            

            if s.ok:
                e =datetime.now()
                print("\033[1;35m", end = "")
                print("--> Convo Or Inbox I'd Link  :--", thread_id)
                print (e.strftime("--> F9RMAN H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Message Successfully Sent By N9RUT0 D0N :D ::-->> ", message, "\n")
                time.sleep(timm)
            else:
                print('\033[1;32m[x] Message Block ' + tt, '\n[×] Token Error\n')
                time.sleep(30)
        except Exception as e:
            print("\033[1;31;40m", end = "")
            print(e , '\n')           
            time.sleep(30)

def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")


if int:
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ Facebook Tool Create by N9RUT0 1NX1D3 ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/profile.php?id=61565520028828 ]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ Tool Fucker == > [ Naruto Insiide ]\n''')
    print("\033[1;36;40m", end = "")
    mo=str(input("\033[1;36m[+] Mobile Number :: "))
    token = input("[+] Input Token File Name :: ")
    print('\n')
    with open(token, 'r') as f2:
        access_token = f2.read()
        payload = {'access_token': access_token}
        a = "https://graph.facebook.com/v15.0/me"
        b = requests.get(a, params=payload)
        d = json.loads(b.text)
        if 'name' not in d:
            print(BOLD + RED + '\n[x] Token Invalid..!!')
            sys.exit()
        mb = d['name']
        print('\033[1;32mYour Profile Name :: \033[1;32;1m%s' % (mb))
        print('\n')
        thread_id = input(BOLD + CYAN + "\033[1;36m[+] Conservation ID :: \033[1;32;1m")
        mn= input(BOLD + CYAN + "\033[1;36m[+] Enter Kidx Name :: \033[1;32;1m")
        ms = input(BOLD + CYAN + "\033[1;36m[+] Add Gali File Name :: \033[1;32;1m")
        repeat = int(input(BOLD + CYAN + "\033[1;36m[+] File Repeat No :: \033[1;32;1m"))
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
        print('\n')
        print('''\033[1;34m________All Done....Loading Profile Info.....!''')
        print('\033[1;34mYour Profile Name :: ', mb)
        print('\n')
        ns = open(ms, 'r').readlines()
        

        for i in range(repeat):
            messenger = get_messages()
            message_on_messenger(thread_id)
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
