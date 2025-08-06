from PySide6 import QtCore


class ToggleSignal(QtCore.QObject):
    """
    Signal class to communicate pynput keyboard detection thread events to
    QT GUI thread process methods, while avoiding hangups and errors due to
    direct calls from one type of thread to another.
    """

    received = QtCore.Signal(str)  # Note: this is a class variable

    def __init__(self):
        # Initialize KeySignal as QObject
        QtCore.QObject.__init__(self)
        print(f"[SIG] Signal object instantiated")

    def send(self, sigstr="none"):
        """Emits signal for key press event"""
        self.received.emit(sigstr)
        print(f"[SIG] Signal emitted")
