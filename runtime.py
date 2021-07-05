import time
import os
import pickle
from main import ImageToAscii

obj = ImageToAscii("kek.mp4", 5)
obj.video_ascii()

def read():
    pickle_off = open("output.txt", "rb")
    emp = pickle.load(pickle_off)
    for el in emp:
        print(el)
        time.sleep(0.0)
        os.system('clear')

read()
os.system('clear')