from about import AboutWindow
from PySide6.QtGui import QAction, QCursor, QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from clicker import AutoClicker
from config import resource_path, settings
from settings import SettingsWindow


class SysTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)  # Create the icon

        # Internal variables
        self._clicker_clicking = False

        self.icon = QIcon(resource_path(settings.icon))
        self.setIcon(self.icon)

        # Menu
        self.menu = QMenu()

        # Clicker Toggle
        # Menu is created first so NOT_CLICKING_TEXT is used initially
        self.toggle_action = QAction(AutoClicker.NOT_CLICKING_TEXT)
        self.menu.addAction(self.toggle_action)
        self.menu.addSeparator()

        # Settings Action
        self.settings_action = QAction("Settings")
        self.settings_action.triggered.connect(self.show_settings)
        self.menu.addAction(self.settings_action)

        # About Action
        self.about_action = QAction("About")
        self.about_action.triggered.connect(self.show_about)
        self.menu.addAction(self.about_action)

        # Quit Action
        self.quit_action = QAction("Quit")
        self.menu.addAction(self.quit_action)

        # signals
        self.activated.connect(self.on_tray_activated)

        # context menu
        self.setContextMenu(self.menu)

        self.show()

    def signal_rx(self, arg):
        """
        Connected to the hotkey thread via signals.  Must be done like this
        to prevent the GUI from crashing or behaving poorly.  Here we keep
        our own boolean variable: _clicker_clicking and track the clicker
        status ourselves to keep everything separate.  Maybe not the best
        idea, but besides separation, we don't worry about race conditions.
        """

        self._clicker_clicking = not self._clicker_clicking
        if self._clicker_clicking:
            self.toggle_action.setText(AutoClicker.IS_CLICKING_TEXT)
        else:
            self.toggle_action.setText(AutoClicker.NOT_CLICKING_TEXT)

    def show_about(self):
        self.about = AboutWindow()
        self.about.show()

    def show_settings(self):
        self.settings = SettingsWindow()
        self.settings.show()

    def on_tray_activated(self, reason):
        print(reason)
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
