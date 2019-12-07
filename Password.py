import random
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?"

def ranpass(length):
    password = ""
    for i in range(0, int(length)):
        randomspot = random.randint(0, len(chars))
        spot = chars[randomspot:randomspot + 1]
        password += spot

    return password

def start():
    passLen = input("How long do you want your password to be?: ")
    try:
        int(passLen)
        print(ranpass(passLen))
        start()
    except:
        print("Not an integer...")
        start()

start()

