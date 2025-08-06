import json
import os
import sys
from sys import platform

from PySide6.QtGui import QGuiApplication, Qt

from goat.appdirs import AppDirs

__VERSION__ = "0.2.1"
__BUILD__ = "23"
__APP_NAME__ = "goat_clicker"
__AUTHOR__ = "hoppon"


def resource_path(relative):
    if getattr(sys, "frozen", False):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in a normal Python environment
        abs_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.join(abs_path, "data")

    return os.path.join(base_path, relative)


class AppConfig:
    """
    Configuration File
    """

    APP_NAME: str = "Goat Clicker"
    DEFAULT = {
        "rest": {"random": True, "range": [0.1, 5]},
        "duration": {"random": True, "range": [0.1, 0.5]},
        "interval": {"random": True, "range": [150, 150]},
    }

    def __init__(self):
        """
        Perform any neccwcessary initializations here, e.g.:
        - Loading settings from a file
        """
        self.color_scheme = None
        self.platform = None
        self.icon = None

        self.spam_log()

        self.dir = AppDirs(__APP_NAME__, __AUTHOR__).user_config_dir
        self.filename = f"{dir}/prefs.json"

        self.load()
        print(f"[CONFIG] cfg object instantiated = {self.payload}")

    def spam_log(self):
        print(f"[CONFIG] Running Goat Clicker v{__VERSION__}")
        if getattr(sys, "frozen", False):
            print(f"[CONFIG] Running in pyinstaller bundle - {sys._MEIPASS}")
        else:
            print("[CONFIG] NOT Running in pyinstaller bundle.")

        self.determine_color_scheme()
        self.determine_platform()
        print("[CONFIG] Running on {self.platform} platform")
        print("[CONFIG] Using icon: {self.icon}")
        print("[CONFIG] Color scheme {self.color_scheme}")

    def determine_platform(self):
        if platform == "linux":
            self.platform = "LINUX"
            self.icon = "black.png"
        elif platform == "linux2":
            self.platform = "LINUX"
            self.icon = "black.png"
        elif platform == "darwin":
            self.platform = "MAC"
            self.icon = "blue.png"
        elif platform == "win32":
            self.platform = "WINDOWS"
            self.icon = "blue.png"

    def determine_color_scheme(self):
        cs = QGuiApplication.styleHints().colorScheme()
        if cs == Qt.ColorScheme.Dark:
            self.color_scheme = "DARK"
        elif cs == Qt.ColorScheme.Light:
            self.color_scheme = "LIGHT"
        elif cs == Qt.ColorScheme.Unknown:
            self.color_scheme = "UNKNOWN"
        else:
            self.color_scheme = "UNKNOWN++"

    def create_dir(self, dir):
        try:
            os.mkdir(dir)
            print(f"[CONFIG] Directory '{dir}' created successfully.")
        except FileExistsError:
            print(f"[CONFIG] Directory '{dir}' already exists.")
        except PermissionError:
            print(f"[CONFIG] Permission denied: Unable to create '{dir}'.")
        except Exception as e:
            print(f"[CONFIG] An error occurred: {e}")

    @property
    def file_exists(self):
        if os.path.exists(self.filename):
            return True
        return False

    def load(self):
        if self.file_exists:
            with open(self.filename, "r") as f:
                self.payload = json.load(f)
        else:
            self.payload = self.DEFAULT

    def persist(self):
        # First make sure directory exists
        if not os.path.isdir(self.dir):
            print(f"[CONFIG] {self.dir} does not exist, creating.")
            self.create_dir(self.dir)

        with open(self.filename, "w+", encoding="utf-8") as f:
            json.dump(self.payload, f, indent=4, ensure_ascii=False)


cfg = AppConfig()
