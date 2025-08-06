import threading
import time

# import keyboard
from pynput.mouse import Button, Controller


class AutoClicker(threading.Thread):
    NOT_CLICKING_TEXT = "Start (F10)"
    IS_CLICKING_TEXT = "Stop (F10)"

    def __init__(self):
        super().__init__()
        self.btn = Button.left
        self.clicking = False
        self.active = True
        self.paused = False
        self.skip_tick = False

        self.cps = 1
        self.sleep = 1 / self.cps
        self.mouse = Controller()

        print("[CLICKER] Clicker object instantiated")

    @property
    def is_clicking(self):
        """
        Property to determine if class instance is actively clicking
        """
        return self.clicking and self.active

    @property
    def menu_text(self):
        """
        Currently unused prop, would like to use this in the future when
        setting the systray menu text.
        """

        if self.clicking:
            return self.IS_CLICKING_TEXT
        return self.NOT_CLICKING_TEXT

    def start_clicking(self):
        """
        setter for self.clicking
        """

        self.clicking = True

    def stop_clicking(self):
        """
        setter for self.clicking
        """

        self.clicking = False

    def pause(self):
        """
        courtesy - context menu doesn't get auto clicked
        """

        self.paused = True
        print("[CLICKER] clicker paused")

    def unpause(self):
        """
        courtesy - context menu doesn't get auto clicked
        Skip 1 tick after unpausing to make surfe we are still clicking.
        Otherwise there is a vagrant click before toggle
        """

        self.paused = False
        self.skip_tick = True
        print("[CLICKER] clicker UN-paused")

    def exit(self):
        """
        Terminate the thread
        """

        self.clicking = False
        self.active = False
        print("[CLICKER] Clicker thread terminated")

    def run(self):
        """
        The main method for the thread to run.
        """

        print("[CLICKER] Clicker thread started")
        while self.active:
            while self.clicking and not self.paused:
                # Skip 1 iteration of the loop after unpausing to ensure still clicking
                if self.skip_tick:
                    self.skip_tick = False
                    print("[CLICKER] Skipping tick")
                else:
                    self.mouse.press(self.btn)
                    self.mouse.release(self.btn)
                    print("[CLICKER] click")
                time.sleep(self.sleep)

    def toggle(self):
        print("[CLICKER] Toggling clicker")
        if self.is_clicking:
            self.stop_clicking()
        else:
            self.start_clicking()
