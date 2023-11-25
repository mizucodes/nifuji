from PyQt5.QtWidgets import QTextEdit


class TextEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize text editor settings here

        # possible set default font, text wrap, etc.
