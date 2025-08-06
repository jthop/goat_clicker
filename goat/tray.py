from PySide6.QtGui import QAction, QCursor, QGuiApplication, QIcon, Qt
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from goat.about import AboutWindow
from goat.clicker import AutoClicker
from goat.config import cfg, resource_path
from goat.settings import SettingsWindow


class SysTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)  # Create the icon

        # Internal variables
        self._clicker_clicking = False

        # Instantiate other windows we will use
        self.about = AboutWindow()
        self.settings = SettingsWindow()
        print(f"[TRAY] AboutWindow and SettingsWindow instantiated")

        self.icon = QIcon(resource_path(cfg.icon))
        self.setIcon(self.icon)

        # First setup QActions
        self.create_actions()

        # Setup Context Menu
        self.menu = QMenu()
        self.menu.addAction(self.toggle_action)
        self.menu.addSeparator()
        self.menu.addAction(self.settings_action)
        self.menu.addAction(self.about_action)
        self.menu.addAction(self.quit_action)
        self.setContextMenu(self.menu)

        # signals
        self.activated.connect(self.on_tray_activated)
        self.show()

    def create_actions(self):
        self.toggle_action = QAction(AutoClicker.NOT_CLICKING_TEXT)
        self.about_action = QAction("About")
        self.settings_action = QAction("Settings")
        self.quit_action = QAction("Quit")

        self.about_action.triggered.connect(self.about.show)
        self.settings_action.triggered.connect(self.settings.show)
        print(f"[TRAY] context menu actions created")

    def signal_rx(self, arg):
        """
        Connected to the hotkey thread via signals.  Must be done like this
        to prevent the GUI from crashing or behaving poorly.  Here we keep
        our own boolean variable: _clicker_clicking and track the clicker
        status ourselves to keep everything separate.  Maybe not the best
        idea, but besides separation, we don't worry about race conditions.
        """

        print(f"[TRAY] Systray rx signal.  Updating toggle_action via setText")
        self._clicker_clicking = not self._clicker_clicking
        if self._clicker_clicking:
            self.toggle_action.setText(AutoClicker.IS_CLICKING_TEXT)
        else:
            self.toggle_action.setText(AutoClicker.NOT_CLICKING_TEXT)

    # def show_about(self):
    #     self.about.show()

    # def show_settings(self):
    #     self.settings.show()

    def on_tray_activated(self, reason):
        print(f"[TRAY] Activation reason: {reason}")
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # This is typically a left-click on Windows, or the default context menu trigger on other platforms.
            # You can explicitly show the menu at the cursor position if needed for specific behavior.
            pass
        elif reason == QSystemTrayIcon.ActivationReason.Context:
            # This is typically a right-click, which automatically shows the context menu set by setContextMenu().
            pass  # No explicit action needed here as setContextMenu handles it.
        elif reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            # Handle double-click, e.g., show the main application window.
            pass
