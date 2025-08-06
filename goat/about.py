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

from goat.config import __BUILD__, __VERSION__, resource_path


class AboutWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(100, 100, 300, 400)

        self.center_on_screen()

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        # filler
        self.filler = QWidget()
        self.filler.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # image
        self.image = QLabel(self)
        self.image.setMinimumSize(200, 200)
        self.image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(resource_path("hoppon.png"))
        self.image.setPixmap(pixmap)

        # font
        font1 = QFont()
        font1.setFamily("Helvetica")
        font1.setPointSize(18)
        font1.setWeight(QFont.Weight.Black)  # 900

        # text
        self.version = QLabel(f"GoatClicker v{__VERSION__}+build{__BUILD__}")
        self.version.setAlignment(Qt.AlignCenter)
        self.version.setFont(font1)

        self.copyright = QLabel(f"© 2025 Hoppon. \n All Rights Reserved.")
        self.copyright.setAlignment(Qt.AlignCenter)

        # button
        self.btn = QPushButton("OK")
        self.btn.pressed.connect(self.quit)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.image)
        layout.addWidget(self.filler)
        layout.addWidget(self.version)
        layout.addWidget(self.copyright)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        print("[ABOUT] AboutWindow instantiated")

    def quit(self):
        print("[ABOUT] Destroying about window")
        self.hide()

    def center_on_screen(self):
        screen = QApplication.primaryScreen()  # primary screen
        screen_geometry = screen.availableGeometry()  # available geometry of screen
        center_point = screen_geometry.center()  # calculate center point

        window_geometry = self.frameGeometry()  # frame geometry
        window_geometry.moveCenter(
            center_point
        )  # move window top-left corner to center

        self.move(window_geometry.topLeft())  # Set the new geometry for the window
