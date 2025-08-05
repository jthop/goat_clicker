import json
import os
import sys
from sys import platform

from appdirs import AppDirs

__VERSION__ = "0.1.7"
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
        "cps": 1,
        "hotkey": {"<f10>": "F10"},
    }

    def __init__(self):
        """
        Perform any necessary initializations here, e.g.:
        - Loading settings from a file
        """

        self.spam_log()
        self.determine_platform()

        dirs = AppDirs(__APP_NAME__, __AUTHOR__)
        self.dir = dirs.user_config_dir
        self.file_name = f"{self.dir}/prefs.json"

        self.load()
        print(self.payload)

    def spam_log(self):
        print(f"Running Goat Clicker v{__VERSION__}")
        if getattr(sys, "frozen", False):
            print(f"Running in pyinstaller bundle - {sys._MEIPASS}")
        else:
            print("NOT Running in pyinstaller bundle.")

    def determine_platform(self):
        self.platform = None
        self.icon = None

        if platform == "linux":
            self.platform = "linux"
            self.icon = "black.png"
        elif platform == "linux2":
            self.platform = "linux"
            self.icon = "black.png"
        elif platform == "darwin":
            self.platform = "mac"
            self.icon = "white.png"
        elif platform == "win32":
            self.platform = "windoze"
            self.icon = "black.png"

        print(f"Running {self.platform} platform")

    def create_dir(self, dir):
        try:
            os.mkdir(dir)
            print(f"Directory '{dir}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dir}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{dir}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @property
    def file_exists(self):
        if os.path.exists(self.file_name):
            return True
        return False

    def load(self):
        if self.file_exists:
            with open(self.file_name, "r") as f:
                self.payload = json.load(f)
        else:
            self.payload = self.DEFAULT

    def persist(self):
        # First make sure directory exists
        if not os.path.isdir(self.dir):
            print(f"{self.dir} does not exist, creating.")
            self.create_dir(self.dir)

        with open(self.file_name, "w+", encoding="utf-8") as f:
            json.dump(self.payload, f, indent=4, ensure_ascii=False)


settings = AppConfig()
