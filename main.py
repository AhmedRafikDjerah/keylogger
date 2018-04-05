from listener import Listener
from pynput import keyboard


l = Listener()

with keyboard.Listener(on_press = l.on_press, ) as listener:
    listener.join()


