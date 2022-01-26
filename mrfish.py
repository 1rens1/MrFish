import requests
import os
import random
import string
import json
import threading
from requests.exceptions import SSLError
from datetime import datetime


def generate_random_name():
    event = random.randint(0, 4)
    if event == 0:
        return str(random.choice(names)).lower()
    elif event in [1, 2]:
        separator = ['-', '.', '_']
        return str(random.choice(names)).lower() + separator[random.randint(0, len(separator) - 1)] + str(
            random.choice(names)).lower()
    else:
        return str(random.choice(names)).lower() + random.choice(string.digits) + random.choice(string.digits)


def generate_random_password():
    event = random.randint(0, 6)
    if event == 0:
        return ''.join(random.choice(chars) for i in range(random.randint(7, 15)))
    elif event in [1, 2]:
        return random.choice(dictionary) + random.choice(dictionary) + random.choice(string.digits)
    elif event in [3, 4]:
        return random.choice(dictionary) + random.choice(string.digits)
    else:
        return random.choice(string.digits) + random.choice(dictionary) + random.choice(names)


proxy_list = json.loads(open('assets/proxies.json').read())
get_proxy = random.choice(proxy_list)
proxy = {'https': f'https://{get_proxy}'}


def run():
    while True:
        username = generate_random_name() + '@' + random.choice(emails) + \
            '.' + random.choice(ext)
        password = generate_random_password()
        try:
            r = requests.post(url, allow_redirects=False, data={
                str(formDataNameLogin): username,
                str(formDataNamePass): password,
            })
            date = datetime.today().strftime('%H:%m:%S')
            print(
                f'{date}> [Result: {r.status_code}] - [{formDataNameLogin}: {username}] - [{formDataNamePass}: {password}]')
        except SSLError as e:
            print('Error: URL can no longer be reached..')
        except Exception as e:
            print(f'Error: {e}')

"""
                      
        /`·.¸          ___  ___      ______ _     _     
       /¸...¸`:·       |  \/  |      |  ___(_)   | |    
   ¸.·´  ¸   `·.¸.·´)  | .  . |_ __  | |_   _ ___| |__  
  : © ):´;      ¸  {   | |\/| | '__| |  _| | / __| '_ \ 
   `·.¸ `·  ¸.·´\`·¸)  | |  | | |    | |   | \__ \ | | |
       `\\\\´´\¸.·´    \_|  |_/_|    \_|   |_|___/_| |_|
                                                        
                                                        
"""


mrfish_display = """.
 \033[93m       /`·.¸          \033[0m
 \033[93m      /¸...¸`:·       \033[0m \033[93mMrFish\033[0m - Discord Nitro Phishing Form Spammer
 \033[93m  ¸.·´  ¸   `·.¸.·´)  \033[0m
 \033[93m : © ):´;      ¸  {   \033[0m By Daan Van Essen#1337 / Amadeus
 \033[93m  `·.¸ `·  ¸.·´\`·¸)  \033[0m Modified by rens#6161
 \033[93m      `\\\\´´\¸.·´    \033[0m
."""
mrfish_display_list = mrfish_display.split('\n')

if __name__ == '__main__':
    for i in mrfish_display_list:
        os.system(f'echo{i}')
    url = input(' Form Request URL: ')
    formDataNameLogin = input(' Form Data Username [Account/Email] Name: ')
    formDataNamePass = input(' Form Data Password Name: ')
    while True:
        threads = input(' Threads [recommend max of 32]: ')
        if threads.isdigit() and 1 <= int(threads) <= 5000:
            threads = int(threads)
            break
        else:
            print(' Please enter a valid number between 0 and 5001')
            continue
    while True:
        use_proxy = input(' Enable Proxy [Y/N]: ')
        if use_proxy.lower() in ('y', 'n'):
            if use_proxy.lower() == 'y':
                break
            if use_proxy.lower() == 'n':
                proxy = {}
                break
        else:
            print(' That is not a valid option')
            continue

    chars = string.ascii_letters + string.digits
    random.seed = (os.urandom(1024))

    names = json.loads(open('assets/names.json').read())
    emails = json.loads(open('assets/emails.json').read())
    ext = json.loads(open('assets/extensions.json').read())
    dictionary = json.loads(open('assets/dictionary.json').read())

    for i in range(threads):
        t = threading.Thread(target=run)
        t.start()