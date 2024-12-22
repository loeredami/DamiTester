import os

COOKIE_MESSAGE = "Hello we are cookies!"

def get_all_cookies():
    # file obviously does not exist
    with open("cookies.txt", "r") as src: data = src.read()
    return data

def clear_cookies():
    os.remove("cookies.txt")

def add_cookies():
    with open("cookies.txt", "w") as dest: dest.write("Hello I am a cookie!")