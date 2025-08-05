from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QGroupBox,
    QRadioButton,
    QVBoxLayout,
)

from config import __VERSION__


class CustomDialog(QDialog):
    def __init__(self, parent=None):  # <1>
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        group_box = QGroupBox("Some radio buttons")

        radio1 = QRadioButton("Radio 1")
        radio2 = QRadioButton("Radio 1")
        radio3 = QRadioButton("Radio 1")

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(radio1)
        radio_layout.addWidget(radio2)
        radio_layout.addWidget(radio3)

        group_box.setLayout(radio_layout)

        button_box = QDialogButtonBox(QBtn)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(group_box)
        layout.addWidget(button_box)
        self.setLayout(layout)


def show_about():
    msg_box = QMessageBox()
    msg_box.setText(f"Goat Clicker v. {__VERSION__}")
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.exec()


def show_settings():
    settings = CustomDialog()
    settings.exec()
    settings.showMinimized()
    settings.show()
