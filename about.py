from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

from config import __VERSION__, resource_path, settings


class AboutWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 300, 350)

        self.center_on_screen()

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        # image
        self.image = QLabel(self)
        self.image.setMinimumSize(200, 200)
        self.image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(resource_path("black.png"))
        self.image.setPixmap(pixmap)

        # font
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(QFont.Weight.Black)  # 900

        # text
        self.label1 = QLabel(f"Goat Clicker v{__VERSION__}")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(font)
        self.label2 = QLabel(f"© 2025 Hoppon. \n All Rights Reserved.")
        self.label2.setAlignment(Qt.AlignCenter)

        # button
        self.btn = QPushButton("OK")
        self.btn.pressed.connect(self.quit)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.image)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def quit(self):
        print("Destroying about window")
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
