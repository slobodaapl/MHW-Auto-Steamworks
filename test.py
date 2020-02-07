from time import sleep
import reader
import keyboard
from time import time
import warnings
import os
from ahk import AHK
from random import randint, seed
import pywinauto

stop = False

warnings.filterwarnings("ignore")


def end():
    global stop
    stop = True


a = pywinauto.application.Application().connect(best_match="MONSTER HUNTER: WORLD")
window = a.window(best_match="MONSTER HUNTER: WORLD")
window.set_focus()
print("Running, don't worry about that error you saw")
print("I swear it was nothing. Press F10 to quit anytime.")

seed(time())
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'AutoHotKey.exe')
kb = AHK(executable_path=filename)
sleep(1)
sleep(0.25)
kb.key_press('Space') if stop is not True else None
sleep(1)

keyboard.add_hotkey('f10', end)

if stop is not True:
    proc = reader.ProcReader()
    fuel = proc.get_fuel()
    print(stop)
    print(fuel)
    while fuel > 0:
        a = randint(0, 2)
        b = [0, 1, 2]
        b.pop(b.index(a))
        if a == 0:
            kb.key_down('a')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('a')
        elif a == 1:
            kb.key_down('w')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('w')
        elif a == 2:
            kb.key_down('d')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('d')
        sleep(0.20)
        a = randint(0,1)
        if b[a] == 0:
            kb.key_down('a')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('a')
        elif b[a] == 1:
            kb.key_down('w')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('w')
        elif b[a] == 2:
            kb.key_down('d')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('d')
        b.pop(a)
        sleep(0.20)
        if b[0] == 0:
            kb.key_down('a')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('a')
        elif b[0] == 1:
            kb.key_down('w')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('w')
        elif b[0] == 2:
            kb.key_down('d')
            d = randint(-10, 10)
            sleep(0.05 + d / 1000)
            kb.key_up('d')
        kb.key_press('Space')
        sleep(0.45)
        fuel = proc.get_fuel()
        if stop is True:
            proc.quit()
            break

print("Ended")
os.system('pause')