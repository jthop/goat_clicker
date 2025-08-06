import sys

from PySide6.QtWidgets import QApplication

from goat.clicker import AutoClicker
from goat.hotkey import HotKeyManager
from goat.signals import ToggleSignal
from goat.tray import SysTray

# create app object first, connecting tray.quit to app.quit later
app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Now we can create the tray icon, and wire up it's quit to app
tray = SysTray()
tray.quit_action.triggered.connect(app.quit)

# Create the clicker thread instance, and signal instance
clicker = AutoClicker()
toggle_signal = ToggleSignal()

# When are signals sent ?
# When hotkey manager is triggered, or user clicks the tray
manager = HotKeyManager(signal_cb=toggle_signal.send)
tray.toggle_action.triggered.connect(toggle_signal.send)

# When a signal is received, what should we do?
# toggle clicker thread and update the context menu
toggle_signal.received.connect(clicker.toggle)
toggle_signal.received.connect(tray.signal_rx)

# context menu show/hide connects to clicker pause/unpause
tray.menu.aboutToHide.connect(clicker.unpause)
tray.menu.aboutToShow.connect(clicker.pause)


def clean_exec():
    clicker.start()
    manager.start()
    app.exec()
    clicker.exit()
    manager.exit()


# Add the menu to the tray
sys.exit(clean_exec())
