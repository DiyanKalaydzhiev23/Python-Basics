# pip install pynput

from pynput import keyboard


def on_press(event):
    print("Pressed:", event)


def on_release(event):
    print("Released:", event)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
