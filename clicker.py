import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os

delay = 0.1
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
special_key = KeyCode(char='c')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def change_delay(self,new_delay):
        print(new_delay)
        tmp = 1 / new_delay
        self.delay = tmp
        self.prints()

    def prints(self):
        try:
            os.system('clear')
        except:
            os.system('cls')
        print("Ready to go")
        print("Clicks per second = {}".format(int(1/self.delay)))
        print("Controls:")
        print("\ts = Start/Stop")
        print("\te = Exit")
        print("\tc = Change clicks per second")
        print("\n\n=====================================")
        

    def run(self):
        print("Auto Clicker by Euan Morgan\n\n")
        self.prints()
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if not click_thread.running:
            click_thread.start_clicking()
            
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
def on_release(key):
    if key == special_key:
        tmp = input("Clicks per second >> ")
        if tmp.isdigit():
            click_thread.change_delay(int(tmp))
        elif tmp[1:].isdigit():
            click_thread.change_delay(int(tmp[1:]))
        else:
            print("Error! Please only enter numeric values. Press c again to enter another value")
    elif key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
