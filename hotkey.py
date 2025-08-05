from pynput.keyboard import GlobalHotKeys, HotKey, Key, Listener


class HotKeyManager:
    CLICKER_START_DELAY = 1
    DEFAULT_HOTKEY = "<f10>"
    HOTKEY_CHOICES = {
        "F10": "<f10>",
        "ESC": "<esc>",
        "CTRL+SHIFT+T": "<ctrl>+<shift>+t",
        "CMD+SHIFT+T": "<cmd>+<shift>+t",
    }

    def __init__(self, signal_cb=None):
        self._signal_cb = signal_cb
        self.hotkey = self.DEFAULT_HOTKEY
        print(f"Hotkey manager constructed")

    def _cb(self):
        if self._signal_cb:
            print("Hotkey pressed, executing callback")
            self._signal_cb()
        else:
            print("Hotkey pressed but no signal cb registered! Nothing to do.")

    def exit(self):
        self.listener.stop()
        print("Hotkey manager terminated")

    def _for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    def connect(self, cb):
        self._connected_cb = cb

    def start(self):
        hotkey = HotKey(HotKey.parse(self.hotkey), self._cb)
        self.listener = Listener(
            on_press=self._for_canonical(hotkey.press),
            on_release=self._for_canonical(hotkey.release),
        )
        self.listener.start()

    def _using_global_hotkeys(self):
        """
        Construct dict to use as arg for GlobalHotkeys.
        Key (hotkey) is a string variable so tedius construction required.
        """

        hotkeys = {}
        hotkeys[self.DEFAULT_HOTKEY] = self._cb
        self.listener = GlobalHotKeys(hotkeys)
        self.listener.start()
        print(f"Hotkey manager thread started")
        print(f"Using hotkeys: {hotkeys}")

    def _OLD(self):
        """
        No longer used, saving only in case...
        """

        self.listener = GlobalHotKeys(
            {
                "<f10>": self._toggle,
            }
        )
        self.listener.start()
