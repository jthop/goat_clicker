from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from config import __VERSION__, resource_path, settings


class SettingsWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 250, 200)

        self.center_on_screen()

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        # font
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setWeight(QFont.Weight.Bold)  # 900

        filler = QWidget()
        filler.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # text
        self.label1 = QLabel(f"CPS (clicks per second): {settings.payload.get("cps")}")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(font)
        self.label2 = QLabel(f"Hotkey: {settings.payload.get("hotkey")}")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(font)

        # button
        self.btn = QPushButton("OK")
        self.btn.pressed.connect(self.quit)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(filler)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def quit(self):
        print("Destroying settings window")
        self.destroy()

    def center_on_screen(self):
        screen = QApplication.primaryScreen()  # primary screen
        screen_geometry = screen.availableGeometry()  # available geometry of screen
        center_point = screen_geometry.center()  # calculate center point

        window_geometry = self.frameGeometry()  # frame geometry
        window_geometry.moveCenter(
            center_point
        )  # move window top-left corner to center

        self.move(window_geometry.topLeft())  # Set the new geometry for the window
