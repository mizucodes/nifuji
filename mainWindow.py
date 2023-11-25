from PyQt5.QtWidgets import QMainWindow, QTextEdit
from PyQt5.QtGui import QIcon
from menuBar import MenuBar  # Ensure this matches the name of your menu bar file
from themeManager import ThemeManager
from textEditor import TextEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window icon
        self.setWindowIcon(QIcon("resources/logo.png"))

        # Configuration of the window
        self.setWindowTitle("nifuji")  # Title of window
        self.setGeometry(100, 100, 800, 600)  # Size of window

        # Set the main widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Create and set the menu bar
        self.menuBar = MenuBar(self)
        # new below
        self.textEditor = TextEditor(self)
        self.setCentralWidget(self.textEditor)

        # Initialize ThemeManager
        self.themeManager = ThemeManager(self)

    def applyTheme(self, theme_name):
        # Apply the selected theme
        self.themeManager.applyTheme(theme_name)
