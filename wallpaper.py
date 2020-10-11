import random
import ctypes
import time
import os
import sys

command = sys.argv
path = "C:\\Users\\dell\\Desktop\\wh"
file = os.listdir(path)
filepath = path + "\\" + random.choice(file)
print(filepath)
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)